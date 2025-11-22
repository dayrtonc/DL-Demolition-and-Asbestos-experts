# DL Demolition Asbestos & Demolition Website

Professional website for asbestos removal and demolition services across Gold Coast to Sunshine Coast, Queensland, Australia.

## 🚀 Features

- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **PWA Ready**: Progressive Web App with offline functionality and app installation
- **SEO Optimized**: Advanced SEO techniques with Schema.org markup for maximum visibility
- **Conversion Focused**: Multiple optimization strategies for lead generation
- **Performance Optimized**: Fast loading with Lighthouse score target ≥90
- **Mobile First**: iOS and Android specific optimizations

## 📁 Project Structure

```
DL-Demolition-and-Asbestos-experts/
├── assets/
│   ├── css/
│   │   └── mobile-styles.css          # Mobile-specific optimizations
│   ├── js/
│   │   ├── form-validation.js         # Form validation & submission
│   │   ├── formspree-config.js        # Formspree integration config
│   │   └── pwa-install.js             # PWA installation handler
│   ├── images/                         # All images and icons (to be added)
│   └── fonts/                          # Custom fonts (if any)
├── templates/
│   └── create_pages.py                 # Python script for page generation
├── backup/
│   ├── index_improved.html             # Alternative homepage version
│   └── index_with_calculator.html      # Homepage with integrated calculator
├── docs/                               # Documentation files
├── *.html                              # Main website pages
├── service-worker.js                   # PWA service worker
├── manifest.webmanifest                # PWA manifest
├── robots.txt                          # SEO robots file
├── sitemap.xml                         # SEO sitemap
└── README.md                           # This file
```

## 📄 Main Pages

1. **index.html** - Homepage with hero section and quick quote form (OFFICIAL)
2. **services.html** - Detailed service descriptions and pricing
3. **calculator.html** - Interactive price calculator with multiple service selection
4. **about.html** - Company information, certifications, and team
5. **reviews.html** - Customer testimonials and ratings
6. **blog.html** - Industry news, tips, and company updates
7. **quote.html** - Comprehensive quote request form
8. **offline.html** - Offline page for PWA functionality

## 🎯 Key Features

### Conversion Optimization
- Exit-intent popups
- Scroll-based triggers
- Time-based offers
- Social proof notifications
- Urgency elements
- A/B testing ready
- Multiple CTAs strategically placed

### Mobile Optimization
- iOS Safari specific fixes
- Android Chrome optimizations
- Touch-friendly interface (44px minimum touch targets)
- Sticky action bars
- Floating WhatsApp button
- PWA installation prompts
- Responsive images with lazy loading

### SEO Features
- Structured data (Schema.org LocalBusiness)
- Local business optimization
- Meta tag optimization
- Image optimization
- Internal linking
- Breadcrumb navigation
- Sitemap with image references
- Open Graph tags for social sharing

### Performance
- Lazy loading images
- Critical CSS inlining
- JavaScript optimization
- Font optimization
- Service Worker caching strategies
- Offline-first approach

## 📞 Contact Information

- **Phone**: +61 451 612 742
- **Email**: hello@dldemolition.com.au
- **Domain**: www.breathesafe.com.au
- **Service Areas**: Gold Coast, Sunshine Coast, Brisbane
- **Emergency**: 24/7 availability

## 🛠️ Technical Details

### Dependencies
- **TailwindCSS** (via CDN) - Utility-first CSS framework
- **Font Awesome 7.0.1** - Icon library
- **Google Fonts (Inter)** - Typography
- **Vanilla JavaScript** - No heavy frameworks, optimal performance

### Browser Support
- Chrome 80+
- Safari 13+
- Firefox 75+
- Edge 80+
- iOS Safari 13+
- Android Chrome 80+

### Performance Targets
- Lighthouse Performance: ≥90
- First Contentful Paint: <2s
- Largest Contentful Paint: <2.5s
- Cumulative Layout Shift: <0.1
- Time to Interactive: <3.5s

## 🚀 Deployment

### Prerequisites
1. Web server with HTTPS support
2. Domain: breathesafe.com.au
3. Formspree account for form handling
4. (Optional) Google Analytics for tracking
5. (Optional) Facebook Pixel for ads

### Installation Steps

1. **Upload files to web server**
   ```bash
   # Upload all files to server root directory
   rsync -avz --exclude '.git' ./ user@server:/var/www/html/
   ```

2. **Configure SSL certificate**
   ```bash
   # Using Let's Encrypt (recommended)
   sudo certbot --nginx -d breathesafe.com.au -d www.breathesafe.com.au
   ```

3. **Setup Formspree**
   - Create account at https://formspree.io
   - Create new form for your website
   - Copy form ID
   - Update `assets/js/formspree-config.js` with your form ID
   - Replace `YOUR_FORM_ID` with actual ID

4. **Add images**
   - Upload all images to `assets/images/` directory
   - Ensure proper naming as referenced in HTML files
   - Optimize images for web (WebP format recommended)

5. **Configure analytics** (Optional)
   - Add Google Analytics tracking code to all HTML files
   - Add Facebook Pixel code if running ads
   - Configure conversion tracking

6. **Submit sitemap to Google Search Console**
   - Verify domain ownership
   - Submit sitemap.xml
   - Monitor indexing status

### PWA Setup

1. **Ensure HTTPS is enabled** (required for PWA)
2. **Verify manifest.webmanifest is accessible**
   ```
   https://breathesafe.com.au/manifest.webmanifest
   ```
3. **Test service worker functionality**
   - Open DevTools → Application → Service Workers
   - Verify service worker is registered
4. **Validate PWA criteria with Lighthouse**
   - Run Lighthouse audit in Chrome DevTools
   - Ensure PWA score is 100

## 📊 Analytics & Tracking

### Conversion Events to Track
- Phone clicks (`tel:` links)
- WhatsApp clicks
- Form submissions
- Calculator usage
- Quote requests
- Page views
- Time on site
- Bounce rate

### Performance Monitoring
- Page load times
- Core Web Vitals
- Error tracking
- User engagement metrics
- Mobile vs Desktop usage
- Geographic distribution

## 🔧 Maintenance

### Regular Tasks
- [ ] Update content and pricing monthly
- [ ] Monitor performance metrics weekly
- [ ] Check for broken links monthly
- [ ] Update testimonials as received
- [ ] Refresh project gallery quarterly
- [ ] Review and respond to form submissions daily
- [ ] Update blog content weekly

### Security
- [ ] Keep dependencies updated
- [ ] Monitor for vulnerabilities
- [ ] Regular backups (daily recommended)
- [ ] SSL certificate renewal (auto with Let's Encrypt)
- [ ] Review form spam protection
- [ ] Monitor server logs for suspicious activity

## 📈 Expected Results

### Conversion Metrics (Projected)
- +60% leads qualified via PWA
- +40% engagement on mobile
- +35% time on site
- +70% value per project
- 24-hour quote response time

### SEO Metrics (Projected)
- +50% ranking improvement for local keywords
- +40% organic traffic within 6 months
- +30% click-through rate
- +25% domain authority
- Top 3 ranking for "asbestos removal Gold Coast"

## 🔄 Version History

### v1.0.0 (Current)
- ✅ Initial website structure
- ✅ 8 main pages implemented
- ✅ PWA functionality complete
- ✅ Mobile optimizations
- ✅ SEO implementation
- ✅ Form validation
- ✅ Service Worker caching
- ✅ Organized file structure

### Planned Updates (v1.1.0)
- [ ] Add project gallery with before/after photos
- [ ] Implement blog CMS integration
- [ ] Add live chat widget
- [ ] Implement A/B testing framework
- [ ] Add customer portal for project tracking
- [ ] Integrate online booking system

## 🤝 Contributing

This is a private project for DL Demolition. For suggestions or issues, please contact the development team.

## 📝 Setup Instructions for Developers

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/dayrtonc/DL-Demolition-and-Asbestos-experts.git
   cd DL-Demolition-and-Asbestos-experts
   ```

2. **Start local server**
   ```bash
   # Using Python
   python3 -m http.server 8000
   
   # Or using Node.js
   npx http-server -p 8000
   ```

3. **Open in browser**
   ```
   http://localhost:8000
   ```

4. **Test PWA functionality**
   - PWA features require HTTPS
   - Use ngrok or similar for HTTPS testing locally
   ```bash
   ngrok http 8000
   ```

### Making Changes

1. Create a new branch for your feature
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes and test thoroughly

3. Commit with descriptive messages
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   ```

4. Push to repository
   ```bash
   git push origin feature/your-feature-name
   ```

## 📞 Support

For technical support or questions:
- **Email**: hello@dldemolition.com.au
- **Phone**: +61 451 612 742

## 📄 License

© 2024 DL Demolition Asbestos & Demolition. All rights reserved.

---

**Built with performance, conversion, and user experience in mind.**

*Last updated: November 22, 2025*
