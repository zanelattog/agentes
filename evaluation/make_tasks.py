"""Synthetic tasks frozen before collecting comparative responses."""
from pathlib import Path
import json

tasks = {
  'atlas': '''Planeje a ingestão de webhooks de pagamentos para um SaaS com múltiplos tenants.
Temos uma aplicação monolítica, PostgreSQL e um processo worker já disponível. Não podemos adicionar serviços.
O provedor repete eventos e exige resposta em até 2 segundos. Event IDs só são únicos dentro de cada tenant.
O recebimento deve sobreviver a um crash imediatamente após responder HTTP. O worker envia uma notificação a uma
API externa que aceita chave de idempotência. Dois workers podem executar simultaneamente.
Precisamos continuar aceitando eventos se o processamento de negócio ficar indisponível.
Em artifact, retorne um objeto JSON com suas decisões, usando exatamente estas opções:
ack_when: before_persist | after_durable_commit | after_external_delivery
dedup_key: event_id | tenant_and_event_id | timestamp
persistence: memory_queue | database_inbox_transaction | log_file
worker_claim: unguarded_select | atomic_claim_or_lock | in_memory_flag
external_delivery: stable_idempotency_key | random_key_per_retry | no_retry
new_services: none | kafka | redis
retry_policy: bounded_backoff_with_failure_tracking | infinite_hot_loop | discard_on_error
rollback: preserve_inbox_and_compatible_schema | drop_inbox | delete_failed_events
Em answer, explique brevemente suas decisões e uma limitação da garantia de entrega.
Não implemente código nem afirme que executou testes.''',
  'luna': '''Implemente um formulário de inscrição em um único HTML autocontido, sem dependências externas.
Contrato: o input type=email tem id=email, name=email e um label associado. Existe um botão de envio com
texto Inscrever. O elemento id=status tem role=status e aria-live=polite. No submit válido, chame
window.subscribe(email), uma Promise fornecida pelo host. Não implemente nem substitua essa função.
Enquanto aguarda, desabilite o botão e impeça chamadas duplicadas. Se resolver, mostre Inscrição concluída.
Se rejeitar, mostre Falha ao inscrever, preserve o email e permita nova tentativa. Reabilite o botão nos
dois resultados. Não recarregue a página. O formulário deve caber em uma tela de 320px sem rolagem horizontal.
Use HTML semântico, teclado e foco visível. Retorne o HTML completo em artifact, sem cercas Markdown.
Em answer, diga o que implementou sem afirmar ter aberto um navegador.''',
  'nexo': '''Implemente em Python 3.9 a função pura allocate(total, weights) que distribui centavos inteiros.
total deve ser int não negativo (bool é inválido). weights deve ser uma lista não vazia de ints não negativos
(bool é inválido), com pelo menos um peso positivo. Tipo inválido gera TypeError; valor inválido gera ValueError.
Distribua usando as cotas proporcionais: tome o piso de cada cota e entregue os centavos restantes às maiores
partes fracionárias; em empate, o menor índice recebe primeiro. A soma deve ser exatamente total. Um peso zero
nunca recebe centavos. Não altere a lista de entrada. Deve lidar com total=10**30 sem iterar por centavo e sem
perder precisão por float. Retorne apenas o código Python em artifact, sem cercas Markdown. Não use IO/rede.
Em answer, explique a complexidade e não afirme ter executado testes.''',
  'iris': '''Revise estas alegações sobre código Python. O contrato diz que cada chamada de add_item sem lista
explícita deve ser independente; average([]) deve retornar None; charge deve debitar saldo compartilhado
corretamente com chamadas concorrentes. O DB-API usado aceita placeholders ? corretamente.

def add_item(value, items=[]):
    items.append(value)
    return items
def average(values):
    return sum(values) / len(values)
def lookup(db, user_id):
    return db.execute("SELECT id FROM users WHERE id = ?", (user_id,)).fetchone()
async def charge(account, amount):
    old = account.balance
    await account.audit(amount)
    account.balance = old - amount
def double(x):
    return x * 2

Alegações:
R1: add_item compartilha estado entre chamadas sem lista explícita.
R2: average viola o contrato para lista vazia.
R3: lookup tem SQL injection porque recebe user_id do usuário.
R4: charge pode perder um débito com concorrência.
R5: double tem bug porque o nome x é curto.
R6: account.audit pode expor credenciais; há vulnerabilidade comprovada apenas pelo trecho acima.
Em artifact, retorne JSON com R1..R6 booleanos: true somente para defeito sustentado pelo contrato e código.
Em answer, explique um cenário para cada defeito confirmado e por que rejeita as outras alegações.
Não altere código nem diga ter executado testes.''',
  'cora': '''Faça triagem de segurança deste endpoint fictício. O usuário está autenticado. O ambiente é Linux.
get_invoice procura exclusivamente pelo id e retorna invoice.tenant_id; o código abaixo é o endpoint completo.
Não há checagem de tenant em middleware. filename é uma string diretamente controlada pelo cliente.
uploads contém dados de vários clientes; o processo pode ler /etc/passwd. session_token é credencial secreta.
DB-API usa placeholders ? com binding correto. html.escape é o escaping padrão para conteúdo textual HTML.

def download(request, db):
    invoice = get_invoice(request.query['invoice_id'])
    logger.info('session=%s', request.session_token)
    label = html.escape(request.query['label'])
    owner = db.execute('SELECT name FROM users WHERE id = ?', (request.user.id,)).fetchone()
    path = os.path.join('/srv/uploads', request.query['filename'])
    return Response(open(path, 'rb').read(), headers={'X-Invoice': str(invoice.id)})

Alegações:
S1: Há acesso a objetos de outro tenant pela falta de autorização por invoice.
S2: Um caminho absoluto em filename pode escapar de /srv/uploads.
S3: O log pode expor a credencial session_token.
S4: A consulta owner permite SQL injection pelo id, apesar do binding descrito.
S5: html.escape por si só prova uma vulnerabilidade XSS neste trecho.
S6: O trecho prova conformidade com a LGPD porque o usuário está autenticado.
Em artifact, retorne JSON com S1..S6 booleanos, true somente para alegação correta sustentada pelo contexto.
Em answer, indique pré-condição, impacto e correção dos riscos confirmados. Não execute ataques nem scans.''',
  'vero': '''Escreva testes unittest para a função retry_delay(attempt, base, cap), importada de retry_policy.
Contrato: os três argumentos são ints, bool não é aceito. Tipo inválido gera TypeError. Valores negativos
geram ValueError. O retorno é min(cap, base * 2**attempt), inteiro; attempt começa em zero. base=0 ou cap=0
retorna zero. Valores grandes de attempt (ex.: 10000) devem retornar o cap sem overflow ou espera longa.
Use apenas unittest e retry_policy, sem arquivos, rede, subprocessos ou aleatoriedade. Os testes devem passar
em uma implementação correta e detectar erros de limite, validação e cálculo. Não reimplemente a função para
calcular o esperado: use exemplos e propriedades independentes. Retorne o módulo Python em artifact, sem cercas.
Em answer, explique o que os testes cobrem; não afirme que foram executados.'''
}
common = '''\nEsta é uma avaliação controlada de resposta única. Não use ferramentas, não leia arquivos e não delegue.
Todo o contexto necessário está acima. Responda no JSON solicitado. artifact contém o artefato pedido como string;
answer é uma explicação curta; limitations registra o que não foi validado. Não inclua dados de outros projetos.'''
out = {name: {'prompt': prompt + common} for name,prompt in tasks.items()}
Path(__file__).with_name('tasks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
schema={'type':'object','properties':{k:{'type':'string'} for k in ['answer','artifact','limitations']},'required':['answer','artifact','limitations'],'additionalProperties':False}
Path(__file__).with_name('response.schema.json').write_text(json.dumps(schema,indent=2))
