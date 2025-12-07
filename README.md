# DL Demolition and Asbestos Experts - Website Oficial

![Logo da DL Demolition](https://www.dldemolition.com.au/assets/images/logo_header_optimized.png)

[![Status do Site](https://img.shields.io/website?down_message=offline&label=dldemolition.com.au&style=for-the-badge&up_message=online&url=https%3A%2F%2Fwww.dldemolition.com.au)](https://www.dldemolition.com.au) [![Licença](https://img.shields.io/github/license/dayrtonc/DL-Demolition-and-Asbestos-experts?style=for-the-badge)](LICENSE) [![Tech Stack](https://img.shields.io/badge/tech-HTML_&_Tailwind_CSS-blue?style=for-the-badge)](https://tailwindcss.com/)

---

Este repositório contém o código-fonte do site oficial da **DL Demolition and Asbestos Experts Pty Ltd**, uma empresa licenciada e segurada de demolição e remoção de amianto com sede em Southport, QLD, Austrália. O projeto é um site estático, totalmente responsivo e otimizado para SEO, projetado para gerar leads qualificados e estabelecer a marca da empresa como um provedor de serviços confiável, em conformidade com as regulamentações e profissional nas regiões de Gold Coast, Brisbane e Sunshine Coast.

## 📋 Índice

1. [Visão Geral](#-visão-geral)
2. [Demonstração ao Vivo](#-demonstração-ao-vivo)
3. [Principais Funcionalidades](#-principais-funcionalidades)
4. [Tecnologias Utilizadas](#-tecnologias-utilizadas)
5. [Estrutura do Projeto](#-estrutura-do-projeto)
6. [Configuração e Desenvolvimento Local](#-configuração-e-desenvolvimento-local)
7. [Implantação (Deploy)](#-implantação-deploy)
8. [Guia de Manutenção](#-guia-de-manutenção)
9. [SEO e Analytics](#-seo-e-analytics)
10. [Licença](#-licença)

---

## 🎯 Visão Geral

O site serve como a principal presença digital da **DL Demolition and Asbestos Experts Pty Ltd** (ABN: 40 693 228 321). Foi construído com foco em **performance**, **SEO local** e **experiência do usuário** para converter visitantes em clientes de forma eficaz.

Um pilar central do projeto é a ênfase na conformidade com as rigorosas regulamentações de Queensland, incluindo a **Work Health and Safety Regulation 2011 (QLD)** e o **'How to Safely Remove Asbestos' Code of Practice 2021**. A estratégia de conteúdo visa estabelecer autoridade e confiança através de páginas de serviços detalhadas, um portfólio de projetos e um blog informativo.

### Informações da Empresa

- **Nome da Empresa:** DL Demolition and Asbestos Experts Pty Ltd
- **ABN:** 40 693 228 321
- **Endereço:** Southport QLD 4215, Austrália
- **Telefone:** [07 5699 9693](tel:0756999693)
- **Email:** [hello@dldemolition.com.au](mailto:hello@dldemolition.com.au)

---

## 🌐 Demonstração ao Vivo

O site está no ar e pode ser acessado em:

### **[https://www.dldemolition.com.au](https://www.dldemolition.com.au)**

---

## ✨ Principais Funcionalidades

- 📱 **Design Profissional e Responsivo:** Construído com uma abordagem *mobile-first* usando Tailwind CSS para uma experiência perfeita em todos os dispositivos.
- 🚀 **Progressive Web App (PWA):** O site é instalável e oferece uma experiência offline, garantindo acessibilidade e uma sensação de aplicativo nativo.
- 🧮 **Calculadora de Preços Interativa:** Uma funcionalidade exclusiva que permite aos clientes obter estimativas de custo instantâneas para 8 serviços diferentes, com modificadores para urgência, dificuldade de acesso e localização. Os resultados integram-se diretamente com o WhatsApp para um processo de cotação sem atritos.
- 📈 **SEO Avançado e Schema Markup:** SEO técnico e de página abrangente, incluindo meta tags exclusivas, palavras-chave baseadas em localização e dados estruturados (LocalBusiness, Service, AggregateRating) para rich snippets nos resultados de busca.
- 🛡️ **Conteúdo Focado em Conformidade:** Todo o conteúdo enfatiza a adesão às regulamentações de Queensland para demolição e remoção de amianto, construindo confiança e autoridade.
- ✉️ **Geração de Leads:** Múltiplos pontos de conversão, incluindo um formulário de cotação rápida, uma página de solicitação de cotação detalhada e integração direta com o WhatsApp.
- ✍️ **Blog Rico em Conteúdo:** Mais de 11 artigos sobre segurança, regulamentações e guias de serviço para impulsionar o tráfego orgânico e educar os clientes.
- ♿ **Acessibilidade Otimizada:** Em conformidade com as diretrizes WCAG, utilizando atributos ARIA e HTML semântico para leitores de tela.

---

## 🛠️ Tecnologias Utilizadas

| Categoria | Tecnologia |
| :--- | :--- |
| **Frontend** | HTML5, Tailwind CSS, JavaScript (ES6+) |
| **PWA** | Service Worker API, `manifest.webmanifest` |
| **Analytics** | Google Analytics 4 (G-4GBXQJ78CT) |
| **SEO** | `sitemap.xml`, `robots.txt`, Schema.org JSON-LD |
| **Hospedagem** | GitHub Pages (compatível com qualquer host estático) |
| **Dev Server** | Python 3 `http.server`, Node.js `live-server` |

---

## 📁 Estrutura do Projeto

```
/DL-Demolition-and-Asbestos-experts
├── assets/
│   ├── css/                    # Arquivos CSS (atualmente não compilados)
│   ├── images/                 # Todos os ativos de imagem (logos, projetos, ícones)
│   └── js/                     # Scripts JavaScript
├── *.html                      # Páginas HTML principais (index, about, services, etc.)
├── blog-*.html                 # Páginas de artigos de blog individuais
├── manifest.webmanifest        # Arquivo de configuração do PWA
├── service-worker.js           # Service worker para funcionalidade offline
├── sitemap.xml                 # Sitemap XML para motores de busca
├── robots.txt                  # Instruções para crawlers
├── README.md                   # Este arquivo
└── LICENSE                     # Licença do projeto
```

---

## 🚀 Configuração e Desenvolvimento Local

Nenhuma ferramenta de build complexa é necessária para executar este projeto localmente. Você só precisa de um servidor web local para servir os arquivos estáticos.

### Pré-requisitos

- [Python 3](https://www.python.org/downloads/) ou [Node.js](https://nodejs.org/) instalado.

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/dayrtonc/DL-Demolition-and-Asbestos-experts.git
    cd DL-Demolition-and-Asbestos-experts
    ```

2.  **Inicie um servidor local:**

    **Opção A: Com Python**
    ```bash
    python3 -m http.server 8000
    ```

    **Opção B: Com Node.js (usando `live-server`)**
    ```bash
    npm install -g live-server
    live-server
    ```

3.  **Abra no navegador:**
    Navegue para `http://localhost:8000` (ou o endereço fornecido pelo seu servidor).

---

## ☁️ Implantação (Deploy)

Este é um site estático. Para implantar, basta fazer o upload do conteúdo do repositório para qualquer provedor de hospedagem estática. **Nenhum processo de build é necessário.**

### Passos para Deploy

1.  Escolha um provedor de hospedagem (Netlify, Vercel, GitHub Pages, AWS S3, etc.).
2.  Conecte seu repositório Git ao provedor.
3.  Defina o diretório de publicação como a **raiz** do repositório.
4.  Implante.

Qualquer alteração enviada para a branch `main` será automaticamente implantada se a integração contínua estiver configurada.

---

## 🔧 Guia de Manutenção

Este guia simplifica o processo de atualização e manutenção do site.

### Adicionando um Novo Artigo de Blog

1.  **Crie um novo arquivo:** Duplique um arquivo de blog existente (ex: `blog-asbestos-removal-guide.html`) e renomeie-o para corresponder ao novo título (ex: `blog-novo-titulo.html`).
2.  **Edite o conteúdo:** Atualize o título, meta description, conteúdo e imagens no novo arquivo.
3.  **Atualize o `sitemap.xml`:** Adicione uma nova entrada `<url>` para o seu artigo:
    ```xml
    <url>
      <loc>https://www.dldemolition.com.au/blog-novo-titulo.html</loc>
      <lastmod>YYYY-MM-DD</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.6</priority>
    </url>
    ```
4.  **Atualize o `blog.html`:** Adicione um novo card na página principal do blog com o link para o seu novo artigo.
5.  **Faça commit e push** das suas alterações para implantar.

### Atualizando Informações de Contato

As informações de contato (telefone, email, endereço) aparecem em vários arquivos. Para atualizar:

1.  **Use a função "Localizar e Substituir"** no seu editor de código para procurar o valor antigo e substituí-lo pelo novo em todos os arquivos.
2.  **Arquivos-chave para verificar:**
    -   Todos os arquivos `.html` (especialmente `index.html`, `about.html`, `quote.html` e rodapés).
    -   Dados estruturados JSON-LD nas tags `<script type="application/ld+json">`.
    -   `README.md` (este arquivo).

### Otimizando Imagens

Antes de fazer upload de novas imagens:

1.  **Comprima:** Use ferramentas como [TinyPNG](https://tinypng.com/) ou [Squoosh](https://squoosh.app/).
2.  **Converta para WebP:** Use formatos modernos para melhor performance.
3.  **Use nomes descritivos:** `remocao-amianto-gold-coast.jpg` em vez de `IMG_1234.jpg`.
4.  **Adicione texto alternativo (alt text):** Sempre inclua atributos `alt` descritivos para SEO e acessibilidade.

---

## 📊 SEO e Analytics

### Google Analytics 4

-   **ID de Medição:** `G-4GBXQJ78CT`
-   **Painel:** [analytics.google.com](https://analytics.google.com)
-   Rastreia todas as interações do usuário, fontes de tráfego e eventos de conversão.

### Google Search Console

-   **Propriedade:** `https://www.dldemolition.com.au`
-   **Painel:** [search.google.com/search-console](https://search.google.com/search-console)
-   Monitora o desempenho da pesquisa, o status da indexação e permite o envio de sitemaps.

### Checklist de SEO

-   [x] `sitemap.xml` enviado ao Google Search Console.
-   [x] `robots.txt` configurado.
-   [x] Todas as páginas possuem meta títulos e descrições únicos.
-   [x] Dados estruturados Schema.org implementados.
-   [x] Todas as imagens possuem texto alternativo.
-   [x] Design responsivo e amigável para dispositivos móveis.
-   [x] HTTPS ativado.
-   [x] Velocidade de carregamento da página otimizada.
-   [x] Padrões de acessibilidade WCAG atendidos.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

*Este README foi gerado e mantido pela Manus AI e pela equipe da DL Demolition.*
*Última atualização: 6 de dezembro de 2024*
