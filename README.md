# DL Demolition and Asbestos Experts - Official Website

[![Status](https://img.shields.io/badge/status-live-success?style=for-the-badge)](https://www.dldemolition.com.au)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)
[![Tech Stack](https://img.shields.io/badge/tech-HTML,_Tailwind_CSS,_JS-yellowgreen?style=for-the-badge)](https://github.com/dayrtonc/DL-Demolition-and-Asbestos-experts)

Official website for DL Demolition and Asbestos Experts Pty Ltd, a licensed and insured demolition and asbestos removal company based in Southport, QLD. The project is a static, fully responsive, and SEO-optimized website designed to generate leads and establish the company's brand as a trusted, compliant, and professional service provider in the Gold Coast, Brisbane, and Sunshine Coast regions.

---

## 📋 Table of Contents

1. [Overview](#-overview)
2. [Live Demo](#-live-demo)
3. [Key Features](#-key-features)
4. [Tech Stack](#-tech-stack)
5. [Project Structure](#-project-structure)
6. [Setup and Local Development](#-setup-and-local-development)
7. [Deployment](#-deployment)
8. [License](#-license)

---

## 🎯 Overview

This repository contains the source code for the official business website of **DL Demolition and Asbestos Experts Pty Ltd**. The site is built with a focus on performance, local SEO, and user experience to effectively convert visitors into qualified leads.

It prominently features the company's commitment to regulatory compliance in Queensland, including adherence to the **Work Health and Safety Regulation 2011 (QLD)** and the **'How to Safely Remove Asbestos' Code of Practice 2021**. The content strategy is built around establishing expertise and trust through detailed service pages, project showcases, and an extensive blog.

## 🌐 Live Demo

The website is live at:
**[https://www.dldemolition.com.au](https://www.dldemolition.com.au)**

## ✨ Key Features

- **Professional & Responsive Design:** Mobile-first design built with Tailwind CSS for a seamless experience on all devices.
- **Progressive Web App (PWA):** The site is installable and provides an offline-ready experience, ensuring accessibility and a native-app feel.
- **Interactive Price Calculator:** A unique feature allowing potential clients to get instant cost estimates for 8 different services, with modifiers for urgency, access difficulty, and location. The results integrate directly with WhatsApp for a frictionless quote process.
- **Advanced SEO & Schema Markup:** Comprehensive on-page and technical SEO, including unique meta tags, location-based keywords, and structured data (LocalBusiness, Service, AggregateRating) for rich snippets in search results.
- **Compliance Focused Content:** All content emphasizes adherence to Queensland's strict regulations for demolition and asbestos removal, building trust and authority.
- **Lead Generation Forms:** Multiple conversion points, including a quick quote form, a detailed quote request page, and direct WhatsApp integration.
- **Content-Rich Blog:** Features 11+ articles on safety, regulations, and service guides to drive organic traffic and educate clients.

## 🛠️ Tech Stack

- **Frontend:** HTML5, Tailwind CSS, JavaScript (ES6+)
- **Build Tool:** No build step required; the project is a pure static site.
- **PWA:** Service Worker API for offline caching and `manifest.webmanifest` for installability.
- **Hosting:** Can be deployed on any static hosting provider (e.g., Netlify, Vercel, GitHub Pages).

## 📁 Project Structure

The project follows a straightforward structure for a static website:

```
/home/ubuntu/DL-Demolition-and-Asbestos-experts
├── assets/
│   ├── css/         # Compiled CSS (if any)
│   ├── images/      # All image assets
│   └── js/          # JavaScript files
├── backup/          # Backup versions of the site
├── *.html           # All main HTML pages (index, about, services, etc.)
├── blog-*.html      # Individual blog post pages
├── manifest.webmanifest # PWA configuration file
├── sitemap.xml      # Sitemap for SEO
├── robots.txt       # Instructions for web crawlers
└── README.md        # This file
```

## 🚀 Setup and Local Development

No complex build tools are required to run this project locally. You only need a local web server to serve the static files.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/dayrtonc/DL-Demolition-and-Asbestos-experts.git
    cd DL-Demolition-and-Asbestos-experts
    ```

2.  **Serve the files:**
    You can use any simple local web server. If you have Python installed, you can run:
    ```sh
    # For Python 3
    python3 -m http.server 8000
    ```
    Or with Node.js, you can use `live-server`:
    ```sh
    # Install live-server globally if you haven't already
    npm install -g live-server

    # Run the server
    live-server
    ```

3.  **Open in browser:**
    Navigate to `http://localhost:8000` (or the address provided by your server).

## ☁️ Deployment

This is a static website. To deploy, simply upload the contents of the repository to any static hosting provider. No build process is necessary.

1.  Choose a hosting provider (Netlify, Vercel, GitHub Pages, AWS S3, etc.).
2.  Connect your Git repository to the provider.
3.  Set the publish directory to the root of the repository.
4.  Deploy.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
