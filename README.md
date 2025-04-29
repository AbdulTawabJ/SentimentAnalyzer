# Sentiment Analyzer - Web App

A Flask-based web application for analyzing text sentiment (Positive, Negative, Neutral), built using Python and TextBlob. This project was developed for HackOps 2025, demonstrating a range of professional DevOps practices including CI/CD, containerization, cloud deployment, automated testing, security scanning, and monitoring.

## Project Description

This web application provides a user-friendly interface to:
- Input sentences or paragraphs of text.
- Receive an instant sentiment analysis (Positive, Negative, or Neutral).
- The analysis is powered by the TextBlob natural language processing library.

## Features

- Simple and clean web UI built with Flask and HTML/CSS.
- Real-time sentiment analysis using TextBlob's polarity score.
- Containerized with Docker for consistent deployment.
- Automated CI/CD pipeline for build, test, security scan, and deployment.
- Deployed as a serverless application on Google Cloud Run.

## Live Demo

You can access the deployed application here:
[https://sentiment-analyzer-service-492944601563.asia-southeast2.run.app/](https://sentiment-analyzer-service-492944601563.asia-southeast2.run.app/)

## Presentation and Report
You can view the presentation here:
https://www.canva.com/design/DAGmA30k_-w/VUXrQtxcvBSUu-cE5MVdVA/view?utm_content=DAGmA30k_-w&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h7e0e7e9326

You can view the report here:
https://docs.google.com/document/d/1RkmH9smANickX7Idti6UH-eTA8clzFwdUcdIdv0r0iI/edit?usp=sharing

## Technology Stack

- **Backend:** Python, Flask
- **NLP Library:** TextBlob
- **Frontend:** HTML, CSS (via Jinja2 Templates)
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Cloud Platform:** Google Cloud Platform (GCP)
- **Deployment:** GCP Cloud Run, GCP Artifact Registry
- **Testing:** Pytest
- **Security:** GCP Artifact Analysis (SAST), GitHub Secrets
- **Monitoring:** GCP Cloud Monitoring & Dashboards

##  DevOps Practices Implemented

This project incorporates several DevOps practices as required by HackOps 2025:
- **Version Control:** Git & GitHub for source code management and collaboration.
- **Containerization:** Application packaged as a Docker container.
- **CI/CD Pipeline:** Automated workflow using GitHub Actions for building the Docker image, running tests, performing security scans, pushing the image to Artifact Registry, and deploying to Cloud Run on pushes/PRs to `main`.
- **Automated Testing:** Unit tests using Pytest run automatically in the pipeline.
- **Security Integration:** SAST scanning via GCP Artifact Analysis integrated into the workflow; GCP credentials managed securely using GitHub Secrets.
- **Cloud Deployment:** Automated deployment to a scalable, serverless platform (GCP Cloud Run).
- **Monitoring:** Basic monitoring configured using Google Cloud Monitoring dashboards (tracking request count, latency, errors, and uptime checks).

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd SentimentAnalyzer
    ```
2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate # On Windows use `venv\Scripts\activate`
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Download TextBlob corpora (Needed on first run):**
    ```bash
    python -m textblob.download_corpora
    ```
5.  **Run the Flask application:**
    ```bash
    python src/app.py
    ```
6.  **Access the application:** Open your web browser and go to `http://localhost:8080`.

## Running with Docker Locally

1.  **Build the Docker image:**
    ```bash
    docker build -t sentiment-analyzer .
    ```
2.  **Run the Docker container:**
    ```bash
    # This maps port 8080 inside the container to port 8080 on your machine
    docker run -p 8080:8080 sentiment-analyzer
    ```
3.  **Access the application:** Open your web browser and go to `http://localhost:8080`.

## CI/CD Pipeline

A GitHub Actions workflow (`.github/workflows/your_pipeline.yaml`) is configured to automate the following on pushes and pull requests to the `main` branch:
1.  Check out source code.
2.  Set up Python environment.
3.  Install dependencies.
4.  Run automated tests (`pytest`).
5.  Build the Docker image.
6.  Authenticate to Google Cloud.
7.  Push the Docker image to Google Artifact Registry.
8.  (On push to main) Trigger Vulnerability Scanning via Artifact Analysis (SAST).
9.  (On push to main) Deploy the new image to Google Cloud Run.

## Testing

Automated unit tests using `pytest` are located in the `/tests` directory. These tests cover:
- Correct identification of Positive sentiment.
- Correct identification of Negative sentiment.
- Correct identification of Neutral sentiment.
- Basic API endpoint functionality (if applicable).

Tests are automatically executed as part of the CI/CD pipeline.

## Monitoring

The deployed application's health and performance are monitored using Google Cloud Monitoring. Key metrics tracked on the GCP dashboard include:
- Request Count & Latency
- Error Rates (HTTP 5xx)
- Container CPU and Memory Utilization
- Uptime Checks verifying service availability.