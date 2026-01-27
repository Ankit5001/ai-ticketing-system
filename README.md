# 🎫 SmartDesk: AI-Powered Enterprise Ticketing System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-Ensemble-orange?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

**SmartDesk** is an intelligent IT support automation platform.  
It uses a **Multi-Model Ensemble AI** to classify support tickets and assign urgency levels in real time.

---

## 🚀 Key Features

- **🧠 Dual-Brain Architecture**
  - Department Classifier (HR, IT, Billing, Access)
  - Priority Scorer (Low / Medium / High)

- **🤖 Ensemble Learning**
  - Random Forest
  - Support Vector Machine
  - Neural Network (MLP)

- **⚡ High-Performance Backend**
  - FastAPI with async inference

- **🎨 Dashboard**
  - HTML, CSS, JavaScript frontend

- **💾 Persistence**
  - PostgreSQL with SQLAlchemy ORM

---

## 🛠️ Tech Stack

| Component | Technology |
|---------|------------|
| AI / ML | Scikit-Learn, Pandas |
| Backend | Python, FastAPI |
| Database | PostgreSQL |
| Frontend | HTML, CSS, JS |
| Server | Uvicorn |

---

## 📂 Project Structure

```text
AI-TICKETING-SYSTEM/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   └── schemas.py
├── ml_training/
│   ├── train_ensemble.py
│   └── large_ticket_dataset.csv
├── models/
│   ├── ticket_pipeline.joblib
│   └── priority_pipeline.joblib
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── requirements.txt
```

---

## ⚡ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-ticketing-system.git
cd ai-ticketing-system
```

### 2. Create Virtual Environment

```bash
python -m venv myenv
```

Activate:

- Windows: `myenv\Scripts\activate`
- Linux/Mac: `source myenv/bin/activate`

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

```sql
CREATE DATABASE ticket_db;
```

---

## 🧠 Train Models

```bash
python ml_training/train_ensemble.py
```

---

## ▶ Run Application

```bash
uvicorn app.main:app --reload
```

- UI: http://127.0.0.1:8000  
- API Docs: http://127.0.0.1:8000/docs  

---

## 📄 License

MIT License
