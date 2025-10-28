# Landon Holcomb's Academic Website# Landon Holcomb's Academic Website# Landon Holcomb's Academic Website# Landon Holcomb's Academic Website



[![Live Site](https://img.shields.io/badge/Live_Site-landonholcomb.com-blue)](https://landonholcomb.com)

[![Built with Hugo](https://img.shields.io/badge/Built_with-Hugo-ff4088)](https://gohugo.io/)

[![Theme](https://img.shields.io/badge/Theme-Hugo_Blox-00d4aa)](https://hugoblox.com)[![Live Site](https://img.shields.io/badge/Live_Site-landonholcomb.com-blue)](https://landonholcomb.com)



Personal academic website for Landon Holcomb, PhD student in Computer Science at Clemson University.[![Built with Hugo](https://img.shields.io/badge/Built_with-Hugo-ff4088)](https://gohugo.io/)



## About[![Theme](https://img.shields.io/badge/Theme-Hugo_Blox-00d4aa)](https://hugoblox.com)[![Live Site](https://img.shields.io/badge/🌐_Live_Site-landonholcomb.github.io-blue)](https://landonholcomb.github.io)[![Live Site](https://img.shields.io/badge/🌐_Live_Site-landonholcomb.github.io-blue)](https://landonholcomb.github.io)



This site showcases my research in:

- **Quantum Machine Learning (QML)**

- **Quantum Natural Language Processing (QNLP)**Personal academic website for Landon Holcomb, PhD student in Computer Science at Clemson University.[![Built with Hugo](https://img.shields.io/badge/Built_with-Hugo-ff4088)](https://gohugo.io/)[![Built with Hugo](https://img.shields.io/badge/Built_with-Hugo-ff4088)](https://gohugo.io/)

- **Variational Quantum Algorithms**

- **Quantum Algorithm Design & Optimization**



## Site Features## About[![Theme](https://img.shields.io/badge/Theme-Hugo_Blox-00d4aa)](https://hugoblox.com)[![Theme](https://img.shields.io/badge/Theme-Hugo_Blox-00d4aa)](https://hugoblox.com)



- **Research Profile**: Education, interests, and research focus

- **Publications**: BibTeX-powered publication management

  - Current research (PhD work)This site showcases my research in:

  - Earlier work (undergraduate research)

- **Blog**: Technical notes and tutorials on quantum computing- **Quantum Machine Learning (QML)**

- **SEO Optimized**: JSON-LD structured data, meta tags, sitemap

- **Responsive Design**: Mobile-friendly, professional layout- **Quantum Natural Language Processing (QNLP)**Personal academic website for Landon Holcomb, PhD student in Computer Science at Clemson University.Personal academic website for Landon Holcomb, PhD student in Computer Science at Clemson University.



## Tech Stack- **Variational Quantum Algorithms**



- **Static Site Generator**: [Hugo](https://gohugo.io/)- **Quantum Algorithm Design & Optimization**

- **Theme**: [Hugo Blox Builder](https://hugoblox.com) (Academic CV template)

- **Hosting**: GitHub Pages

- **CI/CD**: GitHub Actions (automatic deployment)

- **Analytics Ready**: Google Analytics & Plausible support## Site Features## 🎓 About## 🎓 About



## Project Structure



```- **Research Profile**: Education, interests, and research focus

crafty-comet-space/

├── config/_default/          # Site configuration- **Publications**: BibTeX-powered publication management

│   ├── hugo.yaml            # Hugo settings

│   ├── params.yaml          # Theme parameters  - Current research (PhD work)This site showcases my research in:This site showcases my research in:

│   └── menus.yaml           # Navigation menus

├── content/                  # Site content  - Earlier work (undergraduate research)

│   ├── _index.md            # Homepage

│   ├── authors/admin/       # Author profile- **Blog**: Technical notes and tutorials on quantum computing- **Quantum Machine Learning (QML)**- **Quantum Machine Learning (QML)**

│   ├── blog/                # Blog posts

│   ├── publications/        # Current research- **SEO Optimized**: JSON-LD structured data, meta tags, sitemap

│   └── publications-undergrad/  # Earlier work

├── layouts/                  # Custom layouts- **Responsive Design**: Mobile-friendly, professional layout- **Quantum Natural Language Processing (QNLP)**- **Quantum Natural Language Processing (QNLP)**

│   ├── partials/hooks/      # SEO & custom HTML

│   └── robots.txt           # Search engine directives

├── static/uploads/          # CV and files

└── assets/                  # Images and media## Tech Stack- **Variational Quantum Algorithms**- **Variational Quantum Algorithms**

```



## Content Management

- **Static Site Generator**: [Hugo](https://gohugo.io/)- **Quantum Algorithm Design & Optimization**- **Quantum Algorithm Design & Optimization**

### Adding Publications

- **Theme**: [Hugo Blox Builder](https://hugoblox.com) (Academic CV template)

Use the provided BibTeX import script:

- **Hosting**: GitHub Pages

```powershell

python import_publications.py- **CI/CD**: GitHub Actions (automatic deployment)

```

- **Analytics Ready**: Google Analytics & Plausible support## 🚀 Site Features## 🚀 Site Features

Place `.bib` files in:

- `content/publications/` for current research

- `content/publications-undergrad/` for earlier work

## Project Structure

See `PUBLICATIONS_GUIDE.md` for details.



### Writing Blog Posts

```- **Research Profile**: Education, interests, and research focus- **Research Profile**: Education, interests, and research focus

Create new posts in `content/blog/`:

crafty-comet-space/

```yaml

---├── config/_default/          # Site configuration- **Publications**: BibTeX-powered publication management- **Publications**: BibTeX-powered publication management

title: "Your Post Title"

date: 2025-10-28│   ├── hugo.yaml            # Hugo settings

description: "Brief description for SEO"

keywords:│   ├── params.yaml          # Theme parameters  - Current research (PhD work)  - Current research (PhD work)

  - quantum computing

  - tutorial│   └── menus.yaml           # Navigation menus

image: "featured.jpg"

---├── content/                  # Site content  - Earlier work (undergraduate research)  - Earlier work (undergraduate research)



Your content here...│   ├── _index.md            # Homepage

```

│   ├── authors/admin/       # Author profile- **Blog**: Technical notes and tutorials on quantum computing- **Blog**: Technical notes and tutorials on quantum computing

## Local Development

│   ├── blog/                # Blog posts

### Prerequisites

│   ├── publications/        # Current research- **SEO Optimized**: JSON-LD structured data, meta tags, sitemap- **SEO Optimized**: JSON-LD structured data, meta tags, sitemap

- [Hugo Extended](https://gohugo.io/installation/) (v0.112.0+)

- [Go](https://go.dev/dl/) (v1.19+)│   └── publications-undergrad/  # Earlier work



### Setup├── layouts/                  # Custom layouts- **Responsive Design**: Mobile-friendly, professional layout- **Responsive Design**: Mobile-friendly, professional layout



```powershell│   ├── partials/hooks/      # SEO & custom HTML

# Clone the repository

git clone https://github.com/LandonHolcomb/landonholcomb.github.io.git│   └── robots.txt           # Search engine directives

cd landonholcomb.github.io

├── static/uploads/          # CV and files

# Install dependencies

hugo mod get -u└── assets/                  # Images and media## 🛠️ Tech Stack## 🛠️ Tech Stack



# Run development server```

hugo server

```



Visit `http://localhost:1313` to preview.## Content Management



## SEO & Visibility- **Static Site Generator**: [Hugo](https://gohugo.io/)- **Static Site Generator**: [Hugo](https://gohugo.io/)



### Implemented Features### Adding Publications



- **JSON-LD Structured Data** - Schema.org Person markup- **Theme**: [Hugo Blox Builder](https://hugoblox.com) (Academic CV template)- **Theme**: [Hugo Blox Builder](https://hugoblox.com) (Academic CV template)

- **Meta Tags** - Title, description, keywords on all pages

- **Open Graph** - Social media sharing optimizationUse the provided BibTeX import script:

- **Twitter Cards** - Rich tweet previews

- **Sitemap** - Automatic generation at `/sitemap.xml`- **Hosting**: GitHub Pages- **Hosting**: GitHub Pages

- **Robots.txt** - Search engine crawl instructions

```powershell

### Indexing Status

python import_publications.py- **CI/CD**: GitHub Actions (automatic deployment)- **CI/CD**: GitHub Actions (automatic deployment)

To get indexed by search engines:

1. Submit to [Google Search Console](https://search.google.com/search-console)```

2. Submit to [Bing Webmaster Tools](https://www.bing.com/webmasters)

3. Submit sitemap: `https://landonholcomb.com/sitemap.xml`- **Analytics Ready**: Google Analytics & Plausible support- **Analytics Ready**: Google Analytics & Plausible support



See `SEO_GUIDE.md` for complete instructions.Place `.bib` files in:



## Customization- `content/publications/` for current research



### Theme Settings- `content/publications-undergrad/` for earlier work



Edit `config/_default/params.yaml`:## 📁 Project Structure## 📁 Project Structure

- Color scheme (currently: cyan)

- Font optionsSee `PUBLICATIONS_GUIDE.md` for details.

- Analytics IDs

- Footer content



### Navigation Menu### Writing Blog Posts



Edit `config/_default/menus.yaml` to add/remove menu items.``````



### Homepage SectionsCreate new posts in `content/blog/`:



Edit `content/_index.md` to customize sections:crafty-comet-space/crafty-comet-space/

- Biography & education

- Research focus```yaml

- Publications

- Blog posts---├── config/_default/          # Site configuration├── config/_default/          # Site configuration

- Teaching & outreach

title: "Your Post Title"

## Deployment

date: 2025-10-25│   ├── hugo.yaml            # Hugo settings│   ├── hugo.yaml            # Hugo settings

The site auto-deploys via GitHub Actions when you push to `main`:

description: "Brief description for SEO"

```powershell

git add -Akeywords:│   ├── params.yaml          # Theme parameters│   ├── params.yaml          # Theme parameters

git commit -m "Your update message"

git push origin main  - quantum computing

```

  - tutorial│   └── menus.yaml           # Navigation menus│   └── menus.yaml           # Navigation menus

Changes go live at `https://landonholcomb.com` in ~2 minutes.

image: "featured.jpg"

## Documentation

---├── content/                  # Site content├── content/                  # Site content

- **SEO_GUIDE.md** - SEO optimization & Google Search Console setup

- **PUBLICATIONS_GUIDE.md** - BibTeX import system documentation

- **ANALYTICS_SETUP.md** - Analytics configuration guide

Your content here...│   ├── _index.md            # Homepage│   ├── _index.md            # Homepage

## Links

```

- **Live Site**: [landonholcomb.com](https://landonholcomb.com)

- **GitHub**: [@LandonHolcomb](https://github.com/LandonHolcomb)│   ├── authors/admin/       # Author profile│   ├── authors/admin/       # Author profile

- **LinkedIn**: [landonholcomb](https://www.linkedin.com/in/landonholcomb)

- **Email**: lholco2@clemson.edu## Local Development



## License│   ├── blog/                # Blog posts│   ├── blog/                # Blog posts



Content © 2025 Landon Holcomb. All rights reserved.### Prerequisites



Website theme: [Hugo Blox Builder](https://github.com/HugoBlox/hugo-blox-builder) (MIT License)│   ├── publications/        # Current research│   ├── publications/        # Current research



---- [Hugo Extended](https://gohugo.io/installation/) (v0.112.0+)



Built with Hugo & Hugo Blox Builder- [Go](https://go.dev/dl/) (v1.19+)│   └── publications-undergrad/  # Earlier work│   └── publications-undergrad/  # Earlier work




### Setup├── layouts/                  # Custom layouts├── layouts/                  # Custom layouts



```powershell│   ├── partials/hooks/      # SEO & custom HTML│   ├── partials/hooks/      # SEO & custom HTML

# Clone the repository

git clone https://github.com/LandonHolcomb/landonholcomb.github.io.git│   └── robots.txt           # Search engine directives│   └── robots.txt           # Search engine directives

cd landonholcomb.github.io

├── static/uploads/          # CV and files├── static/uploads/          # CV and files

# Install dependencies

hugo mod get -u└── assets/                  # Images and media└── assets/                  # Images and media



# Run development server``````

hugo server

```



Visit `http://localhost:1313` to preview.## 📝 Content Management## 📝 Content Management



## SEO & Visibility



### Implemented Features### Adding Publications### Adding Publications



- **JSON-LD Structured Data** - Schema.org Person markup

- **Meta Tags** - Title, description, keywords on all pages

- **Open Graph** - Social media sharing optimizationUse the provided BibTeX import script:Use the provided BibTeX import script:

- **Twitter Cards** - Rich tweet previews

- **Sitemap** - Automatic generation at `/sitemap.xml`

- **Robots.txt** - Search engine crawl instructions

```powershell```powershell

### Indexing Status

python import_publications.pypython import_publications.py

To get indexed by search engines:

1. Submit to [Google Search Console](https://search.google.com/search-console)``````

2. Submit to [Bing Webmaster Tools](https://www.bing.com/webmasters)

3. Submit sitemap: `https://landonholcomb.com/sitemap.xml`



See `SEO_GUIDE.md` for complete instructions.Place `.bib` files in:Place `.bib` files in:



## Customization- `content/publications/` for current research- `content/publications/` for current research



### Theme Settings- `content/publications-undergrad/` for earlier work- `content/publications-undergrad/` for earlier work



Edit `config/_default/params.yaml`:

- Color scheme (currently: cyan)

- Font optionsSee `PUBLICATIONS_GUIDE.md` for details.See `PUBLICATIONS_GUIDE.md` for details.

- Analytics IDs

- Footer content



### Navigation Menu### Writing Blog Posts### Writing Blog Posts



Edit `config/_default/menus.yaml` to add/remove menu items.



### Homepage SectionsCreate new posts in `content/blog/`:Create new posts in `content/blog/`:



Edit `content/_index.md` to customize sections:

- Biography & education

- Research focus```yaml```yaml

- Publications

- Blog posts------

- Teaching & outreach

title: "Your Post Title"title: "Your Post Title"

## Deployment

date: 2025-10-25date: 2025-10-25

The site auto-deploys via GitHub Actions when you push to `main`:

description: "Brief description for SEO"description: "Brief description for SEO"

```powershell

git add -Akeywords:keywords:

git commit -m "Your update message"

git push origin main  - quantum computing  - quantum computing

```

  - tutorial  - tutorial

Changes go live at `https://landonholcomb.com` in ~2 minutes.

image: "featured.jpg"image: "featured.jpg"

## Documentation

------

- **`SEO_GUIDE.md`** - SEO optimization & Google Search Console setup

- **`PUBLICATIONS_GUIDE.md`** - BibTeX import system documentation

- **`ANALYTICS_SETUP.md`** - Analytics configuration guide

Your content here...Your content here...

## Links

``````

- **Live Site**: [landonholcomb.com](https://landonholcomb.com)

- **GitHub**: [@LandonHolcomb](https://github.com/LandonHolcomb)

- **LinkedIn**: [landonholcomb](https://www.linkedin.com/in/landonholcomb)

- **Email**: lholco2@clemson.edu## 🔧 Local Development## 🔧 Local Development



## License



Content © 2025 Landon Holcomb. All rights reserved.### Prerequisites### Prerequisites



Website theme: [Hugo Blox Builder](https://github.com/HugoBlox/hugo-blox-builder) (MIT License)



---- [Hugo Extended](https://gohugo.io/installation/) (v0.112.0+)- [Hugo Extended](https://gohugo.io/installation/) (v0.112.0+)



**Built with Hugo & Hugo Blox Builder**- [Go](https://go.dev/dl/) (v1.19+)- [Go](https://go.dev/dl/) (v1.19+)




### Setup### Setup



```powershell```powershell

# Clone the repository# Clone the repository

git clone https://github.com/LandonHolcomb/landonholcomb.github.io.gitgit clone https://github.com/LandonHolcomb/landonholcomb.github.io.git

cd landonholcomb.github.iocd landonholcomb.github.io



# Install dependencies# Install dependencies

hugo mod get -uhugo mod get -u



# Run development server# Run development server

hugo serverhugo server

``````



Visit `http://localhost:1313` to preview.Visit `http://localhost:1313` to preview.



## 📊 SEO & Visibility## 📊 SEO & Visibility



### Implemented Features### Implemented Features



✅ **JSON-LD Structured Data** - Schema.org Person markup  ✅ **JSON-LD Structured Data** - Schema.org Person markup  

✅ **Meta Tags** - Title, description, keywords on all pages  ✅ **Meta Tags** - Title, description, keywords on all pages  

✅ **Open Graph** - Social media sharing optimization  ✅ **Open Graph** - Social media sharing optimization  

✅ **Twitter Cards** - Rich tweet previews  ✅ **Twitter Cards** - Rich tweet previews  

✅ **Sitemap** - Automatic generation at `/sitemap.xml`  ✅ **Sitemap** - Automatic generation at `/sitemap.xml`  

✅ **Robots.txt** - Search engine crawl instructions  ✅ **Robots.txt** - Search engine crawl instructions  



### Indexing Status### Indexing Status



To get indexed by search engines:To get indexed by search engines:

1. Submit to [Google Search Console](https://search.google.com/search-console)1. Submit to [Google Search Console](https://search.google.com/search-console)

2. Submit to [Bing Webmaster Tools](https://www.bing.com/webmasters)2. Submit to [Bing Webmaster Tools](https://www.bing.com/webmasters)

3. Submit sitemap: `https://landonholcomb.github.io/sitemap.xml`3. Submit sitemap: `https://landonholcomb.github.io/sitemap.xml`



See `SEO_GUIDE.md` for complete instructions.See `SEO_GUIDE.md` for complete instructions.



## 🎨 Customization## 🎨 Customization



### Theme Settings### Theme Settings



Edit `config/_default/params.yaml`:Edit `config/_default/params.yaml`:

- Color scheme (currently: cyan)- Color scheme (currently: cyan)

- Font options- Font options

- Analytics IDs- Analytics IDs

- Footer content- Footer content



### Navigation Menu### Navigation Menu



Edit `config/_default/menus.yaml` to add/remove menu items.Edit `config/_default/menus.yaml` to add/remove menu items.



### Homepage Sections### Homepage Sections



Edit `content/_index.md` to customize sections:Edit `content/_index.md` to customize sections:

- Biography & education- Biography & education

- Research focus- Research focus

- Publications- Publications

- Blog posts- Blog posts

- Teaching & outreach- Teaching & outreach



## 📦 Deployment## 📦 Deployment



The site auto-deploys via GitHub Actions when you push to `main`:The site auto-deploys via GitHub Actions when you push to `main`:



```powershell```powershell

git add -Agit add -A

git commit -m "Your update message"git commit -m "Your update message"

git push origin maingit push origin main

``````



Changes go live at `https://landonholcomb.github.io` in ~2 minutes.Changes go live at `https://landonholcomb.github.io` in ~2 minutes.



## 📚 Documentation## � Documentation



- **`SEO_GUIDE.md`** - SEO optimization & Google Search Console setup- **`SEO_GUIDE.md`** - SEO optimization & Google Search Console setup

- **`PUBLICATIONS_GUIDE.md`** - BibTeX import system documentation- **`PUBLICATIONS_GUIDE.md`** - BibTeX import system documentation

- **`ANALYTICS_SETUP.md`** - Analytics configuration guide- **`ANALYTICS_SETUP.md`** - Analytics configuration guide



## 🔗 Links## 🔗 Links



- **Live Site**: [landonholcomb.github.io](https://landonholcomb.github.io)- **Live Site**: [landonholcomb.github.io](https://landonholcomb.github.io)

- **GitHub**: [@LandonHolcomb](https://github.com/LandonHolcomb)- **GitHub**: [@LandonHolcomb](https://github.com/LandonHolcomb)

- **LinkedIn**: [landonholcomb](https://www.linkedin.com/in/landonholcomb)- **LinkedIn**: [landonholcomb](https://www.linkedin.com/in/landonholcomb)

- **Email**: lholco2@clemson.edu- **Email**: lholco2@clemson.edu



## 📄 License## 📄 License



Content © 2025 Landon Holcomb. All rights reserved.Content © 2025 Landon Holcomb. All rights reserved.



Website theme: [Hugo Blox Builder](https://github.com/HugoBlox/hugo-blox-builder) (MIT License)Website theme: [Hugo Blox Builder](https://github.com/HugoBlox/hugo-blox-builder) (MIT License)



------



**Built with** ❤️ **using Hugo & Hugo Blox Builder****Built with** ❤️ **using Hugo & Hugo Blox Builder**


## Level Up with Pro Templates

Ready to take your career to the next level? Our Pro templates offer exclusive designs and features to help you stand out even more.

<!-- <p align="center">
  <img src="" alt="Free vs Pro templates">
</p>-->

| Feature              | Academic CV (Free)       | Academic CV Pro & Resumé Pro     |
| -------------------- | ------------------------ | -------------------------------- |
| **Design**           | Professional & clean     | **Exclusive premium designs**    |
| **Layouts**          | Standard resumé sections | **Advanced layouts & timelines** |
| **Call to Action**   | Simple contact link      | **Prominent CTA buttons**        |
| **First Impression** | Strong                   | **Unforgettable**                |

<br/>
<p align="center">
  <a href="https://hugoblox.com/pro?utm_source=github&utm_medium=readme"><b>💎 Get the Pro Pass</b></a> — Includes all Pro templates for a one-time price.<br/>
  <a href="https://hugoblox.com/templates/academic-cv-pro/start?utm_source=github&utm_medium=readme">✨ Deploy Academic CV Pro</a>
  &nbsp;•&nbsp;
  <a href="https://hugoblox.com/templates/resume-pro/start?utm_source=github&utm_medium=readme">📄 Deploy Resumé Pro</a>
</p>

---

## What Researchers Say

> “Hugo Blox saved me 40+ hours on my lab site. BibTeX integration auto-updates publications — **our citations are up 3×**.”
> — **Dr. Sarah Yang**, AI Researcher

---

## Get Started in Minutes

### Recommended (Fastest)

Deploy your site to GitHub Pages in just 60 seconds with our browser-based starter.

👉 <a href="https://hugoblox.com/templates/academic-cv/start?utm_source=github&utm_medium=readme"><b>Start with the Academic CV Template</b></a>

### Prefer the Command Line?

Use the local quickstart:

```bash
# 1. Install Hugo Extended → https://docs.hugoblox.com/getting-started/install-hugo/
# 2. Clone this starter
git clone https://github.com/HugoBlox/theme-academic-cv my-site
cd my-site

# 3. Run locally
pnpm install && hugo server
```

For more guides, visit our documentation at **https://docs.hugoblox.com/**.

---

## Join the Community

Join thousands of creators in our vibrant community to ask questions, share your work, and help us improve.

- 💬 <a href="https://discord.gg/z8wNYzb">Discord</a>
- 📚 <a href="https://docs.hugoblox.com/?utm_source=github&utm_medium=readme">Docs & Guides</a>
- 🐦 <a href="https://x.com/BuildLore">X / Twitter</a>
- ⭐ <a href="https://github.com/HugoBlox/hugo-blox-builder">Star on GitHub</a>

---

MIT © 2016-Present [George Cushen](https://georgecushen.com)

<!--START_SECTION:news-->
<!--END_SECTION:news-->
