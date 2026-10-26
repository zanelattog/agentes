"""Offline checks for the saved, reviewed synthetic responses. No model calls.
Inspect generated artifacts before running: this executes their Python code.
Run grade_luna.mjs separately (requires Playwright) before this script.
"""
from pathlib import Path
import json, random, subprocess, sys, tempfile
ROOT=Path(__file__).resolve().parent
scores={}
def artifact(role,version):
 return json.loads((ROOT/'outputs'/f'{role}-{version}.json').read_text())['response']['artifact']
def record(role,version,checks):
 scores[f'{role}-{version}']={'passed':sum(bool(v) for v in checks.values()),'total':len(checks),'checks':checks}
expected_atlas=dict(ack_when='after_durable_commit',dedup_key='tenant_and_event_id',persistence='database_inbox_transaction',worker_claim='atomic_claim_or_lock',external_delivery='stable_idempotency_key',new_services='none',retry_policy='bounded_backoff_with_failure_tracking',rollback='preserve_inbox_and_compatible_schema')
gold='''def retry_delay(attempt, base, cap):
    if any(type(x) is not int for x in (attempt,base,cap)): raise TypeError()
    if any(x < 0 for x in (attempt,base,cap)): raise ValueError()
    if base == 0 or cap == 0: return 0
    if base >= cap or attempt >= cap.bit_length(): return cap
    return min(cap, base << attempt)
'''
mutants={
 'wrong_exponent':gold.replace('base << attempt','base << (attempt+1)'),
 'missing_cap':gold.replace('if base >= cap or attempt >= cap.bit_length(): return cap','if False: return cap').replace('min(cap, base << attempt)','base << attempt'),
 'zero_base_wrong':gold.replace('if base == 0 or cap == 0: return 0','if base == 0: return cap\n    if cap == 0: return 0'),
 'accepts_negative':gold.replace('if any(x < 0 for x in (attempt,base,cap)): raise ValueError()','if any(x < 0 for x in (attempt,base,cap)): return 0'),
 'accepts_bool':gold.replace('type(x) is not int','not isinstance(x,int)'),
 'zero_cap_wrong':gold.replace('if base == 0 or cap == 0: return 0','if cap == 0: return 1\n    if base == 0: return 0'),
}
mutation_details={}
for version in ('baseline','candidate'):
 for role,expected in [('atlas',expected_atlas),('iris',dict(R1=True,R2=True,R3=False,R4=True,R5=False,R6=False)),('cora',dict(S1=True,S2=True,S3=True,S4=False,S5=False,S6=False))]:
  actual=json.loads(artifact(role,version)); record(role,version,{k:actual.get(k)==v for k,v in expected.items()})
 ns={}; exec(artifact('nexo',version),ns); allocate=ns['allocate']
 checks={}
 for label,total,weights,expected in [('ties',2,[1,1,1],[1,1,0]),('zero_total',0,[1,2],[0,0]),('zero_weights',5,[0,1,0],[0,5,0]),('proportion',10,[1,2,3],[2,3,5]),('large',10**30+1,[1,1],[5*10**29+1,5*10**29])]:
  original=weights.copy(); checks[label]=allocate(total,weights)==expected and weights==original
 invalid=[(True,[1],TypeError),(1.0,[1],TypeError),(1,(1,),TypeError),(1,[True],TypeError),(1,[1.0],TypeError),(-1,[1],ValueError),(1,[],ValueError),(1,[0,0],ValueError),(1,[-1,2],ValueError)]
 for i,(total,weights,error) in enumerate(invalid):
  try: allocate(total,weights); checks[f'invalid_{i}']=False
  except Exception as e: checks[f'invalid_{i}']=type(e) is error
 rng=random.Random(742); valid=True
 for _ in range(100):
  weights=[rng.randrange(20) for _ in range(rng.randrange(1,20))]
  if not sum(weights): weights[0]=1
  total=rng.randrange(10**30); denominator=sum(weights)
  pairs=[divmod(total*w,denominator) for w in weights]; expected=[q for q,r in pairs]
  for i in sorted(range(len(weights)),key=lambda i:(-pairs[i][1],i))[:total-sum(expected)]: expected[i]+=1
  before=weights.copy(); got=allocate(total,weights)
  valid &= got==expected and sum(got)==total and weights==before
 checks['100_seeded_exact_cases']=valid; record('nexo',version,checks)
 with tempfile.TemporaryDirectory() as tmp:
  directory=Path(tmp); (directory/'test_retry.py').write_text(artifact('vero',version))
  details={}; checks={}
  for name,source in [('gold',gold)]+list(mutants.items()):
   (directory/'retry_policy.py').write_text(source)
   import shutil
   shutil.rmtree(directory/'__pycache__',ignore_errors=True)
   run=subprocess.run([sys.executable,'-B','-m','unittest','test_retry','-v'],cwd=directory,capture_output=True,text=True,timeout=5)
   text=run.stdout+run.stderr
   details[name]={'exit_code':run.returncode,'log':text}
   checks[name]=(run.returncode==0 and 'Ran 6 tests' in text) if name=='gold' else (run.returncode!=0 and 'FAIL:' in text)
  if not checks['gold']: checks={k:False for k in checks}
  record('vero',version,checks); mutation_details[version]=details
luna=json.loads((ROOT/'luna-results.json').read_text())
for version,checks in luna.items(): record('luna',version,checks)
(ROOT/'scores.json').write_text(json.dumps(scores,indent=2)+'\n')
(ROOT/'mutation-results.json').write_text(json.dumps(mutation_details,indent=2)+'\n')
for key,value in scores.items(): print(key,value['passed'], '/',value['total'])
