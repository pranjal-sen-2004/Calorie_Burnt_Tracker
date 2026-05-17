import sys
from src.exception import CustomException
from src.utils import load_object
import pandas as pd
import os


class PredictPipeline:

    def __init__(self):

        try:

            model_path = os.path.join("artifacts", "model.pkl")
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")

            print("Loading model and preprocessor once...")

            self.model = load_object(file_path=model_path)

            self.preprocessor = load_object(file_path=preprocessor_path)

            print("Model loaded successfully")

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, features):

        try:

            data_scaled = self.preprocessor.transform(features)

            preds = self.model.predict(data_scaled)

            return preds

        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(  self,
        Age:int,
        Gender: str,
        Weight: int,
        Height: int,
        Max_BPM: int,
        Avg_BPM: int,
        Resting_BPM: int,
        Session_Duration: int,
        Workout_type: str,
        Fat_Percentage: int,
        Water_Intake: int,
        Workout_Frequency: int,
        Experience_Level: str,
        BMI: int):

        self.Age = Age
        self.Gender = Gender
        self.Weight = Weight
        self.Height = Height
        self.Max_BPM = Max_BPM
        self.Avg_BPM = Avg_BPM
        self.Resting_BPM = Resting_BPM
        self.Session_Duration = Session_Duration
        self.Workout_type = Workout_type
        self.Fat_Percentage = Fat_Percentage
        self.Water_Intake = Water_Intake
        self.Workout_Frequency = Workout_Frequency
        self.Experience_Level = Experience_Level
        self.BMI = BMI

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Age": [self.Age],
                "Gender": [self.Gender],
                "Weight (kg)": [self.Weight],
                "Height (m)": [self.Height],
                "Max_BPM": [self.Max_BPM],
                "Avg_BPM": [self.Avg_BPM],
                "Resting_BPM": [self.Resting_BPM],
                "Session_Duration (hours)": [self.Session_Duration],
                "Workout_Type": [self.Workout_type],
                "Fat_Percentage": [self.Fat_Percentage],
                "Water_Intake (liters)": [self.Water_Intake],
                "Workout_Frequency (days/week)": [self.Workout_Frequency],
                "Experience_Level": [self.Experience_Level],
                "BMI": [self.BMI]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)



