"""Run one paired Codex response per role. Requires authenticated Codex CLI.
This measures constrained profile responses, not full multi-agent orchestration.
"""
from pathlib import Path
import hashlib
import json
import os
import subprocess
import tempfile
import time
try:
    import tomllib
except ImportError:
    from pip._vendor import tomli as tomllib

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
TASKS=json.loads((HERE/'tasks.json').read_text())
MODEL='gpt-6-astra'
EFFORT='medium'
output=HERE/'outputs'
output.mkdir(exist_ok=True)
meta=[]
with tempfile.TemporaryDirectory(prefix='agentes-comparison-') as sandbox:
    for index,(role,task) in enumerate(TASKS.items()):
        # Alternate order to reduce a systematic warm-cache/order advantage.
        order=['baseline','candidate'] if index%2==0 else ['candidate','baseline']
        for version in order:
            result_file=output/f'{role}-{version}.json'
            profile_path=(HERE/'baseline' if version=='baseline' else ROOT/'agents')/f'{role}.toml'
            profile=tomllib.loads(profile_path.read_text())['developer_instructions']
            event_path=Path(sandbox)/'events.jsonl'
            error_path=Path(sandbox)/'stderr.txt'
            final_path=Path(sandbox)/'answer.json'
            final_path.unlink(missing_ok=True)
            args=['codex','exec','--ignore-user-config','--ephemeral','--skip-git-repo-check',
                  '-C',sandbox,'-s','read-only','-m',MODEL,
                  '-c','model_reasoning_effort="'+EFFORT+'"',
                  '-c','developer_instructions='+json.dumps(profile,ensure_ascii=False),
                  '-c','features.shell_tool=false','-c','features.apps=false',
                  '-c','features.plugins=false','-c','features.memories=false',
                  '-c','skills.bundled.enabled=false','-c','agents.enabled=false',
                  '-c','project_doc_max_bytes=0','--output-schema',str(HERE/'response.schema.json'),
                  '--json','-o',str(final_path),'-']
            print(f'RUN {role} {version}',flush=True)
            start=time.monotonic()
            with event_path.open('w') as events,error_path.open('w') as errors:
                completed=subprocess.run(args,input=task['prompt'],text=True,stdout=events,stderr=errors,timeout=240)
            usage=None
            events=[json.loads(line) for line in event_path.read_text().splitlines() if line.startswith('{')]
            for event in events:
                if event.get('type')=='turn.completed': usage=event.get('usage')
            if completed.returncode or not final_path.exists() or usage is None:
                raise RuntimeError(f'{role} {version} failed: '+error_path.read_text()[-1500:])
            response=json.loads(final_path.read_text())
            record={'role':role,'version':version,'model':MODEL,'reasoning_effort':EFFORT,
                    'elapsed_seconds':round(time.monotonic()-start,2),'usage':usage,
                    'profile_sha256':hashlib.sha256(profile_path.read_bytes()).hexdigest(),
                    'task_sha256':hashlib.sha256(task['prompt'].encode()).hexdigest(),
                    'response':response}
            result_file.write_text(json.dumps(record,ensure_ascii=False,indent=2))
            meta.append({k:v for k,v in record.items() if k!='response'})
            (HERE/'runs.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2))
            print(f'DONE {role} {version} {record["elapsed_seconds"]}s {usage}',flush=True)
