# 🎫 AI-Powered Ticket Classification System

## Overview
This project is an **end-to-end AI-enabled backend application** designed to automatically classify and prioritize enterprise support tickets. It demonstrates how traditional machine learning models can be **integrated into a production-style backend** and exposed through clean, usable APIs.

The system takes a free-text support ticket description as input, predicts the **responsible department** and **priority level**, stores the result in a database, and serves it to a frontend interface.

This project was built to showcase **backend engineering + applied machine learning**, with emphasis on API design, ML model integration, and system-level thinking.

---

## Key Features
- REST APIs built with **FastAPI**
- Machine Learning–based **ticket classification and prioritization*
*
- **Ensemble models** for improved prediction stability
- End-to-end flow: **API → ML inference → database → frontend**
- Modular project structure suitable for extension

---

## System Architecture

**High-level flow:**
1. User submits a ticket description via API or frontend
2. Text is preprocessed and passed to trained ML pipelines
3. Models predict:
   - Target department
   - Ticket priority
4. Results are stored in a relational database
5. Response is returned to the client

The ML models are loaded once at application startup and reused for inference, avoiding unnecessary overhead per request.

---

## Machine Learning Approach

### Problem Formulation
- **Task 1:** Multi-class text classification (Department prediction)
- **Task 2:** Multi-class text classification (Priority prediction)

### Model Design
Both tasks use an **ensemble learning approach** implemented via `VotingClassifier`:
- Random Forest Classifier
- Support Vector Machine (linear kernel)
- Multi-Layer Perceptron (Neural Network)

The models are combined using **hard voting**, where the final prediction is based on majority consensus.

### Text Processing
- Text normalization and cleaning
- TF-IDF vectorization (`max_features=5000`, English stop words)
- Pipelines ensure identical preprocessing during training and inference

### Model Persistence
- Trained pipelines are serialized using **joblib**
- Models are loaded at API startup for efficient reuse

---

## Backend Implementation

### Technology Stack
- **FastAPI** – REST API framework
- **SQLAlchemy** – ORM for database operations
- **Scikit-learn** – Machine learning models and pipelines
- **Joblib** – Model serialization

### API Endpoint

`POST /predict_ticket/`

**Input:**
- Ticket description (text)

**Output:**
- Ticket ID
- Predicted department
- Predicted priority

The endpoint performs input cleaning, ML inference, database persistence, and response generation in a single request flow.

---

## Frontend
A simple frontend interface is served using FastAPI’s static file support, allowing users to submit ticket descriptions and view predictions without external tools.

---

## Project Structure

```
ai-ticketing-system/
├── app/
│   ├── main.py          # FastAPI application
│   ├── models.py        # Database models
│   ├── schemas.py       # API request/response schemas
│   ├── database.py      # Database configuration
│
├── ml/
│   ├── train_models.py  # ML training pipeline
│   ├── large_ticket_dataset.csv
│
├── models/
│   ├── ticket_pipeline.joblib
│   ├── priority_pipeline.joblib
│
├── static/
│   ├── index.html
│
└── README.md
```

---

## What This Project Demonstrates
- Deploying ML models **outside notebooks** into real backend services
- Designing APIs that safely expose ML functionality
- Using ML pipelines for consistent preprocessing and inference
- Thinking beyond model accuracy toward **system integration**

---

## Limitations & Future Improvements
This project is a prototype intended for learning and demonstration purposes. Possible enhancements include:
- Background inference using task queues for high-load scenarios
- Model monitoring and retraining pipelines
- Shared preprocessing modules to avoid duplication
- Authentication and role-based access control
- Containerized deployment with Docker

---

## Author
**Ankit Chaudhary**  
Final-year ECE student, NIT Mizoram  
Interest areas: Generative AI Backend systems, API development, applied machine learning

---

## License
This project is for educational and demonstration purposes.
