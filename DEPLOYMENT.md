# Invoice Analyzer - Deployment Guide

## Render Deployment Setup

This project is configured for free deployment on Render with CI/CD integration.

### Files Created for Deployment:

1. **render.yaml** - Render service configuration
2. **Procfile** - Process file for web server
3. **requirements.txt** - Updated with specific versions
4. **app.py** - Updated for production deployment
5. **.github/workflows/deploy.yml** - CI/CD pipeline

### Deployment Steps:

#### 1. Push to GitHub
```bash
git add .
git commit -m "Add Render deployment configuration"
git push origin main
```

#### 2. Connect to Render
1. Go to [render.com](https://render.com)
2. Sign up/login with GitHub
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Render will automatically detect the `render.yaml` configuration

#### 3. Set Environment Variables
In Render dashboard, add:
- `GOOGLE_API_KEY`: Your Google Generative AI API key

#### 4. Deploy
- Render will automatically deploy when you push to main branch
- The CI/CD pipeline will run tests before deployment

### CI/CD Features:
- **Automatic testing** on every push/PR
- **Automatic deployment** to Render on main branch
- **Linting** with flake8
- **Dependency installation** and testing

### Free Tier Limits:
- 750 hours/month
- Sleeps after 15 minutes of inactivity
- Cold start time ~30 seconds

### Custom Domain (Optional):
- Add custom domain in Render dashboard
- Free SSL certificate included

Your app will be available at: `https://your-app-name.onrender.com`
