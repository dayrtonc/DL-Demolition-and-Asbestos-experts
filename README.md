# DL Demolition and Asbestos Experts - Official Website

[![Status](https://img.shields.io/badge/status-live-success?style=for-the-badge)](https://www.dldemolition.com.au)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)
[![Tech Stack](https://img.shields.io/badge/tech-HTML,_Tailwind_CSS,_JS-yellowgreen?style=for-the-badge)](https://github.com/dayrtonc/DL-Demolition-and-Asbestos-experts)

Official website for **DL Demolition and Asbestos Experts Pty Ltd** (ABN: 40 693 228 321), a licensed and insured demolition and asbestos removal company based in Southport, QLD. This project is a static, fully responsive, and SEO-optimized website designed to generate leads and establish the company's brand as a trusted, compliant, and professional service provider across Gold Coast, Brisbane, and Sunshine Coast regions.

---

## 📋 Table of Contents

1. [Overview](#-overview)
2. [Live Demo](#-live-demo)
3. [Key Features](#-key-features)
4. [Tech Stack](#-tech-stack)
5. [Project Structure](#-project-structure)
6. [Setup and Local Development](#-setup-and-local-development)
7. [Deployment](#-deployment)
8. [Maintenance Guide](#-maintenance-guide)
9. [SEO & Analytics](#-seo--analytics)
10. [License](#-license)

---

## 🎯 Overview

This repository contains the source code for the official business website of **DL Demolition and Asbestos Experts Pty Ltd**. The site is built with a focus on performance, local SEO, and user experience to effectively convert visitors into qualified leads.

The website prominently features the company's commitment to regulatory compliance in Queensland, including adherence to the **Work Health and Safety Regulation 2011 (QLD)** and the **'How to Safely Remove Asbestos' Code of Practice 2021**. The content strategy is built around establishing expertise and trust through detailed service pages, project showcases, and an extensive blog.

### Business Information

-   **Company Name:** DL Demolition and Asbestos Experts Pty Ltd
-   **ABN:** 40 693 228 321
-   **Location:** Southport QLD 4215, Australia
-   **Phone:** 07 5699 9693 (Local) | +61 7 5699 9693 (International)
-   **Email:** hello@dldemolition.com.au
-   **Business Hours:**
    -   Monday–Friday: 7:30am – 5:00pm
    -   Saturday: 7:30am – 1:00pm
    -   Sunday: Closed

---

## 🌐 Live Demo

The website is live at: **[https://www.dldemolition.com.au](https://www.dldemolition.com.au)**

---

## ✨ Key Features

-   **Professional & Responsive Design:** Mobile-first design built with Tailwind CSS for a seamless experience on all devices.
-   **Progressive Web App (PWA):** The site is installable and provides an offline-ready experience, ensuring accessibility and a native-app feel.
-   **Interactive Price Calculator:** A unique feature allowing potential clients to get instant cost estimates for 8 different services, with modifiers for urgency, access difficulty, and location. Results integrate directly with WhatsApp for a frictionless quote process.
-   **Advanced SEO & Schema Markup:** Comprehensive on-page and technical SEO, including unique meta tags, location-based keywords, and structured data (LocalBusiness, Service, AggregateRating) for rich snippets in search results.
-   **Compliance Focused Content:** All content emphasizes adherence to Queensland's strict regulations for demolition and asbestos removal, building trust and authority.
-   **Lead Generation Forms:** Multiple conversion points, including a quick quote form, a detailed quote request page, and direct WhatsApp integration.
-   **Content-Rich Blog:** Features 11+ articles on safety, regulations, and service guides to drive organic traffic and educate clients.
-   **Accessibility Optimized:** WCAG-compliant with ARIA labels and semantic HTML roles for screen readers.

---

## 🛠️ Tech Stack

-   **Frontend:** HTML5, Tailwind CSS, JavaScript (ES6+)
-   **Build Tool:** No build step required; the project is a pure static site.
-   **PWA:** Service Worker API for offline caching and `manifest.webmanifest` for installability.
-   **Analytics:** Google Analytics 4 (G-4GBXQJ78CT)
-   **SEO Tools:** Google Search Console, Sitemap.xml, Robots.txt
-   **Hosting:** Compatible with any static hosting provider (Netlify, Vercel, GitHub Pages, AWS S3).

---

## 📁 Project Structure

```
/DL-Demolition-and-Asbestos-experts
├── assets/
│   ├── css/                    # Compiled CSS files
│   ├── images/                 # All image assets (logos, projects, icons)
│   └── js/                     # JavaScript files
├── backup/                     # Backup versions of the site (not in production)
├── *.html                      # Main HTML pages (index, about, services, etc.)
├── blog-*.html                 # Individual blog post pages (11 articles)
├── manifest.webmanifest        # PWA configuration file
├── service-worker.js           # Service worker for offline functionality
├── sitemap.xml                 # XML sitemap for search engines
├── robots.txt                  # Crawler instructions
├── README.md                   # This file
└── LICENSE                     # MIT License
```

---

## 🚀 Setup and Local Development

No complex build tools are required to run this project locally. You only need a local web server to serve the static files.

### Prerequisites

-   Python 3 or Node.js installed

### Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dayrtonc/DL-Demolition-and-Asbestos-experts.git
    cd DL-Demolition-and-Asbestos-experts
    ```

2.  **Serve the files:**
    
    **Option A: Python**
    ```bash
    python3 -m http.server 8000
    ```
    
    **Option B: Node.js (live-server)**
    ```bash
    npm install -g live-server
    live-server
    ```

3.  **Open in browser:**
    Navigate to `http://localhost:8000` (or the address provided by your server).

---

## ☁️ Deployment

This is a static website. To deploy, simply upload the contents of the repository to any static hosting provider. **No build process is necessary.**

### Deployment Steps

1.  Choose a hosting provider (Netlify, Vercel, GitHub Pages, AWS S3, etc.).
2.  Connect your Git repository to the provider.
3.  Set the publish directory to the **root** of the repository.
4.  Deploy.

Any changes pushed to the `main` branch will be automatically deployed.

---

## 🔧 Maintenance Guide

This guide simplifies the process of updating and maintaining the website.

### Adding a New Blog Article

1.  **Create a new file:** Duplicate an existing blog file (e.g., `blog-asbestos-removal-guide.html`) and rename it to match your new article (e.g., `blog-new-article-title.html`).
2.  **Edit the content:** Update the title, meta description, content, and images in the new file.
3.  **Update `sitemap.xml`:** Add a new `<url>` entry for your article:
    ```xml
    <url>
      <loc>https://www.dldemolition.com.au/blog-new-article-title.html</loc>
      <lastmod>YYYY-MM-DD</lastmod>
      <changefreq>monthly</changefreq>
      <priority>0.6</priority>
    </url>
    ```
4.  **Update `blog.html`:** Add a new card linking to your article on the main blog page.
5.  **Commit and push** your changes to deploy.

### Updating Contact Information

Contact information (phone, email, address, business hours) appears in multiple files. To update:

1.  **Use Find & Replace** in your code editor to search for the old value and replace it with the new one across all files.
2.  **Key files to check:**
    -   All HTML files (especially `index.html`, `about.html`, `quote.html`, footers)
    -   JSON-LD structured data in `<script type="application/ld+json">` tags
    -   `README.md` (this file)
3.  **Update link attributes:**
    -   Phone links: `href="tel:0756999693"`
    -   Email links: `href="mailto:hello@dldemolition.com.au"`

### Updating the Sitemap

When adding new pages or updating existing ones:

1.  Open `sitemap.xml`
2.  Update the `<lastmod>` date to today's date (format: `YYYY-MM-DD`)
3.  Add new `<url>` entries for any new pages
4.  Commit and push changes
5.  Resubmit the sitemap in Google Search Console

### Optimizing Images

Before uploading new images:

1.  **Compress:** Use [TinyPNG](https://tinypng.com/) or [Squoosh](https://squoosh.app/)
2.  **Convert to WebP:** Use modern formats for better performance
3.  **Use descriptive names:** `asbestos-removal-gold-coast.jpg` instead of `IMG_1234.jpg`
4.  **Add alt text:** Always include descriptive alt attributes for SEO and accessibility

---

## 📊 SEO & Analytics

### Google Analytics 4

-   **Measurement ID:** G-4GBXQJ78CT
-   **Dashboard:** [analytics.google.com](https://analytics.google.com)
-   Tracks all user interactions, traffic sources, and conversion events

### Google Search Console

-   **Property:** https://www.dldemolition.com.au
-   **Dashboard:** [search.google.com/search-console](https://search.google.com/search-console)
-   Monitor search performance, indexing status, and submit sitemaps

### Google Business Profile

-   **Status:** Verified (awaiting final approval)
-   **Location:** Southport QLD 4215
-   Regularly update with posts, photos, and respond to reviews

### SEO Checklist

-   ✅ Sitemap.xml submitted to Google Search Console
-   ✅ Robots.txt configured
-   ✅ All pages have unique meta titles and descriptions
-   ✅ Schema.org structured data implemented
-   ✅ All images have alt text
-   ✅ Mobile-friendly and responsive
-   ✅ HTTPS enabled
-   ✅ Page load speed optimized
-   ✅ WCAG accessibility standards met

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📞 Contact & Support

For technical support or inquiries about this repository:

-   **Email:** hello@dldemolition.com.au
-   **Phone:** 07 5699 9693
-   **GitHub Issues:** [Create an issue](https://github.com/dayrtonc/DL-Demolition-and-Asbestos-experts/issues)

---

**Last Updated:** December 1, 2025  
**Maintained by:** Manus AI & DL Demolition Team
