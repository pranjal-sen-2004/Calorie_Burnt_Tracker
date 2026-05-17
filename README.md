# 🔥 Gym Calories Burned Prediction 🏋️‍♂️

A complete end-to-end Machine Learning web application that predicts the number of calories burned during a workout session using fitness, biometric, and workout-related parameters.

The project is built using:

- Machine Learning
- Flask
- Scikit-Learn
- AWS Elastic Beanstalk
- AWS CodePipeline

and deployed on AWS Cloud with CI/CD integration.

---

# 🌐 Live Demo

🚀 **Deployed Application:**  
http://calorieburnttracker-env.eba-mgm99i6b.eu-north-1.elasticbeanstalk.com/

---

# 📌 Project Overview

This project predicts the estimated calories burned based on:

- Personal Information
- Heart Rate Metrics
- Workout Information
- Body Composition Metrics
- Fitness Experience

The application uses a trained Machine Learning regression model to generate real-time predictions through an interactive web interface.

---

# ✨ Features

✅ Modern Responsive UI  
✅ Real-Time Calories Prediction  
✅ Interactive Fitness Dashboard  
✅ BMI Auto Calculation  
✅ Error Handling & Validation  
✅ Machine Learning Pipeline Integration  
✅ AWS Elastic Beanstalk Deployment  
✅ AWS CodePipeline CI/CD Integration  
✅ Fully Responsive Design  
✅ Production Ready Flask Application  

---

# 🧠 Machine Learning Workflow

The project follows a complete ML lifecycle:

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Data Preprocessing
6. Model Training
7. Model Evaluation
8. Model Serialization
9. Flask Integration
10. Cloud Deployment

---

# 📊 Input Features

The model takes the following features as input:

| Feature | Description |
|---|---|
| Age | User age |
| Gender | Male / Female |
| Weight (kg) | Body weight |
| Height (m) | Height in meters |
| Max BPM | Maximum heart rate |
| Avg BPM | Average heart rate |
| Resting BPM | Resting heart rate |
| Session Duration | Workout duration |
| Workout Type | Cardio / Strength / HIIT / Yoga |
| Fat Percentage | Body fat percentage |
| Water Intake | Daily water intake |
| Workout Frequency | Weekly workout frequency |
| Experience Level | Fitness experience level |
| BMI | Body Mass Index |

---

# 🏗️ Project Architecture

```bash
Gym-Calorie-Predictor/
│
├── artifacts/
│   ├── model.pkl
│   └── preprocessor.pkl
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── notebooks/
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── static/
│
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── setup.py
└── README.md
```

---

# ⚙️ Tech Stack

## 💻 Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap

## 🧠 Backend
- Flask
- Python

## 🤖 Machine Learning
- Scikit-Learn
- Pandas
- NumPy

## ☁️ Cloud & DevOps
- AWS Elastic Beanstalk
- AWS CodePipeline
- GitHub

---

# 📈 Model Training

Multiple regression models were trained and evaluated, including:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor
- CatBoost Regressor
- AdaBoost Regressor

The best-performing model was selected based on:

- R² Score
- RMSE
- MAE

---

# 🚀 AWS Deployment

The application is fully deployed on AWS using:

- AWS Elastic Beanstalk
- AWS CodePipeline
- Amazon EC2
- Amazon S3
- AWS IAM

---

# 🔄 CI/CD Pipeline

This project includes a complete CI/CD workflow:

```text
GitHub Repository
        ↓
AWS CodePipeline
        ↓
Elastic Beanstalk Deployment
        ↓
Live Production Application
```

Every GitHub push automatically triggers deployment.

---

# 🧪 Running Locally

## 1️⃣ Clone Repository

```bash
git clone <your-github-repo-link>
cd Gym-Calorie-Predictor
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run Application

```bash
python app.py
```

---

## 5️⃣ Open Browser

```text
http://127.0.0.1:5000
```

---

# 📷 Application Screenshots

## 🏠 Home Page

- Modern landing page
- Fitness-themed UI
- Interactive navigation

## 📊 Prediction Page

- Multi-section smart form
- Real-time BMI calculation
- Animated prediction result card

---

# 📌 Future Improvements

- User Authentication
- Workout Recommendation System
- Fitness Analytics Dashboard
- Nutrition Recommendation Module
- MongoDB Integration
- Docker Deployment
- Kubernetes Scaling
- Mobile Application Version

---

# 📚 Learning Outcomes

This project demonstrates:

- End-to-End Machine Learning Pipeline
- Production Deployment
- Flask Web Development
- Cloud Deployment on AWS
- CI/CD Automation
- Model Serialization
- Feature Engineering
- Frontend + Backend Integration

---

# 👨‍💻 Author

## Pranjal Sen

Machine Learning & Software Engineering Enthusiast

---

# ⭐ If You Like This Project

Please consider giving this repository a ⭐ on GitHub!
