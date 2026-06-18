gentic Real Estate AI

An end-to-end Agentic AI system for automatic real-estate listing generation using FastAPI, React, LangGraph, Ollama, and Machine Learning.

The system accepts property images, detects room types, extracts features, predicts property price, generates descriptions, creates marketing posters, verifies the owner, publishes listing, and handles buyer enquiries automatically.

---

 Features

- Image Classification 
- Feature Extraction 
- Price Prediction 
- Description Generation  (Ollama Llama 3.2)
- AI Poster Generation 
- Owner Verification 
- Property Listing 
- Buyer Notification 
- Download Poster
- Accept / Reject Poster
- Buyer Interest Form (Buy/Rent)
- FastAPI Backend
- React Frontend
- LangGraph

  Tech Stack

## Backend

- FastAPI
- LangGraph
- SQLAlchemy
- SQLite
- Scikit-Learn
- TensorFlow/Keras
- Ollama
- Pillow

## Frontend

- React
- Vite
- Axios

  AI Models

### Image Classification

Mobilenet

### Description Generator

Llama 3.2 (Ollama)

### Poster Generator

Stable Diffusion 

### Price Prediction
Regression Model


# 📂 Project Structure

```text
backend
│
├── agents
│      classifier_agent.py
│      feature_agent.py
│      price_agent.py
│      description_agent.py
│      poster_agent.py
│      owner_verification_agent.py
│      listing_agent.py
│      buyer_notification_agent.py
│
├── graph
│      realestate_graph.py
│      state.py
│
├── routes
│      property_routes.py
│      pipeline_routes.py
│      interest_routes.py
│
├── services
│      poster_generator.py
│      property_pipeline.py
│
├── database
│
├── posters
│
└── main.py


frontend
│
├── pages
│      Home.jsx
│
├── services
│      api.js
│
└── App.jsx
