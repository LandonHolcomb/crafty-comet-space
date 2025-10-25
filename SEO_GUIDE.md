# SEO & Visibility Guide for landonholcomb.github.io

## What's Been Implemented

### 1. ✅ Enhanced Front-Matter Metadata
Added to all major pages (`_index.md`, `blog/_index.md`, `publications/_index.md`):
- **Title**: Descriptive, keyword-rich titles
- **Description**: Concise summaries for search results
- **Keywords**: Relevant search terms including:
  - "Landon Holcomb"
  - "quantum computing"
  - "quantum machine learning"
  - "QML", "QNLP"
  - "Clemson University"
  - "variational quantum algorithms"

### 2. ✅ JSON-LD Structured Data
Created `layouts/partials/hooks/head-end/custom-seo.html` with:
- **Schema.org Person markup** for rich search results
- Educational background (Clemson, Texas A&M)
- Research areas and expertise
- Social profiles (GitHub, LinkedIn)
- Contact information

### 3. ✅ Open Graph & Twitter Cards
Added meta tags for better social media sharing:
- OG tags for Facebook/LinkedIn
- Twitter Card metadata
- Profile image integration

### 4. ✅ Sitemap Configuration
Enhanced `hugo.yaml` with:
- Weekly change frequency
- Priority settings
- Automatic sitemap generation at `/sitemap.xml`

### 5. ✅ Custom Robots.txt
Created `layouts/robots.txt` with:
- Search engine permissions
- Sitemap location
- Crawl delay settings

## Immediate Actions Required

### 1. Submit to Google Search Console (Priority #1)
**This is why you're not showing up in search!**

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Add property: `https://landonholcomb.github.io`
3. Verify ownership (GitHub Pages method):
   - Click "URL prefix" method
   - Download verification HTML file
   - Add to `static/` folder
   - Commit and push
4. After verification, submit sitemap: `https://landonholcomb.github.io/sitemap.xml`

### 2. Submit to Bing Webmaster Tools
1. Go to [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. Add site: `https://landonholcomb.github.io`
3. Import from Google Search Console (easier) OR verify manually
4. Submit sitemap

### 3. Add Google Analytics (Optional but Recommended)
1. Create GA4 property at [Google Analytics](https://analytics.google.com)
2. Get measurement ID (format: `G-XXXXXXXXXX`)
3. Add to `config/_default/params.yaml`:
   ```yaml
   marketing:
     analytics:
       google_analytics: 'G-XXXXXXXXXX'
   ```

### 4. Verify Your Sitemap Works
After deploying, check:
- `https://landonholcomb.github.io/sitemap.xml` - should show XML sitemap
- `https://landonholcomb.github.io/robots.txt` - should show robots directives

## Why You're Not Showing Up (And How to Fix It)

### Current Issues:
1. **Not indexed by Google** - You need to manually submit to Search Console
2. **New domain** - GitHub Pages sites need time to build authority
3. **Limited external links** - No backlinks pointing to your site yet

### Solutions:

#### Immediate (1-2 weeks):
- ✅ Submit to Google Search Console
- ✅ Submit to Bing Webmaster Tools
- ✅ Check sitemap generation after next deploy
- ✅ Verify all metadata is working

#### Short-term (2-4 weeks):
- Add your website to:
  - LinkedIn profile
  - GitHub profile README
  - ORCID profile (create if you don't have one)
  - ResearchGate profile
  - Any university directory listings
- Share blog posts on social media
- Link to your site from any previous publications

#### Medium-term (1-3 months):
- Write blog posts with long-tail keywords:
  - "How to get started with quantum machine learning"
  - "Understanding barren plateaus in variational quantum circuits"
  - "Qiskit vs PennyLane comparison"
- Guest post on quantum computing blogs
- Contribute to discussions on quantum computing forums
- Present at conferences and link to your site in slides

## SEO Best Practices Going Forward

### For New Blog Posts:
Always include in front-matter:
```yaml
---
title: "Descriptive Title with Keywords"
date: 2025-10-25
description: "Clear 150-160 character summary for search results"
keywords:
  - specific keyword 1
  - specific keyword 2
  - quantum computing
  - your name
image: "featured.jpg"  # Add a featured image
---
```

### For New Publications:
Always include:
```yaml
---
title: "Paper Title"
authors: ["Landon Holcomb", "Co-author"]
date: 2025-10-25
publication: "Journal Name"
abstract: "Full abstract here"
tags:
  - Quantum Computing
  - Machine Learning
---
```

## Tracking Your Progress

### Google Search Console Metrics to Watch:
- **Impressions**: How often your site appears in search
- **Clicks**: How many people click through
- **Average Position**: Where you rank for queries
- **Coverage**: Which pages are indexed

### Search Queries to Target:
- "Landon Holcomb" (your name - should rank #1)
- "Landon Holcomb quantum computing"
- "Clemson quantum computing PhD students"
- "quantum machine learning research"
- "QNLP research"

## Expected Timeline

- **Week 1-2**: Google crawls and indexes your site
- **Week 3-4**: Start appearing for "Landon Holcomb" searches
- **Month 2-3**: Appear for "Landon Holcomb quantum computing"
- **Month 3-6**: Start ranking for broader research terms

## Technical Validation

After deploying, use these tools to verify:
1. **Google Rich Results Test**: https://search.google.com/test/rich-results
   - Paste your homepage URL
   - Should show "Person" schema detected
   
2. **Schema Markup Validator**: https://validator.schema.org/
   - Paste your homepage URL
   - Verify JSON-LD is valid

3. **Open Graph Debugger**: https://developers.facebook.com/tools/debug/
   - Test how your site appears when shared

## Common Issues & Solutions

### Issue: "My sitemap shows 404"
- Check that `enableRobotsTXT: true` in `hugo.yaml`
- Verify `layouts/robots.txt` exists
- Rebuild and redeploy

### Issue: "Google says pages aren't indexed"
- Check robots.txt allows crawling
- Verify sitemap is submitted to Search Console
- Check for `noindex` meta tags (shouldn't exist)

### Issue: "Search results show wrong description"
- Update `description` in front-matter
- Request re-indexing in Search Console
- Wait 1-2 weeks for update

## Additional Resources

- [Google Search Central](https://developers.google.com/search/docs)
- [Bing Webmaster Guidelines](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
- [Schema.org Person Documentation](https://schema.org/Person)
- [Academic SEO Guide](https://www.aje.com/arc/seo-for-academics/)

---

**Bottom Line**: The main reason you're not showing up is that Google doesn't know your site exists yet. Once you submit to Search Console and get indexed (1-2 weeks), you should start appearing for searches with your name. Building broader visibility takes 2-6 months of consistent content and backlinks.
