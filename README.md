# Invoice Analyzer App

A Flask-based web application that uses Google's Generative AI (Gemma) to analyze invoice images and answer questions about them.

## Features

- Upload invoice images
- AI-powered analysis using Google's Gemma model
- Interactive Q&A about invoice content
- Settings page for API key management
- Analytics dashboard
- Responsive web interface

## Tech Stack

- **Backend**: Flask (Python)
- **AI Model**: Google Generative AI (Gemma-3-27b-it)
- **Frontend**: HTML, CSS, JavaScript
- **Image Processing**: Pillow (PIL)
- **Deployment**: Docker, Render
- **CI/CD**: GitHub Actions

## Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd project3
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your Google API key
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the app**
   Open http://localhost:5000 in your browser

### Docker Development

1. **Build the Docker image**
   ```bash
   docker build -t invoice-analyzer .
   ```

2. **Run the container**
   ```bash
   docker run -p 5000:5000 --env-file .env invoice-analyzer
   ```

## Deployment on Render

### Prerequisites

1. GitHub repository with your code
2. Google AI API key
3. Render account (free tier available)

### Steps

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Add Docker and CI/CD setup"
   git push origin main
   ```

2. **Connect to Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure the service**
   - **Name**: `invoice-analyzer-app`
   - **Environment**: `Docker`
   - **Dockerfile Path**: `./Dockerfile`
   - **Branch**: `main`
   - **Plan**: `Free`

4. **Set environment variables**
   - `GOOGLE_API_KEY`: Your Google AI API key
   - `SECRET_KEY`: A secure random string
   - `FLASK_ENV`: `production`
   - `PORT`: `5000`

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app

### CI/CD with GitHub Actions

The repository includes a GitHub Actions workflow that:

1. **Tests** the application on every push/PR
2. **Builds** Docker image on main branch pushes
3. **Pushes** to GitHub Container Registry
4. **Deploys** to Render automatically

#### Required Secrets

Add these secrets to your GitHub repository:

- `RENDER_SERVICE_ID`: Your Render service ID
- `RENDER_API_KEY`: Your Render API key

To get these:
1. Go to your Render service settings
2. Find "Service ID" in the service details
3. Generate API key in Render account settings

## Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GOOGLE_API_KEY` | Google AI API key | Yes | - |
| `SECRET_KEY` | Flask secret key | Yes | - |
| `FLASK_ENV` | Flask environment | No | `development` |
| `PORT` | Server port | No | `5000` |
| `HOST` | Server host | No | `0.0.0.0` |

## API Endpoints

- `GET /` - Home page
- `GET /settings` - Settings page
- `GET /analytics` - Analytics dashboard
- `POST /save-api-key` - Save API key
- `POST /test-api-key` - Test API key
- `POST /analyze` - Analyze invoice image

## Project Structure

```
project3/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── .dockerignore         # Docker ignore file
├── render.yaml           # Render deployment config
├── .env.example          # Environment variables template
├── .github/
│   └── workflows/
│       └── ci-cd.yml     # GitHub Actions workflow
├── static/
│   └── styles.css        # CSS styles
└── templates/
    ├── index.html        # Main page
    ├── settings.html     # Settings page
    └── analytics.html    # Analytics page
```

## Free Deployment Options

### Render (Recommended)
- **Free tier**: 750 hours/month
- **Features**: Auto-deploy, custom domains, SSL
- **Limitations**: Sleeps after 15 minutes of inactivity

### Other Free Options
- **Railway**: 500 hours/month free
- **Fly.io**: Limited free tier
- **Heroku**: No longer free
- **Vercel**: Good for static sites
- **Netlify**: Good for static sites

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure `GOOGLE_API_KEY` is set correctly
   - Check API key permissions in Google AI Studio

2. **Docker Build Fails**
   - Check Dockerfile syntax
   - Ensure all dependencies are in requirements.txt

3. **Render Deployment Fails**
   - Check environment variables
   - Verify Dockerfile path
   - Check build logs in Render dashboard

4. **Image Upload Issues**
   - Ensure file size limits
   - Check image format support

### Getting Help

- Check the [Render Documentation](https://render.com/docs)
- Review [GitHub Actions Documentation](https://docs.github.com/en/actions)
- Check [Flask Documentation](https://flask.palletsprojects.com/)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.
