# Sentiment Analyzer CLI App

A Sentiment Analysis Application built using Python and TextBlob, developed as part of HackOps 2025 to demonstrate professional DevOps practices including CI/CD, containerization, infrastructure automation, monitoring, and security.

## 📜 Project Description

- Takes user input from the command line
- Analyzes sentiment (Positive, Negative, Neutral)
- Powered by the TextBlob natural language processing library

## 📂 Current Version (1.0)

- Basic CLI interface
- No GUI
- Simple rule-based output using TextBlob's polarity score

## ⚙️ How to Run

```bash
python src/app.py

## 🐳 Dockerization

We have containerized the CLI version of our Sentiment Analyzer app using Docker.

### How to Build and Run the Docker Container

```bash
# Build the Docker image
docker build -t sentiment-analyzer .

# Run the Docker container
docker run -it sentiment-analyzer

