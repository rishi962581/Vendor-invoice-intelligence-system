# 📦 Vendor Invoice Intelligence Portal

An end-to-end Machine Learning application that helps finance teams automate invoice analysis through:

- 🚚 Freight Cost Prediction
- 🧾 Invoice Risk Detection
- 📊 Interactive Analytics Dashboard
- ⚡ Faster Invoice Approval Workflow

---

## 📌 Table of Contents

- [Project Overview](#project-overview)
- [Business Objectives](#business-objectives)
- [Data Sources](#data-sources)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Models Used](#models-used)
- [Evaluation Metrics](#evaluation-metrics)
- [Application](#application)
- [Project Structure](#project-structure)
- [How to Run This Project](#how-to-run-this-project)
- [Future Enhancements](#future-enhancements)

---

## 📌 Project Overview

This project implements an end-to-end machine learning solution for vendor invoice intelligence.

The system helps organizations:

1. Predict expected freight costs for vendor invoices.
2. Detect risky invoices requiring manual review.
3. Reduce financial leakage and fraud.
4. Improve operational efficiency.

---

## 🎯 Business Objectives

### 1. Freight Cost Prediction

Predict expected freight cost using:

- Invoice Quantity
- Invoice Amount
- Vendor Transaction Patterns

**Business Benefit:**
- Better budgeting
- Cost forecasting
- Vendor negotiation support

### 2. Invoice Risk Detection

Automatically identify invoices that may require manual approval based on:

- Cost anomalies
- Freight irregularities
- Operational inconsistencies

**Business Benefit:**
- Fraud detection
- Reduced manual effort
- Faster approvals

---

## 📂 Data Sources

The project uses:

### Purchases Table
- PO Number
- Brand
- Quantity
- Dollars
- PO Date
- Receiving Date

### Vendor Invoice Table
- PO Number
- Quantity
- Dollars
- Freight
- Invoice Date
- Pay Date

Database Source:

```text
inventory.db
```

---

## 📊 Exploratory Data Analysis

EDA includes:

- Missing Value Analysis
- Freight Cost Distribution
- Invoice Amount Distribution
- Correlation Analysis
- Outlier Detection
- Vendor-Level Insights

Libraries Used:

```python
pandas
numpy
matplotlib
seaborn
plotly
```

---

## 🤖 Models Used

### Freight Cost Prediction

Model:

```python
RandomForestRegressor
```

Purpose:

- Predict freight charges for new invoices

### Invoice Risk Prediction

Model:

```python
RandomForestClassifier
```

Purpose:

- Predict whether an invoice should be flagged for manual approval

---

## 📈 Evaluation Metrics

### Regression Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

### Classification Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Classification Report

---

## 🖥️ Application

Built using:

```python
Streamlit
```

Features:

### Freight Cost Prediction Module

Input:
- Quantity
- Invoice Dollars

Output:
- Estimated Freight Cost

### Invoice Risk Prediction Module

Input:
- Invoice Quantity
- Freight Cost
- Invoice Dollars
- Total Item Quantity
- Total Item Dollars

Output:
- Safe for Auto Approval
- Requires Manual Approval

---

## 📁 Project Structure

```text
Vendor-Invoice-Analytics/
│
├── data/
│   └── inventory.db
│
├── models/
│   ├── scaler.pkl
│   ├── predict_freight_model.pkl
│   └── predict_flag_invoice.pkl
│
├── inference/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
├── training/
│   ├── data_preprocessing.py
│   ├── modeling_evaluation.py
│   └── train_model.py
│
├── app/
│   └── streamlit_app.py
│
├── notebooks/
│
├── requirements.txt
│
└── README.md
```

---

## 🚀 How to Run This Project

### 1. Clone Repository

```bash
git clone <repository-url>
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train Models

```bash
python train_model.py
```

### 4. Launch Dashboard

```bash
streamlit run streamlit_app.py
```

---

## 💡 Future Enhancements

- XGBoost Models
- Real-Time Invoice Monitoring
- Automated Vendor Scoring
- Fraud Detection Dashboard
- Cloud Deployment (AWS/Azure)

---

## 👨‍💻 Author

**Rishikesh Yadav**

B.Tech Biotechnology Student  
NSUT Delhi

Interested in:
- Data Science
- Machine Learning
- Artificial Intelligence
- Analytics

---