# Guia de Configuração: Google reCAPTCHA v3

## Por que reCAPTCHA v3?

O reCAPTCHA v3 é **invisível** para usuários legítimos. Ele analisa o comportamento do visitante em segundo plano e atribui uma pontuação de 0 a 1. Você só recebe formulários de usuários com pontuação alta (humanos reais).

---

## Passo 1: Criar Chaves do reCAPTCHA

1. Acesse: https://www.google.com/recaptcha/admin/create
2. Faça login com sua conta Google
3. Preencha o formulário:
   - **Label:** DL Demolition Website
   - **reCAPTCHA type:** reCAPTCHA v3
   - **Domains:** 
     - `dldemolition.com.au`
     - `www.dldemolition.com.au`
   - Aceite os termos
4. Clique em **Submit**
5. **Copie as duas chaves:**
   - **Site Key** (começa com `6L...`)
   - **Secret Key** (começa com `6L...` também)

---

## Passo 2: Configurar no Formspree

1. Acesse: https://formspree.io/forms
2. Faça login na sua conta
3. Clique no formulário `mldqnnyp`
4. Vá em **Settings** → **Spam Protection**
5. Ative **Google reCAPTCHA v3**
6. Cole a **Secret Key** que você copiou
7. Salve as configurações

---

## Passo 3: Adicionar ao Site

Eu já preparei o código! Você só precisa me enviar a **Site Key** e eu atualizo automaticamente.

Ou, se preferir fazer manualmente:

1. Abra o arquivo `assets/js/formspree-config.js`
2. Encontre a linha 59:
   ```javascript
   siteKey: 'YOUR_RECAPTCHA_SITE_KEY'
   ```
3. Substitua `YOUR_RECAPTCHA_SITE_KEY` pela sua **Site Key**
4. Mude a linha 58 de `enabled: false` para `enabled: true`
5. Salve o arquivo

---

## Passo 4: Testar

1. Acesse o site e preencha um formulário
2. Você não verá nenhum CAPTCHA, mas o reCAPTCHA estará funcionando
3. Verifique no painel do Formspree se o formulário foi recebido
4. No painel do reCAPTCHA (https://www.google.com/recaptcha/admin), você verá as estatísticas

---

## ✅ Resultado

- **99% menos spam** nos formulários
- **Invisível** para usuários legítimos
- **Proteção automática** contra bots

**Me envie a Site Key quando estiver pronta e eu configuro tudo!**
