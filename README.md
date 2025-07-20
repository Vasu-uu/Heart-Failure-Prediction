# Heart Failure Prediction Web Application

This project is a machine learning application that predicts the risk of heart failure in patients based on their clinical records. The predictive model is deployed as a web application using the Flask framework.

This project was created as part of the **Predictive Modelling Bootcamp** by **DevTown**.

---

## 🖥️ Application Interface

![UI Screenshot](Screenshots/s1.png)

---

## 🚀 Features

- **Predictive Model:** Utilizes a tuned `RandomForestClassifier` with an accuracy of **83.33%**.
- **Interactive UI:** A professional and responsive dark-themed user interface for entering patient data.
- **Flask Backend:** A lightweight backend to serve the model and handle predictions.

---

## 📊 Sample Outputs

Here are examples of the prediction results for both low-risk and high-risk cases.

| Low Risk Prediction                     | High Risk Prediction                     |
| --------------------------------------- | ---------------------------------------- |
| ![Low Risk Output](Screenshots/s2.png)   | ![High Risk Output](Screenshots/s3.png)   |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **ML/Data Science:** Pandas, Scikit-learn, NumPy  
- **Frontend:** HTML, CSS  

---

## ⚙️ How to Run the Project Locally

Follow these steps to get the application running on your local machine.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Vasu-uu/Heart-Failure-Prediction.git
cd Heart-Failure-Prediction

### 2️⃣ Create and Activate a Virtual Environment

**For macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

---

**For Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate

---


### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt


---

### 4️⃣ Run the Flask Application
```bash
python app.py


### 5️⃣ Access the Application  
Open your web browser and go to:  
http://127.0.0.1:5000

You should now see the web application running and can input data to get predictions.

---

## ✍️ Author

**Vasudev V**  
[https://github.com/Vasu-uu](https://github.com/Vasu-uu)