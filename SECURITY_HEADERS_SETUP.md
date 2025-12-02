# Security Headers Setup Instructions

## O que são Security Headers?

Security headers são cabeçalhos HTTP que protegem o site contra ataques comuns como:
- **XSS (Cross-Site Scripting):** Injeção de scripts maliciosos
- **Clickjacking:** Enganar usuários a clicar em elementos invisíveis
- **MIME Sniffing:** Execução de arquivos maliciosos
- **Data Injection:** Injeção de dados não autorizados

## Arquivos Criados

Foram criados **2 arquivos de configuração** para diferentes tipos de hospedagem:

### 1. `_headers` (Para Netlify, Cloudflare Pages, Vercel)
- Usado automaticamente por plataformas modernas de hospedagem
- Nenhuma configuração adicional necessária
- Já está pronto para uso

### 2. `.htaccess` (Para Apache/cPanel/Shared Hosting)
- Usado em servidores Apache tradicionais
- Inclui redirecionamento HTTPS automático
- Compressão e cache configurados

## Como Aplicar (Depende da sua Hospedagem)

### Se você usa **Netlify, Cloudflare Pages ou Vercel:**
✅ **Não precisa fazer nada!** O arquivo `_headers` será aplicado automaticamente no próximo deploy.

### Se você usa **cPanel, Hostinger, GoDaddy ou outro shared hosting:**
1. Faça upload do arquivo `.htaccess` para a pasta raiz do site
2. Certifique-se de que o arquivo está na mesma pasta que `index.html`
3. O servidor Apache aplicará as configurações automaticamente

### Se você usa **Nginx:**
Você precisará adicionar os headers manualmente no arquivo de configuração do Nginx. Exemplo:

```nginx
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://cdn.tailwindcss.com...";
add_header X-Frame-Options "DENY";
add_header X-Content-Type-Options "nosniff";
add_header X-XSS-Protection "1; mode=block";
add_header Referrer-Policy "strict-origin-when-cross-origin";
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
```

## Testando os Headers

Após o deploy, teste se os headers estão funcionando:

1. Acesse: https://securityheaders.com
2. Digite: `dldemolition.com.au`
3. Clique em "Scan"

**Resultado esperado:** Grade **A** ou **A+**

## Headers Implementados

| Header | Função | Proteção |
|--------|--------|----------|
| Content-Security-Policy | Define fontes permitidas de conteúdo | XSS, Injection |
| X-Frame-Options | Impede que o site seja carregado em iframe | Clickjacking |
| X-Content-Type-Options | Impede MIME sniffing | Execução de malware |
| X-XSS-Protection | Ativa proteção XSS do navegador | XSS |
| Referrer-Policy | Controla informações enviadas a outros sites | Privacy |
| Strict-Transport-Security | Força HTTPS | Man-in-the-middle |
| Permissions-Policy | Desabilita APIs não usadas | Privacy |

## Troubleshooting

### Se algo parar de funcionar após aplicar os headers:

1. **Google Analytics não funciona?**
   - Verifique se `https://www.google-analytics.com` está no CSP
   
2. **Formspree não funciona?**
   - Verifique se `https://formspree.io` está no CSP
   
3. **Tailwind CSS não carrega?**
   - Verifique se `https://cdn.tailwindcss.com` está no CSP

4. **Font Awesome não aparece?**
   - Verifique se `https://cdnjs.cloudflare.com` está no CSP

## Benefícios

✅ Proteção contra ataques comuns  
✅ Melhor pontuação em auditorias de segurança  
✅ Maior confiança dos clientes  
✅ Melhor ranking no Google (segurança é fator de SEO)  
✅ Conformidade com melhores práticas de segurança web
