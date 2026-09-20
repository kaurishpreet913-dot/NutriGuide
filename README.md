# NutriGuide — AI Nutrition Chatbot

## Overview

**NutriGuide** is an AI-powered nutrition chatbot designed to provide real-time responses to nutrition and dietary queries.

The application uses the **Google Gemini API** to generate AI-powered responses through a responsive web interface. It was independently developed from design to deployment, combining a frontend built with HTML, CSS, and JavaScript with a generative AI backend.

## Features

* 🤖 AI-powered nutrition and dietary chatbot
* 💬 Real-time responses to user queries
* 🧠 Generative AI powered by the Google Gemini API
* ✨ Prompt engineering for improved AI responses
* ⚡ Streamed AI responses for a responsive chat experience
* 🌐 Responsive web interface
* 🔑 API key integration and management
* 🎨 User-friendly chatbot interface

## How It Works

NutriGuide follows a simple interaction flow:

```text
User enters nutrition query
          ↓
Web Interface
          ↓
Google Gemini API
          ↓
Prompt Processing
          ↓
AI-generated Response
          ↓
Streamed Response
          ↓
User
```

The user's nutrition or dietary question is sent through the application to the Gemini API. The configured prompt is used to guide the AI's response, which is then streamed back to the user through the chatbot interface.

## Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Generative AI

* Google Gemini API
* Prompt Engineering
* Large Language Model (LLM) integration

### Development

* API Integration
* API Key Management
* Streamed AI Responses
* Responsive Web Design

## Generative AI Integration

NutriGuide integrates the **Google Gemini API** to generate responses to user-provided nutrition and dietary questions.

The project demonstrates an end-to-end generative AI workflow, including:

1. Receiving user input
2. Constructing and managing prompts
3. Sending requests to the Gemini API
4. Processing the generated response
5. Streaming the response back to the user interface

## User Interface

The application provides a responsive web-based chatbot interface where users can enter nutrition and dietary questions and receive AI-generated responses.

The frontend is developed using:

```text
HTML
CSS
JavaScript
```

The interface is designed to provide a simple and interactive conversational experience.

## API Key Management

The application requires a **Google Gemini API key** to communicate with the Gemini API.

For security reasons, API keys should **never be committed directly to a public GitHub repository**.

Before uploading the project to GitHub, make sure your actual API key has been removed from the source code.

For example, do not upload:

```javascript
const API_KEY = "YOUR_ACTUAL_API_KEY";
```

Instead, use a secure configuration approach appropriate for your deployment environment.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/NutriGuide.git
```

### 2. Open the project

Open the project folder in a code editor such as **Visual Studio Code**.

### 3. Configure the Gemini API

Create/configure your Gemini API credentials according to the method used by the application.

**Do not expose your actual API key in the GitHub repository.**

### 4. Run the application

Open the main HTML file in a browser or run the project using a local development server, depending on your project structure.

## Project Structure

```text
NutriGuide/
│
├── index.html        # Main chatbot interface
├── style.css         # Application styling
├── script.js         # Chatbot logic and Gemini API integration
└── README.md         # Project documentation
```

> **Note:** Update the file names above if your actual project uses different filenames.

## Project Highlights

* Independently designed and developed an AI-powered nutrition chatbot
* Integrated the Google Gemini API for real-time generative AI responses
* Implemented prompt engineering to guide chatbot responses
* Built a responsive HTML/CSS/JavaScript interface
* Implemented streamed AI responses for an interactive user experience
* Managed API integration and authentication requirements
* Developed the application end-to-end from design to deployment

## Future Improvements

Potential improvements include:

* User authentication
* Conversation history
* Personalized nutrition profiles
* Improved prompt and response controls
* Nutrition information storage
* Backend-based API key protection
* Deployment as a production web application

## Disclaimer

NutriGuide is an AI-powered informational tool and should not be considered a replacement for professional medical or nutritional advice. Users should consult qualified healthcare or nutrition professionals for personalized dietary guidance.

