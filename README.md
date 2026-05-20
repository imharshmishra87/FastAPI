# 🚀 FastAPI Complete Implementation Guide

A comprehensive learning repository featuring detailed implementations of FastAPI framework and its associated libraries including Pydantic, SQLAlchemy, Streamlit, and practical real-world API projects.

## 📋 Overview

This repository demonstrates professional FastAPI development with focus on:
- Building production-ready REST APIs
- Data validation with Pydantic models
- Database integration and ORM
- Web UI development with Streamlit
- Real-world project implementations

Perfect for backend developers, API designers, and full-stack developers learning FastAPI best practices.

---

## 🌟 Project 1: Pydantic - Data Validation & Serialization

### Overview
Learn the power of Pydantic for data validation, serialization, and documentation.

### 📚 Topics Covered

#### Basic Validation
- **`basic_validation.py`** - Type checking and validation
  - String, Integer, Float validation
  - Boolean and DateTime types
  - List and Dictionary validation
  - Required vs Optional fields
  - Default values

#### Nested Models
- **`nested_models.py`** - Complex data structures
  - Nested Pydantic models
  - List of models
  - Recursive models
  - Union types
  - Circular references

#### Custom Validators
- **`custom_validators.py`** - Advanced validation
  - Field-level validators
  - Root validators
  - Conditional validation
  - Cross-field validation
  - Error handling

#### Field Configuration
- **`fields_and_defaults.py`** - Advanced field features
  - Field descriptions
  - Min/max constraints
  - Regex patterns
  - Aliases
  - Private fields

#### Practical Examples
- **`examples.py`** - Real-world use cases
  - User registration validation
  - Email validation
  - Password requirements
  - Address validation
  - API request/response models

### 🚀 Quick Start - Pydantic

```python
from pydantic import BaseModel, Field, validator
from datetime import datetime

# Basic Model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int = Field(ge=0, le=150)  # Min 0, Max 150
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v

# Usage
user = User(id=1, name="John", email="john@example.com", age=25)
print(user)  # Validated!
```

### Key Concepts

**Type Validation:**
- Automatic type checking
- Type coercion where possible
- Error on invalid types

**Serialization:**
- `.dict()` - Convert to dictionary
- `.json()` - Convert to JSON string
- `.copy()` - Create deep copy

**Configuration:**
- `Config.extra = 'forbid'` - Don't allow extra fields
- `Config.validate_assignment = True` - Validate on assignment

---

## 🌟 Project 2: ML API Design with Streamlit

### Overview
Build a complete machine learning API with a modern web frontend using FastAPI and Streamlit.

### 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│    Streamlit Web UI (Frontend)          │
│  (Interactive, Real-time predictions)   │
└──────────────┬──────────────────────────┘
               │ HTTP Requests
┌──────────────▼──────────────────────────┐
│    FastAPI Backend (API Server)         │
│  - Data validation (Pydantic)           │
│  - ML model inference                   │
│  - Error handling                       │
└──────────────┬──────────────────────────┘
               │
┌──────────────▼──────────────────────────┐
│    Machine Learning Models              │
│  - Scikit-learn                         │
│  - TensorFlow/Keras                     │
│  - Custom models                        │
└─────────────────────────────────────────┘
```

### 📂 Components

#### FastAPI Backend (`main.py`)
- **REST Endpoints**
  - `POST /predict` - Make predictions
  - `GET /models` - List available models
  - `POST /train` - Train new models
  - `GET /health` - Health check

- **Features**
  - Input validation with Pydantic
  - Error handling and logging
  - CORS support for frontend
  - API documentation (Swagger UI)

#### Streamlit Frontend (`streamlit_app.py`)
- **Interactive UI**
  - File upload for data
  - Real-time predictions
  - Visualization of results
  - Model performance metrics
  - Training interface

- **Components**
  - Input forms
  - Data preview
  - Results display
  - Charts and graphs
  - Download predictions

#### Pydantic Schemas (`schemas.py`)
```python
from pydantic import BaseModel, Field
from typing import List, Optional

class PredictionInput(BaseModel):
    features: List[float] = Field(..., description="Input features")
    model_name: str = Field("default", description="Model to use")

class PredictionOutput(BaseModel):
    prediction: float
    confidence: float
    model_used: str
    timestamp: str
```

#### ML Models (`models.py`)
- Model loading and caching
- Inference function
- Model evaluation
- Batch predictions
- Feature preprocessing

### 🚀 Quick Start - ML API

**1. Install dependencies:**
```bash
cd ml_api_design_project_streamlit
pip install -r requirements.txt
```

**2. Run FastAPI backend:**
```bash
uvicorn main:app --reload
# API available at http://localhost:8000
# Docs at http://localhost:8000/docs
```

**3. Run Streamlit frontend (in another terminal):**
```bash
streamlit run streamlit_app.py
# UI available at http://localhost:8501
```

### 📊 Example Workflow

```python
# Backend prediction
@app.post("/predict")
async def predict(input_data: PredictionInput):
    # Validate input
    features = input_data.features
    
    # Load model
    model = load_model(input_data.model_name)
    
    # Make prediction
    prediction = model.predict([features])[0]
    
    # Return result
    return {
        "prediction": float(prediction),
        "confidence": 0.95,
        "model_used": input_data.model_name,
        "timestamp": datetime.now().isoformat()
    }
```

---

## 🌟 Project 3: Patient Management System

### Overview
A complete CRUD application demonstrating FastAPI with database integration, showing how to build production-ready applications.

### 🏗️ System Architecture

```
┌─────────────────────────────────────────────┐
│        HTTP Requests (REST API)             │
│  GET, POST, PUT, DELETE, PATCH              │
└──────────────┬──────────────────────────────┘
               │
┌──────────────▼──────────────────────────────┐
│     FastAPI Application (main.py)           │
│  - Route handlers                           │
│  - Error handling                           │
│  - Authentication (optional)                │
└──────────────┬──────────────────────────────┘
               │
┌──────────────▼──────────────────────────────┐
│    Pydantic Schemas (schemas.py)            │
│  - Input validation                         │
│  - Response models                          │
│  - Documentation                            │
└──────────────┬──────────────────────────────┘
               │
┌──────────────▼──────────────────────────────┐
│    Business Logic (crud.py)                 │
│  - Database operations                      │
│  - Business rules                           │
│  - Data transformation                      │
└──────────────┬──────────────────────────────┘
               │
┌──────────────▼──────────────────────────────┐
│  SQLAlchemy ORM (models.py)                 │
│  - Patient model                            │
│  - Appointment model                        │
│  - Medical records                          │
└──────────────┬──────────────────────────────┘
               │
┌──────────────▼──────────────────────────────┐
│    Database (SQLite/PostgreSQL)             │
│  - Persistent storage                       │
│  - Transactions                             │
└─────────────────────────────────────────────┘
```

### 📊 API Endpoints Summary

| Method | Endpoint | Purpose |
|--------|----------|---------|
| **POST** | `/patients/` | Create new patient |
| **GET** | `/patients/` | List all patients |
| **GET** | `/patients/{id}` | Get patient by ID |
| **PUT** | `/patients/{id}` | Update patient |
| **DELETE** | `/patients/{id}` | Delete patient |
| **GET** | `/health` | Health check |

### 🚀 Quick Start - Patient Project

```bash
cd patient_project

# Install dependencies
pip install -r requirements.txt

# Run application
uvicorn main:app --reload

# Access API
# http://localhost:8000/docs  (Swagger UI)
# http://localhost:8000/redoc (ReDoc)
```

---

## 🚀 Installation & Setup (All Projects)

### Prerequisites
```
- Python 3.8+
- pip or conda
- Virtual environment (recommended)
```

### Global Installation

1. **Clone repository:**
   ```bash
   git clone https://github.com/imharshmishra87/FastAPI.git
   cd FastAPI
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run specific project:**
   ```bash
   # For Pydantic examples
   python pydantic/basic_validation.py
   
   # For ML API
   cd ml_api_design_project_streamlit
   uvicorn main:app --reload
   streamlit run streamlit_app.py  # In another terminal
   
   # For Patient project
   cd patient_project
   uvicorn main:app --reload
   ```

---

## 📚 FastAPI Core Concepts

### Routing & HTTP Methods

```python
from fastapi import FastAPI

app = FastAPI()

# GET request
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# POST request
@app.post("/items/")
def create_item(item: Item):
    return item

# PUT request
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# DELETE request
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}
```

### Path Parameters, Query Parameters, Request Body

```python
# Path parameter
@app.get("/users/{user_id}")
def get_user(user_id: int):  # Path parameter
    pass

# Query parameters
@app.get("/items/")
def list_items(skip: int = 0, limit: int = 10):  # Query parameters
    pass

# Request body
@app.post("/items/")
def create_item(item: Item):  # Request body
    pass

# All combined
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item, q: str = None):
    pass
```

### Dependency Injection

```python
from fastapi import Depends

# Define dependency
def get_current_user(token: str):
    return {"user_id": 1, "username": "john"}

# Use dependency
@app.get("/items/")
def get_items(current_user = Depends(get_current_user)):
    return {"owner": current_user["username"]}
```

### Error Handling

```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]
```

### CORS Support

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 🎓 Learning Path

### Beginner Level (Days 1-3)
1. **Pydantic Basics**
   - Basic type validation
   - Required vs optional fields
   - Default values
   - Type coercion

2. **FastAPI Fundamentals**
   - Create first API
   - Path parameters
   - Query parameters
   - Request body

### Intermediate Level (Days 4-7)
1. **Advanced Pydantic**
   - Nested models
   - Custom validators
   - Field constraints
   - Complex types

2. **FastAPI Features**
   - Dependency injection
   - Error handling
   - Response models
   - Status codes

### Advanced Level (Days 8-14)
1. **Database Integration**
   - SQLAlchemy ORM
   - Database migrations
   - Relationships
   - Transactions

2. **Full Projects**
   - Patient management system
   - ML API with frontend
   - Authentication
   - Production deployment

---

## 🌐 API Documentation

FastAPI automatically generates interactive API documentation:

- **Swagger UI** - Available at `/docs`
  - Try out endpoints
  - View request/response examples
  - Check parameter types

- **ReDoc** - Available at `/redoc`
  - Alternative documentation
  - Better for reading
  - Clean organization

- **OpenAPI Schema** - Available at `/openapi.json`
  - Machine-readable spec
  - For code generation
  - Integration with other tools

---

## 🔒 Security Best Practices

### Input Validation
```python
from pydantic import BaseModel, Field, validator

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8)
    email: EmailStr
    
    @validator('username')
    def username_alphanumeric(cls, v):
        if not v.replace('_', '').isalnum():
            raise ValueError('Username must be alphanumeric')
        return v
```

### Authentication
```python
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthCredentials

security = HTTPBearer()

@app.get("/protected/")
def protected_route(credentials: HTTPAuthCredentials = Depends(security)):
    if not verify_token(credentials.credentials):
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"status": "authenticated"}
```

### CORS Configuration
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],  # Specific origins
    allow_methods=["GET", "POST"],
    allow_headers=["Authorization"],
)
```

---

## 📊 Performance Tips

1. **Async Operations**
   ```python
   @app.get("/items/")
   async def list_items():  # Use async
       return await get_items_from_db()
   ```

2. **Caching**
   ```python
   from functools import lru_cache
   
   @lru_cache(maxsize=100)
   def expensive_function(param):
       return result
   ```

3. **Pagination**
   ```python
   @app.get("/items/")
   def list_items(skip: int = 0, limit: int = 10):
       return items[skip:skip+limit]
   ```

4. **Batch Operations**
   ```python
   @app.post("/items/batch")
   def create_items(items: List[Item]):
       return [create_item(item) for item in items]
   ```

---

## 🧪 Testing FastAPI Applications

```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_create_patient():
    response = client.post(
        "/patients/",
        json={"name": "John", "email": "john@example.com"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "John"

def test_get_patient():
    response = client.get("/patients/1")
    assert response.status_code == 200
```

---

## 🔧 Technologies Overview

### FastAPI
- **Speed:** Comparable to Node.js and Go (top performance)
- **Async:** Built-in async/await support
- **Validation:** Automatic request validation with Pydantic
- **Documentation:** Auto-generated interactive docs
- **Testing:** Built-in testing utilities

### Pydantic
- **Validation:** Runtime type checking
- **Serialization:** Easy data conversion (dict, JSON)
- **Documentation:** Automatic schema generation
- **Performance:** Optimized C implementation

### SQLAlchemy
- **ORM:** Object-relational mapping
- **Databases:** Support for multiple databases
- **Relationships:** Define complex data relationships
- **Migrations:** Alembic integration for schema changes

### Streamlit
- **UI Building:** Create web apps with Python
- **Interactivity:** Buttons, sliders, file uploads
- **Real-time:** Hot reload for development
- **Deployment:** Easy deployment to Streamlit Cloud

---

## 📈 Real-World Applications

✅ **Microservices** - Build microservices architecture  
✅ **REST APIs** - Complete REST API development  
✅ **Data APIs** - Serve machine learning models  
✅ **Internal Tools** - Backend for admin panels  
✅ **Real-time Apps** - WebSocket support  
✅ **Serverless** - Deploy to AWS Lambda, Google Cloud  

---

## 🚀 Deployment Options

### 1. Local Server
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 2. Production ASGI Server
```bash
pip install gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### 3. Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
```

### 4. Streamlit Cloud
```bash
streamlit run app.py --logger.level=debug
# Deploy via: https://share.streamlit.io/
```

---

## 📚 Additional Resources

### Official Documentation
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Streamlit Docs](https://docs.streamlit.io/)

### Tutorials & Courses
- FastAPI official tutorial (in docs)
- Real Python FastAPI articles
- Miguel Grinberg's Flask-to-FastAPI migration
- YouTube tutorials and courses

### Community
- FastAPI GitHub discussions
- Stack Overflow [fastapi] tag
- Pydantic GitHub discussions
- Streamlit community forums

---

## 🤝 Contributing

This is a learning repository. Improvements welcome!
- Add more Pydantic examples
- Create additional projects
- Improve documentation
- Add test cases
- Share your learnings

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file.

---

## 📊 Project Statistics

- **Total Projects:** 3 (Pydantic, ML API, Patient System)
- **Code Files:** 15+
- **Lines of Code:** 2000+
- **Dependencies:** FastAPI, Pydantic, SQLAlchemy, Streamlit
- **Database Support:** SQLite, PostgreSQL, MySQL

---

## 🎯 Key Takeaways

✨ **Pydantic Power** - Type validation simplifies code  
✨ **FastAPI Speed** - Performance-first framework  
✨ **Easy Integration** - Works with databases, ML models  
✨ **Auto Documentation** - Interactive API docs  
✨ **Scalable Design** - From prototype to production  
✨ **Modern Python** - Uses latest Python features  

---

## 💬 FAQ

**Q: Should I use FastAPI or Flask?**  
A: FastAPI is faster and more modern. Use FastAPI for new projects.

**Q: Can I use FastAPI without Pydantic?**  
A: Technically yes, but you lose validation. Not recommended.

**Q: How do I connect to a database?**  
A: Use SQLAlchemy ORM (see patient_project for example).

**Q: Can FastAPI handle WebSockets?**  
A: Yes, built-in support via `@app.websocket()`.

**Q: Is FastAPI production-ready?**  
A: Absolutely. Used by major companies in production.

---

## 📞 Getting Help

- Check project README files
- Review FastAPI official docs
- Search Stack Overflow
- Ask in FastAPI discussions
- Share issues on GitHub

---

**Last Updated:** May 2026  
**Status:** ✅ Complete Learning Repository  
**Contributions:** Welcome!  

⭐ **If this helps your FastAPI learning, please star this repository!**

---

**Happy API Building! 🚀**
