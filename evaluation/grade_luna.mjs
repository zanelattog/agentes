// npm install --no-save playwright; npx playwright install chromium
// Or set PLAYWRIGHT_MODULE and CHROMIUM_EXECUTABLE to existing installations.
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
const {chromium} = await import(process.env.PLAYWRIGHT_MODULE || 'playwright');
const root=path.dirname(fileURLToPath(import.meta.url));
const browser=await chromium.launch({headless:true,...(process.env.CHROMIUM_EXECUTABLE?{executablePath:process.env.CHROMIUM_EXECUTABLE}:{})});
const results={};
try {
for(const version of ['baseline','candidate']){
 const context=await browser.newContext({viewport:{width:320,height:700}});
 await context.route('**/*',r=>r.abort());
 const page=await context.newPage();
 await page.evaluate(()=>{window.calls=[];window.subscribe=email=>{window.calls.push(email);return new Promise((resolve,reject)=>{window.finish=resolve;window.fail=reject;});};});
 await page.setContent(JSON.parse(fs.readFileSync(path.join(root,`outputs/luna-${version}.json`),'utf8')).response.artifact);
 const checks={};
 checks.label=await page.getByLabel(/Email/).count()===1;
 checks.live_region=await page.locator('#status[role=status][aria-live=polite]').count()===1;
 checks.narrow_screen=await page.evaluate(()=>document.documentElement.scrollWidth<=320);
 await page.keyboard.press('Tab');
 checks.keyboard_focus=await page.locator('#email').evaluate(el=>document.activeElement===el && getComputedStyle(el).outlineStyle!=='none');
 await page.locator('button').click();
 checks.invalid_not_sent=await page.evaluate(()=>window.calls.length===0);
 await page.locator('#email').fill('test@example.test');
 await page.locator('button').click();
 await page.locator('form').dispatchEvent('submit');
 checks.pending_deduplicates=await page.evaluate(()=>window.calls.length===1 && document.querySelector('button').disabled);
 await page.evaluate(()=>window.fail(new Error('synthetic failure')));
 await page.waitForFunction(()=>document.querySelector('#status').textContent.includes('Falha ao inscrever'));
 checks.failure_preserves_retry=await page.evaluate(()=>document.querySelector('#email').value==='test@example.test' && !document.querySelector('button').disabled);
 await page.locator('button').click();
 await page.evaluate(()=>window.finish());
 await page.waitForFunction(()=>document.querySelector('#status').textContent.includes('Inscrição concluída'));
 checks.success_reenables=await page.evaluate(()=>window.calls.length===2 && !document.querySelector('button').disabled);
 checks.no_navigation=page.url()==='about:blank';
 results[version]=checks;
 await context.close();
}
}finally{await browser.close();}
fs.writeFileSync(path.join(root,'luna-results.json'),JSON.stringify(results,null,2)+'\n');
console.log(results);
