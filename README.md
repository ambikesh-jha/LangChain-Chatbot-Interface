# LangChain Chatbot Interface

A lightweight Flask web application that provides a chat interface for interacting with Hugging Face's large language models through LangChain.

## Overview

This application serves as a simple yet powerful interface to Mistral-7B-Instruct, allowing users to ask questions and receive AI-generated responses. Built with Flask and LangChain, it demonstrates the integration of modern LLMs into web applications.

## Features

- **Interactive Chat Interface**: Clean web UI for conversing with the AI
- **Mistral-7B Integration**: Powered by the advanced Mistral-7B-Instruct model
- **LangChain Framework**: Leverages LangChain for streamlined LLM interactions
- **Configurable Parameters**: Adjustable temperature and response length
- **RESTful API**: Simple API endpoint for programmatic access

## Tech Stack

- **Backend**: Python Flask
- **LLM Framework**: LangChain
- **AI Model**: Mistral-7B-Instruct-v0.2 (via Hugging Face)
- **Frontend**: HTML, CSS, JavaScript (custom)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install flask langchain langchain-huggingface python-dotenv
