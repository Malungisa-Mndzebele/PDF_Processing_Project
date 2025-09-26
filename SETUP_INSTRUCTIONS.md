# 🚀 Quick Setup Instructions

Follow these steps to deploy your Birthday Book to `https://khasinogaming.com/birthdaybook`:

## 1. 📁 Upload to GitHub

1. **Create a new repository** on GitHub (or use existing one)
2. **Upload your files** to the repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Birthday Book PDF Gallery"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

## 2. 🔐 Configure GitHub Secrets

Go to your repository → **Settings** → **Secrets and variables** → **Actions**

Add these 3 secrets:

| Secret Name | Value |
|-------------|-------|
| `FTP_SERVER` | `server28.shared.spaceship.host` |
| `FTP_USERNAME` | `birthdaybook@khasinogaming.com` |
| `FTP_PASSWORD` | `@QWERTYasd` |

## 3. 🚀 Deploy

1. **Push to main branch** (triggers automatic deployment)
2. **OR** go to **Actions** tab → **Deploy to khasinogaming.com** → **Run workflow**

## 4. ✅ Verify

- Check **Actions** tab for deployment status
- Visit: `https://khasinogaming.com/birthdaybook`
- Wait 5-10 minutes for DNS propagation

## 🎯 What Gets Deployed

- ✅ `index.html` - Main website
- ✅ `style.css` - Styling
- ✅ `script.js` - Interactive features  
- ✅ `pdf_images/` - All 476 images
- ✅ Performance optimizations

## 🆘 Need Help?

- Check the **Actions** tab for error logs
- Verify all 3 secrets are configured
- Wait a few minutes for deployment to complete
- Contact hosting provider if server issues

---

**🎉 That's it!** Your Birthday Book will be live at `https://khasinogaming.com/birthdaybook`
