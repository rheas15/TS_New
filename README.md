# SummarEase: A Text Summarization App

## Overview
SummarEase is a web application that allows users to generate summaries from input text. It leverages the PEGASUS Transformer model from the Hugging Face library  to condense lengthy text documents into concise summaries, enabling users to extract key information quickly and efficiently.

## Features
- **Input Text**: Users can input text into the application through a user-friendly interface.
- **Summarization**: The application generates abstractive summaries of the input text.
- **Multiple Formats**: Summaries can be presented in bullet point format or paragraph format, based on user preference.
- **Thompson Sampling**: The application uses constant A/B Testing with Thompson Sampling to determine the default summary format based on users' behaviour.

## Technologies Used
- **Python**: Backend development.
- **Streamlit**: Web application framework for building the user interface.
- **Amazon ECR (Elastic Container Registry)**: Managed Docker container registry for storing, managing, and deploying Docker container images.
- **Amazon EC2**: Cloud hosting service for deploying the application.
- **GitHub Actions**: Continuous integration and continuous deployment (CI/CD) pipeline for automating the build and deployment process.

## CI/CD Pipeline
The project utilizes a CI/CD pipeline for automating the build and deployment process. GitHub Actions is configured to trigger builds upon code changes in the main branch. The pipeline includes building Docker images, pushing them to Amazon Elastic Container Registry, pulling them into EC2 and deploying the application.

## Dockerization
The application is Dockerized to encapsulate the entire environment and dependencies required to run the application. Docker containers provide consistency and portability, allowing the application to run reliably across different environments.

## Deployment
The application is deployed on Amazon EC2, leveraging its scalable compute capacity and infrastructure-as-a-service (IaaS) capabilities. EC2 instances host the Docker containers, providing a flexible and scalable deployment solution.


