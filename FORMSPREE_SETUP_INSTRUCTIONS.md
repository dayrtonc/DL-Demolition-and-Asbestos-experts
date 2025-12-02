# Formspree Setup Instructions

## ⚠️ IMPORTANTE: Os formulários do site NÃO estão funcionando!

Os formulários de contato, orçamento e calculadora estão configurados mas **não têm um ID válido do Formspree**. Isso significa que **nenhum lead ou pedido de orçamento está sendo recebido**.

## Como Configurar (5 minutos):

### 1. Criar Conta no Formspree
- Acesse: https://formspree.io
- Clique em "Get Started" ou "Sign Up"
- Crie uma conta gratuita (permite até 50 submissões/mês)

### 2. Criar um Novo Formulário
- No dashboard, clique em "New Form"
- Nome do formulário: "DL Demolition Contact Form"
- Email de destino: `hello@dldemolition.com.au`
- Clique em "Create Form"

### 3. Copiar o Form ID
- Após criar o formulário, você verá um ID como: `xpznabcd`
- Copie esse ID

### 4. Atualizar o Arquivo de Configuração
- Abra o arquivo: `assets/js/formspree-config.js`
- Encontre a linha 15: `contactFormId: 'YOUR_FORM_ID',`
- Substitua `YOUR_FORM_ID` pelo ID que você copiou
- Exemplo: `contactFormId: 'xpznabcd',`

### 5. Atualizar os Outros Formulários (Opcional)
Você pode usar o mesmo ID para todos os formulários ou criar IDs separados:
- Linha 18: `quoteFormId` (formulário de orçamento)
- Linha 21: `calculatorFormId` (calculadora de preços)

### 6. Salvar e Fazer Deploy
- Salve o arquivo
- Faça commit e push para o GitHub
- Aguarde o deploy automático (se configurado)

## Configurações Recomendadas no Formspree:

### Auto-Response (Resposta Automática)
- Ative no dashboard do Formspree
- O template já está configurado no código com:
  - Agradecimento
  - Promessa de resposta em 24h
  - Telefone correto: 07 5699 9693

### Notificações
- Configure para receber email em: `hello@dldemolition.com.au`
- Ative notificações instantâneas

### Spam Protection
- Já está configurado com honeypot no código
- Considere ativar reCAPTCHA no dashboard (opcional)

## Testando

Após configurar:
1. Acesse o site: https://dldemolition.com.au
2. Preencha o formulário de contato
3. Verifique se recebeu o email em `hello@dldemolition.com.au`
4. Verifique se o cliente recebeu a resposta automática

## Plano Gratuito vs Pago

**Gratuito:**
- 50 submissões/mês
- Spam filtering básico
- Email notifications

**Gold ($10/mês):**
- 1000 submissões/mês
- Arquivo de submissões
- Webhooks
- Integrações (Slack, etc.)

Para um negócio como DL Demolition, o plano gratuito deve ser suficiente inicialmente.
