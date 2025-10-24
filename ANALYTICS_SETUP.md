# Analytics Setup Guide

Your website is **ready for analytics**, but you need to set up an account first and add the tracking ID.

## Option 1: Google Analytics 4 (GA4) - Free

### Setup Steps:
1. Go to [Google Analytics](https://analytics.google.com/)
2. Click "Start measuring" or "Create Property"
3. Fill in your website details:
   - Property name: "Landon Holcomb Website"
   - Reporting timezone: Your timezone
   - Currency: USD
4. Under "Data streams", add a web stream:
   - Website URL: `https://landonholcomb.github.io`
   - Stream name: "Academic Website"
5. **Copy the Measurement ID** (looks like `G-XXXXXXXXXX`)
6. Add it to `config/_default/params.yaml`:
   ```yaml
   analytics:
     google_analytics: 'G-XXXXXXXXXX'  # Paste your ID here
   ```
7. Commit and push changes

### What You'll See:
- Real-time visitors
- Page views and popular content
- Geographic location of visitors
- Traffic sources (Google, direct, social, etc.)
- User behavior flow

**Dashboard**: https://analytics.google.com/

---

## Option 2: Plausible Analytics - Privacy-Focused

### Why Plausible?
- No cookies needed (GDPR/CCPA compliant)
- Lightweight (< 1 KB script)
- Privacy-friendly
- Clean, simple dashboard

### Setup Steps:
1. Go to [Plausible.io](https://plausible.io/)
2. Sign up (paid: $9/month for 10k pageviews)
3. Add your website: `landonholcomb.github.io`
4. Get your domain name from Plausible
5. Add it to `config/_default/params.yaml`:
   ```yaml
   analytics:
     plausible: 'landonholcomb.github.io'  # Your domain
   ```
6. Commit and push changes

### What You'll See:
- Real-time visitors
- Page views
- Top pages and referrers
- Countries and devices
- Simple, easy-to-read stats

**Dashboard**: https://plausible.io/landonholcomb.github.io

---

## Recommendation

**For academic websites, I recommend Google Analytics 4** because:
- ✅ Free
- ✅ More detailed data
- ✅ Integration with Google Search Console
- ✅ Good for tracking research impact

**Choose Plausible if**:
- You prioritize visitor privacy
- You want a cleaner, simpler dashboard
- You're okay with a paid service

---

## How to View Analytics

Once set up:

### Google Analytics:
1. Go to https://analytics.google.com/
2. Select your property
3. View reports:
   - **Realtime**: See live visitors
   - **Reports > Engagement**: Most viewed pages
   - **Reports > Acquisition**: Traffic sources

### Plausible:
1. Go to https://plausible.io/[your-domain]
2. Everything is on one dashboard

---

## What Metrics to Track

For an academic website, focus on:
- **Total visitors**: Overall reach
- **Top pages**: Which content is most popular (publications? blog?)
- **Referral sources**: Where visitors come from (Google Scholar, Twitter, etc.)
- **Geographic distribution**: Where your audience is located
- **Time trends**: Growth over time

This helps you understand:
- Which research topics resonate
- Impact of blog posts or papers
- When to share updates (based on traffic patterns)
