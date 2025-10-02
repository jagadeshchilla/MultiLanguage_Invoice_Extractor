# 📄 Invoice Extractor - AI-Powered Document Analysis

A modern Flask web application that uses Google's Generative AI (Gemini) to extract and analyze data from invoice images. Built with Docker, CI/CD, and deployed on Render.

## ✨ Features

- 🔍 **AI-Powered Analysis**: Uses Google's Gemini models for intelligent invoice data extraction
- 📱 **Responsive Design**: Modern, mobile-friendly interface
- 🚀 **Quick Actions**: Pre-defined questions for common invoice queries
- ⚙️ **Model Selection**: Choose from different Gemini models based on your needs
- 📊 **Analytics Dashboard**: Track processing times and success rates
- 🔐 **Secure API Key Management**: Safe storage and testing of API keys
- 🐳 **Docker Support**: Containerized for easy deployment
- 🔄 **CI/CD Pipeline**: Automated testing and deployment with GitHub Actions

## 🛠️ Tech Stack

- **Backend**: Flask (Python 3.10)
- **AI**: Google Generative AI (Gemini models)
- **Frontend**: HTML5, CSS3, JavaScript
- **Containerization**: Docker & Docker Compose
- **CI/CD**: GitHub Actions
- **Deployment**: Render
- **Security**: Environment variables, secure headers

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Docker & Docker Compose (optional)
- Google API Key ([Get one here](https://makersuite.google.com/app/apikey))

### Local Development

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd invoice-extractor
   ```

2. **Set up environment**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Edit .env and add your Google API key
   GOOGLE_API_KEY=your_google_api_key_here
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

   Visit `http://localhost:5000` to see the application.

### Docker Development

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Or build and run with Docker**
   ```bash
   # Build the image
   docker build -t invoice-extractor .
   
   # Run the container
   docker run -p 5000:5000 --env-file .env invoice-extractor
   ```

## 🌐 Deployment on Render

### Method 1: Direct GitHub Integration (Recommended)

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit with Docker and CI/CD setup"
   git push origin main
   ```

2. **Connect to Render**
   - Go to [Render Dashboard](https://dashboard.render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository and branch

3. **Configure deployment**
   - **Name**: `invoice-extractor`
   - **Environment**: `Docker`
   - **Dockerfile Path**: `./Dockerfile`
   - **Docker Context**: `.`
   - **Plan**: Free

4. **Set environment variables**
   - `GOOGLE_API_KEY`: Your Google API key
   - `FLASK_ENV`: `production`
   - `SECRET_KEY`: Generate a secure secret key

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your application

### Method 2: Using render.yaml (Advanced)

The project includes a `render.yaml` file for advanced configuration:

```yaml
services:
  - type: web
    name: invoice-extractor
    env: docker
    dockerfilePath: ./Dockerfile
    dockerContext: .
    plan: free
    region: oregon
    branch: main
    # ... additional configuration
```

## 🔄 CI/CD Pipeline

The project includes a comprehensive GitHub Actions workflow (`.github/workflows/ci-cd.yml`) that:

### Features
- ✅ **Automated Testing**: Runs pytest and flake8 on every PR
- 🐳 **Docker Build**: Builds and pushes Docker images to GitHub Container Registry
- 🔒 **Security Scanning**: Uses Trivy for vulnerability scanning
- 📊 **Code Coverage**: Generates and uploads coverage reports
- 🚀 **Auto Deployment**: Deploys to Render on main branch pushes

### Workflow Steps
1. **Test**: Lint, test, and generate coverage reports
2. **Build**: Create Docker image and push to registry
3. **Deploy**: Automatically deploy to Render
4. **Security**: Scan for vulnerabilities

### Required Secrets
Add these secrets to your GitHub repository:

- `RENDER_SERVICE_ID`: Your Render service ID
- `RENDER_API_KEY`: Your Render API key

## 📁 Project Structure

```
invoice-extractor/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # GitHub Actions CI/CD pipeline
├── static/
│   └── styles.css             # Application styles
├── templates/
│   ├── index.html             # Main application page
│   ├── analytics.html         # Analytics dashboard
│   └── settings.html          # Settings page
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker configuration
├── docker-compose.yml         # Docker Compose for development
├── render.yaml               # Render deployment configuration
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `GOOGLE_API_KEY` | Google Generative AI API key | Yes | - |
| `FLASK_ENV` | Flask environment | No | `development` |
| `SECRET_KEY` | Flask secret key | Yes | - |
| `MAX_CONTENT_LENGTH` | Max file upload size | No | `10485760` (10MB) |

### Supported AI Models

- **Gemma 3 27B IT** (Recommended): Best accuracy
- **Gemma 3 12B IT** (Balanced): Good balance of speed and accuracy
- **Gemma 3 4B IT** (Fast): Fastest processing
- **Gemini 2.0 Flash** (Experimental): Latest features
- **Gemini 2.5 Flash** (Preview): Preview features

## 🧪 Testing

```bash
# Install test dependencies
pip install pytest pytest-cov flake8

# Run tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run linting
flake8 .
```

## 📊 Monitoring & Analytics

The application includes built-in analytics tracking:
- Processing times
- Success rates
- Confidence scores
- Usage statistics

Access analytics at `/analytics` endpoint.

## 🔒 Security Features

- Environment variable protection
- Secure session management
- File upload validation
- Security headers (HSTS, XSS protection, etc.)
- Non-root Docker user
- Vulnerability scanning in CI/CD

## 🐛 Troubleshooting

### Common Issues

1. **API Key Not Working**
   - Verify your Google API key is correct
   - Check if the API key has proper permissions
   - Ensure billing is enabled for your Google Cloud project

2. **Docker Build Fails**
   - Check if all dependencies are in `requirements.txt`
   - Verify Dockerfile syntax
   - Ensure proper file permissions

3. **Render Deployment Issues**
   - Check environment variables are set correctly
   - Verify Dockerfile path in Render settings
   - Check Render logs for specific error messages

### Getting Help

- Check the [Issues](https://github.com/your-username/invoice-extractor/issues) page
- Review Render deployment logs
- Check GitHub Actions workflow logs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Google Generative AI](https://ai.google.dev/) for the AI models
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Render](https://render.com/) for hosting
- [GitHub Actions](https://github.com/features/actions) for CI/CD

---

**Made with ❤️ for efficient invoice processing**
