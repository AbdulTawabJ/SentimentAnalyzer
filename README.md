# SentimentAnalyzer - CLI App

A Sentiment Analysis Application built using Python and TextBlob, developed as part of HackOps 2025 to demonstrate professional DevOps practices including CI/CD, containerization, infrastructure automation, monitoring, testing, and security.

## 📜 Project Description

- Takes user input from the command line
- Analyzes sentiment (Positive, Negative, Neutral)
- Powered by the TextBlob natural language processing library

## 📂 Current Version (1.0)

- Basic CLI interface
- No GUI yet
- Simple output using TextBlob's polarity score

## ⚙️ How to Run Locally

```bash
python src/app.py
```

Make sure to install dependencies first:

```bash
pip install -r requirements.txt
```

## 🐳 Dockerization

We have containerized the CLI version of our Sentiment Analyzer app using Docker.

### How to Build and Run the Docker Container

```bash
# Build the Docker image
docker build -t sentiment-analyzer .

# Run the Docker container
docker run -it sentiment-analyzer
```

## 🔄 CI/CD Pipeline

A GitHub Actions CI pipeline is set up to:

- Checkout code
- Set up Python environment
- Install project dependencies
- Run automated unit tests
- Run application health check

The pipeline triggers on every push and pull request targeting the `main` branch.

## 🧪 Testing

Automated unit tests are written using Python's `unittest` framework to ensure:

- Positive sentiment is correctly detected
- Negative sentiment is correctly detected
- Neutral sentiment is correctly detected

Tests are automatically executed during the CI pipeline using `pytest`.

## 🛠️ Upcoming Enhancements

- Develop a GUI version of the application (using Tkinter or Flask)
- Deploy the Dockerized application to a cloud server
- Add Infrastructure as Code for automated server setup
- Integrate monitoring and health checks
- Implement security scanning and vulnerability checks
- Full Continuous Deployment (CD) setup after successful CI