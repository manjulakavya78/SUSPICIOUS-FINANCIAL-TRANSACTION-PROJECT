http://127.0.0.1:8000/
# 🛡️ Suspicious Financial Transaction Detection Using Autoencoder & Risk-Based Approach

## 🌟 Overview

Financial fraud and money laundering have become increasingly sophisticated with the rise of digital banking and online financial services. This project presents an **Autoencoder-based Deep Learning model** combined with a **Risk-Based Approach (RBA)** to identify suspicious financial transactions. The model learns normal transaction behavior using unsupervised learning and detects anomalies through reconstruction error, enabling efficient fraud detection without requiring labeled fraudulent data.

---

## 📊 Dataset

**Source:** Financial Transaction Dataset (Proof of Concept)

**Dataset Size:**

* Approximately **890,000** transaction records collected
* **60,000** preprocessed records used for model training

**Dataset Features:**

* Customer Information
* Account Information
* Transaction Information
* Transaction Amount
* Transaction Time
* Transaction Type
* Product Information
* Internal Control Indicators
* Risk-Based Features

---

## 🛠️ Technologies Used

**Programming Language:**

* Python

**Libraries & Frameworks:**

* TensorFlow
* Keras
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* MySQL

**Deep Learning Technique:**

* Autoencoder Neural Network

**Machine Learning Concepts:**

* Unsupervised Learning
* Anomaly Detection
* Risk-Based Approach (RBA)
* Feature Engineering
* Data Normalization
* Dropout Regularization

---

## 🔄 Project Workflow

### 📌 Data Preprocessing

* Remove duplicate records
* Handle missing values
* Normalize numerical features
* Perform feature engineering
* Prepare training and validation datasets

### 📌 Risk-Based Feature Engineering

* Analyze customer transaction behavior
* Generate transaction risk scores
* Incorporate internal control indicators
* Create meaningful financial features

### 📌 Model Development

* Build an Autoencoder Neural Network
* Learn normal transaction patterns
* Detect anomalies using reconstruction error
* Apply dropout to reduce overfitting

### 📌 Model Training & Evaluation

* Train using normal transaction data
* Validate using unseen transactions
* Detect suspicious activities based on anomaly threshold

### 📌 Performance Metrics

* Accuracy: **99.71%**
* ROC-AUC: **0.997**
* High Recall for detecting suspicious transactions
* Low reconstruction error for legitimate transactions

---




## 📈 Results & Insights

* Autoencoder successfully learns normal financial transaction behavior.
* Suspicious transactions are identified using reconstruction error.
* Risk-Based Approach improves anomaly detection by incorporating financial risk indicators.
* The model performs effectively without requiring labeled fraud data.
* Achieved **99.71% detection accuracy** with excellent anomaly detection capability.

---

## 🌐 Deployment

The trained model can be deployed using **Flask** to provide a REST API for real-time suspicious transaction detection.

Possible integrations include:

* Banking Systems
* Financial Monitoring Platforms
* Anti-Money Laundering (AML) Solutions
* Fraud Detection Dashboards

---

## 🔮 Future Improvements

* Implement Variational Autoencoders (VAE)
* Integrate LSTM Autoencoders for sequential transaction analysis
* Develop real-time fraud detection using Apache Kafka
* Add Explainable AI (XAI) techniques for model transparency
* Enhance risk scoring with geolocation and behavioral analytics

---

## 🤝 Contributions

Contributions are welcome!

Feel free to:

* Fork the repository
* Create feature branches
* Submit Pull Requests
* Report issues or suggest improvements

---



## 📬 Connect With Me

📧 Email:manjulakavya78@gmail.com

💼 LinkedIn: https://www.linkedin.com/in/kavya-manjula-0296852b9/

💻 GitHub:https://github.com/manjulakavya78
---

⭐ If you found this project useful, don't forget to **Star** the repository!

🚀 Happy Coding!
