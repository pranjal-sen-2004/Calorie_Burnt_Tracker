# Complete Project Description & Frontend Generation Prompt

## PROJECT OVERVIEW
This is a **Machine Learning-based Gym Member Calories Burned Prediction System** built with **Flask Framework**. The project uses historical gym member exercise tracking data to predict the number of calories a member will burn during their workout session based on their personal metrics and workout characteristics.

## PROJECT ARCHITECTURE

### Backend Stack:
- **Framework**: Flask (Python)
- **Machine Learning**: Multiple regression models (Random Forest, Gradient Boosting, XGBoost, CatBoost, SVR, Linear Regression, Decision Tree, AdaBoost)
- **Data Processing**: Pandas, Scikit-learn, NumPy
- **Model Serialization**: Pickle (.pkl format)

### Project Structure:
```
├── app.py                              # Main Flask application
├── src/
│   ├── components/
│   │   ├── data_ingestion.py          # Handles raw data loading & train-test split
│   │   ├── data_transformation.py     # Handles feature scaling & encoding
│   │   └── model_trainer.py           # Trains multiple ML models & selects best
│   ├── pipeline/
│   │   ├── train_pipeline.py          # Training workflow orchestration
│   │   └── predict_pipeline.py        # Prediction workflow (to be implemented)
│   ├── logger.py                       # Logging utility
│   ├── exception.py                   # Custom exception handling
│   └── utils.py                       # Utility functions
├── artifacts/
│   ├── train.csv                      # Processed training data
│   ├── test.csv                       # Processed test data
│   ├── data.csv                       # Raw data
│   ├── model.pkl                      # Trained ML model
│   └── preprocessor.pkl               # Preprocessing pipeline (scaler + encoder)
├── templates/
│   ├── index.html                     # Home page (to be created)
│   └── predict.html                   # Prediction form page (to be created)
└── requirements.txt                   # Python dependencies

```

## DATASET INFORMATION

### Input Features (14 features):
1. **Age** (Integer, years) - Member's age
2. **Gender** (Categorical: Male/Female) - Member's gender
3. **Weight (kg)** (Float) - Member's body weight
4. **Height (m)** (Float) - Member's height
5. **Max_BPM** (Integer, beats/min) - Maximum heart rate during workout
6. **Avg_BPM** (Integer, beats/min) - Average heart rate during workout
7. **Resting_BPM** (Integer, beats/min) - Resting heart rate
8. **Session_Duration (hours)** (Float) - Duration of workout session
9. **Workout_Type** (Categorical: e.g., Cardio, Strength, etc.) - Type of exercise
10. **Fat_Percentage** (Float, %) - Body fat percentage
11. **Water_Intake (liters)** (Float) - Water consumed during session
12. **Workout_Frequency (days/week)** (Integer) - Weekly workout frequency
13. **Experience_Level** (Integer, 1-5) - Member's fitness experience level
14. **BMI** (Float) - Body Mass Index

### Target Variable:
- **Calories_Burned** (Float) - Number of calories burned during the session (Regression Target)

## MACHINE LEARNING PIPELINE

### Data Processing:
- **Data Ingestion**: Loads gym_members_exercise_tracking.csv, splits into 80% train / 20% test
- **Data Transformation**: 
  - Numerical features: Median imputation + Standard scaling
  - Categorical features: Most frequent imputation + One-hot encoding
  - Preprocessor saved as `preprocessor.pkl`

### Model Training:
- Compares 8 different regression models
- Evaluates using R² score and Mean Squared Error
- Selects best performing model
- Saves trained model as `model.pkl`

## FRONTEND REQUIREMENTS

### Page 1: HOME PAGE (index.html)
**Purpose**: Landing page with project introduction and navigation to prediction

**Design Requirements**:
- Professional, modern, and visually appealing layout
- Hero section with project title: "Gym Calories Burned Predictor"
- Descriptive text explaining what the application does
- Brief explanation: "Predict calories burned based on your fitness metrics"
- Large, prominent call-to-action button: "Start Prediction" that links to /predict page
- Display key features/benefits of the predictor (e.g., "Accurate predictions", "Instant results", "Based on ML models")
- Footer with project information
- Responsive design (works on desktop, tablet, mobile)
- Use color scheme suitable for fitness/gym theme (e.g., blues, greens, or bold accent colors)
- Include gym/fitness related icons or imagery
- Smooth animations and transitions

### Page 2: PREDICTION PAGE (predict.html)
**Purpose**: Interactive form to input user data and get calorie burn prediction

**Form Fields Required** (in logical order):
1. **Age** - Number input (e.g., 25-70 years)
2. **Gender** - Dropdown/Radio buttons (Male / Female)
3. **Weight (kg)** - Number input with decimal support
4. **Height (m)** - Number input with decimal support
5. **Max Heart Rate (BPM)** - Number input (e.g., 100-200)
6. **Average Heart Rate (BPM)** - Number input
7. **Resting Heart Rate (BPM)** - Number input (e.g., 60-100)
8. **Session Duration (hours)** - Number input with decimal support
9. **Workout Type** - Dropdown (Options: Cardio, Strength, Yoga, etc.)
10. **Fat Percentage (%)** - Number input with decimal support
11. **Water Intake (liters)** - Number input with decimal support
12. **Workout Frequency (days/week)** - Number input (0-7)
13. **Experience Level** - Dropdown or Radio buttons (1=Beginner, 2=Intermediate, 3=Intermediate-Advanced, 4=Advanced, 5=Expert)
14. **BMI** - Number input with decimal support (auto-calculate from Height & Weight, optional)

**Form Features**:
- All fields should have proper labels and placeholders
- Input validation (range checks, required fields)
- Real-time BMI calculation (optional feature based on Height and Weight)
- Clear sections/grouping (Personal Info, Heart Rate Metrics, Workout Details, Body Metrics)
- Submit button: "Predict Calories Burned"
- Reset/Clear button to reset all fields

**Results Section** (after prediction):
- Display predicted calories burned prominently
- Show a result message like: "Based on your metrics, you will burn approximately [X] calories"
- Visual representation (e.g., progress bar, badge, or icon)
- Option to "Predict Again" (goes back to form)
- Option to "Go Home" (returns to index page)

**Design Requirements for Prediction Page**:
- Organized form layout with proper spacing
- Mobile-responsive design
- Loading indicator while waiting for prediction
- Error handling messages (in case of invalid input or server error)
- Success/failure notifications
- Consistent styling with home page
- Use of colors to distinguish form sections
- Fitness/gym themed icons for form sections
- Clear visual hierarchy

## FLASK ROUTES TO IMPLEMENT

### Route 1: GET /
- **Function**: `home()`
- **Returns**: Render `templates/index.html`
- **Purpose**: Display home page

### Route 2: GET/POST /predict
- **Function**: `predict()`
- **GET Request**: Render `templates/predict.html` (display form)
- **POST Request**: 
  - Accept form data (14 input features)
  - Load preprocessor.pkl and model.pkl from artifacts
  - Preprocess input data
  - Make prediction using trained model
  - Return result as JSON or render template with predicted value
- **Purpose**: Handle prediction form and generate predictions

## TECHNICAL IMPLEMENTATION NOTES

### Data Flow for Prediction:
1. User fills form on /predict page
2. JavaScript captures form data
3. AJAX POST request to Flask /predict endpoint
4. Flask receives data, validates it
5. Loads preprocessor and model from artifacts
6. Applies preprocessing (scaling & encoding) to input data
7. Uses trained model to predict calories burned
8. Returns prediction result to frontend
9. Display result on prediction page

### Error Handling:
- Handle missing form fields
- Validate numeric input ranges
- Display user-friendly error messages
- Show server error messages if model loading fails

### Styling Preferences:
- Use CSS framework (Bootstrap, Tailwind CSS, or Material Design)
- Maintain consistent color scheme throughout
- Ensure accessibility (proper contrast, alt text, etc.)
- Use responsive grid layout

## EXAMPLE INPUT/OUTPUT

### Example Prediction Input:
- Age: 35
- Gender: Male
- Weight: 80 kg
- Height: 1.75 m
- Max BPM: 160
- Avg BPM: 130
- Resting BPM: 70
- Session Duration: 1.5 hours
- Workout Type: Cardio
- Fat Percentage: 20
- Water Intake: 2.5 liters
- Workout Frequency: 5 days/week
- Experience Level: 4
- BMI: 26.1

### Expected Output:
```
Prediction Result: 450-550 calories (approximately)
```

## KEY REQUIREMENTS SUMMARY

✅ Flask framework with Python backend
✅ Two-page frontend (Home & Predict pages)
✅ Beautiful, modern, fitness-themed UI design
✅ Responsive design (mobile-friendly)
✅ Form with all 14 input fields from dataset
✅ Real-time prediction using ML model
✅ Proper form validation and error handling
✅ Clear, intuitive user experience
✅ Professional styling and layout

---

## DIRECT PROMPT FOR AI FRONTEND GENERATION

Use this as your prompt when requesting an AI to generate the frontend code:

---

**PROMPT:**

"Generate a complete Flask frontend application for a Machine Learning-based Gym Calories Burned Predictor. The project uses Flask framework with Python backend.

The application has two pages:

**Page 1 - Home (index.html):**
- Modern, fitness-themed landing page
- Project title: 'Gym Calories Burned Predictor'
- Description of the application
- Large call-to-action button 'Start Prediction' linking to /predict
- Display key features
- Responsive, mobile-friendly design
- Professional styling with fitness theme (blues, greens, or bold colors)

**Page 2 - Prediction (predict.html):**
- Interactive form with 14 input fields grouped into sections:
  - Personal Info: Age, Gender, Height (m), Weight (kg), BMI
  - Heart Metrics: Max BPM, Avg BPM, Resting BPM
  - Workout Details: Session Duration (hours), Workout Type (dropdown), Workout Frequency (days/week)
  - Body Metrics: Fat Percentage (%), Water Intake (liters), Experience Level (dropdown 1-5)
- All fields with proper labels, placeholders, and validation
- Submit button 'Predict Calories Burned'
- Clear/Reset button
- Results section displaying predicted calories with message
- Loading indicator during prediction
- Error handling and success messages
- 'Predict Again' and 'Go Home' buttons
- Responsive mobile design
- Professional fitness-themed styling

**Flask Routes:**
- GET / → home() → render index.html
- GET/POST /predict → predict() → render predict.html (GET) or process form (POST)

**Data & Predictions:**
- Input: 14 fitness/health metrics from gym members
- Output: Predicted calories burned (float value)
- Backend: ML models using preprocessor.pkl and model.pkl from artifacts folder

**Design Requirements:**
- Use Bootstrap/Tailwind CSS or similar framework
- Fitness/gym themed color scheme
- Smooth animations and transitions
- Clear visual hierarchy
- Professional, modern look
- Mobile-responsive
- Accessible design (proper contrast, labels)
- Icons for form sections (optional)

Create complete HTML files with inline CSS/Bootstrap classes and JavaScript for form handling, validation, and AJAX prediction requests."

---

