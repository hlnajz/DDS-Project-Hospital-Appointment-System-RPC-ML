<div align="center">

![UIZ Hospital RPC Service](https://img.shields.io/badge/UIZ_Hospital-RPC_Service-3776AB?style=for-the-badge&logo=python&logoColor=white)

# UIZ Hospital - RPC & Computational Service 🧮

### Distributed Systems Module Project

**Professor:** Pr. EL HABOUZ Youssef  
**Major:** IISE (Ingénierie Informatique et Systèmes Embarqués)
 
<p>
  <img src="https://img.shields.io/badge/Language-Python_3.x-3776AB?logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Framework-FastAPI-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Server-Uvicorn-4053D6?logo=gunicorn&logoColor=white" alt="Uvicorn" />
  <img src="https://img.shields.io/badge/Architecture-RPC_Microservice-orange" alt="Architecture" />
</p>

</div>

---

## 📖 About The RPC Service

This repository contains the **Computational Microservice** for the UIZ Hospital system. Unlike the main backend which handles CRUD operations, this service is dedicated to performing complex logic and heavy calculations—specifically for the **Assurance & Risk Analysis System**.

By offloading these tasks to a specialized Python environment via **Remote Procedure Calls (RPC)** over HTTP, we demonstrate a decoupled, polyglot architecture typical of modern distributed systems.

### ⚙️ Core Responsibilities

* **Risk Assessment Engine:** Analyzes patient data to calculate health risk scores.
* **Intelligent Recommendations:** Suggests specific insurance plans (Normal vs. Premium) based on calculated risk.
* **High-Performance API:** Built with **FastAPI** for asynchronous, high-speed processing.

---

## 🧠 Logic & Algorithms

The core of this service is the `assurance_logic` module, which processes patient demographics and lifestyle choices to generate financial and medical coverage estimates.

### Input Parameters
The service accepts a JSON payload with the following factors:
* **Age:** Determines base risk brackets (<25, <40, <60, 60+).
* **Gender:** Statistical risk adjustment.
* **Lifestyle:** Analyzes activity levels (`sedentary`, `average`, `active`).
* **Chronic Conditions:** Heavily weighted factor for risk calculation.

### Output Logic
Based on the computed **Risk Score (0-100)**, the system returns:
1.  **Suggested Plan:** `Normal` (Low/Medium Risk) or `Premium` (High Risk).
2.  **Coverage:** Percentage of hospital costs covered (50% or 100%).
3.  **Monthly Cost:** Calculated premium in currency.
4.  **Risk Breakdown:** Detailed analysis of contributing factors.

---

## 🛠️ Tech Stack

This microservice leverages the Python ecosystem for its computational strengths:

* **Framework:** `FastAPI` (Modern, fast web framework for building APIs).
* **Server:** `Uvicorn` (Lightning-fast ASGI server implementation).
* **Validation:** `Pydantic` (Data validation and settings management using Python type hints).
* **Utilities:** `Requests` (For any external HTTP calls).

---

## 🔌 API Endpoints

The service exposes endpoints under the `/rpc` prefix.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/rpc/assurance` | Receives patient data payload and returns the calculated assurance plan and risk analysis. |
| **GET** | `/docs` | Auto-generated interactive API documentation (Swagger UI). |

---

## 👥 The Team

This distributed component was engineered by the **IISE** team:

* **Hamza Labbaalli**
* **Abdoulouahed Id-boubrik**
* **Yassine Maarouf**
* **Nada Bermil**
* **Soumaya Iddaha**

---

## 🚀 Getting Started

Follow these steps to run the Python RPC service locally.

### 1. Prerequisites
* Python 3.8+ installed.

### 2. Installation
Clone the repository and install the required packages:

```bash
git clone [https://github.com/hlnajz/DDS-Project-Hospital-Appointment-System-RPC-ML.git](https://github.com/hlnajz/DDS-Project-Hospital-Appointment-System-RPC-ML.git)
cd uizhospital-rpc
pip install -r requirements.txt
```

### 3. Run the Service
You can start the server using the provided entry point:

````bash
python app/main.py
````
Alternatively, run with Uvicorn directly:

````bash
uvicorn app.main:app --reload
````

The service will run on http://localhost:8000 (or the port defined in your environment variables).

<div align="center"> <p>© 2025 UIZ Hospital Team. Distributed Systems Project.


<i>Powered by Python & FastAPI</i></p> </div>
