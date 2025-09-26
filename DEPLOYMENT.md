# 🚀 Deployment Guide - The Birthday Book

This guide explains how to deploy The Birthday Book to `https://khasinogaming.com/birthdaybook` using GitHub Actions.

## 📋 Prerequisites

1. **GitHub Repository**: Your project must be in a GitHub repository
2. **FTP Credentials**: Access to the hosting server with FTP credentials
3. **GitHub Secrets**: Configured repository secrets for secure deployment

## 🔐 Setting Up GitHub Secrets

You need to add the following secrets to your GitHub repository:

### Required Secrets

1. Go to your GitHub repository
2. Click on **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret** and add:

| Secret Name | Value | Description |
|-------------|-------|-------------|
| `FTP_SERVER` | `server28.shared.spaceship.host` | FTP server address |
| `FTP_USERNAME` | `birthdaybook@khasinogaming.com` | FTP username |
| `FTP_PASSWORD` | `@QWERTYasd` | FTP password |

### How to Add Secrets

1. Navigate to: `https://github.com/YOUR_USERNAME/YOUR_REPO/settings/secrets/actions`
2. Click **"New repository secret"**
3. Enter the secret name and value
4. Click **"Add secret"**

## 🚀 Deployment Process

### Automatic Deployment

The deployment happens automatically when you:

1. **Push to main/master branch**: Any push triggers deployment
2. **Create a Pull Request**: PRs trigger deployment for testing
3. **Manual trigger**: Use the "Actions" tab to run deployment manually

### Manual Deployment

1. Go to your repository's **Actions** tab
2. Select **"Deploy to khasinogaming.com"** workflow
3. Click **"Run workflow"**
4. Select the branch and click **"Run workflow"**

## 📁 What Gets Deployed

The deployment includes:

- ✅ `index.html` - Main website file
- ✅ `style.css` - Styling and animations
- ✅ `script.js` - Interactive functionality
- ✅ `pdf_images/` - All 476 images (complete directory)
- ✅ `.htaccess` - Server configuration for performance
- ✅ `README.md` - Deployment documentation

### Excluded Files

The following files are **NOT** deployed (kept in repository only):

- ❌ Python scripts (`*.py`)
- ❌ PDF files (`*.pdf`)
- ❌ OCR results (`small_batch_results/`, `batch_results/`)
- ❌ Analysis files (`*.json`, `*.txt`)
- ❌ Batch files (`*.bat`)
- ❌ Git files (`.git/`, `.gitignore`)

## 🔧 Deployment Configuration

### Server Settings

- **Target URL**: `https://khasinogaming.com/birthdaybook`
- **FTP Server**: `server28.shared.spaceship.host`
- **FTP Port**: `21` (standard FTP)
- **Remote Directory**: `/khasinogaming.com/birthdaybook/`

### Performance Optimizations

The deployment includes automatic optimizations:

1. **Gzip Compression**: Enabled for all text files
2. **Image Caching**: 1-month cache for images
3. **CSS/JS Caching**: 1-week cache for assets
4. **Security Headers**: Basic security headers added

## 📊 Monitoring Deployment

### Check Deployment Status

1. Go to **Actions** tab in your repository
2. Look for the latest **"Deploy to khasinogaming.com"** run
3. Click on it to see detailed logs

### Deployment Logs

The workflow provides detailed logs for:
- ✅ File preparation
- ✅ FTP upload progress
- ✅ Deployment verification
- ❌ Error messages (if any)

## 🐛 Troubleshooting

### Common Issues

1. **FTP Connection Failed**
   - Check if FTP credentials are correct
   - Verify server is accessible
   - Ensure firewall allows FTP connections

2. **Files Not Uploading**
   - Check file permissions
   - Verify remote directory exists
   - Check available disk space

3. **Site Not Loading**
   - Wait 5-10 minutes for DNS propagation
   - Check if files were uploaded correctly
   - Verify server configuration

### Getting Help

If you encounter issues:

1. Check the **Actions** tab for error logs
2. Verify all secrets are configured correctly
3. Test FTP connection manually if needed
4. Contact hosting provider for server issues

## 🔄 Updating the Site

To update your deployed site:

1. **Make changes** to your local files
2. **Commit and push** to the main branch
3. **Deployment happens automatically**
4. **Check Actions tab** for deployment status
5. **Visit your site** to verify changes

## 📈 Performance Tips

### For Better Performance

1. **Optimize Images**: Compress images before committing
2. **Minify CSS/JS**: Use minified versions for production
3. **Use CDN**: Consider using a CDN for faster loading
4. **Monitor Usage**: Check server logs for performance

### File Size Considerations

- **Current Images**: ~476 PNG files
- **Total Size**: Depends on image compression
- **Loading Time**: Optimized with lazy loading
- **Caching**: Images cached for 1 month

## 🎯 Next Steps

After successful deployment:

1. ✅ **Test the live site**: Visit `https://khasinogaming.com/birthdaybook`
2. ✅ **Check all features**: Test filtering, search, modal viewing
3. ✅ **Mobile testing**: Verify responsive design
4. ✅ **Performance check**: Test loading times
5. ✅ **Share the link**: Let others know about your gallery!

---

**🎉 Congratulations!** Your Birthday Book is now live on the web!

For any questions or issues, check the GitHub Actions logs or refer to this documentation.
