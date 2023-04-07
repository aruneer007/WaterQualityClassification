import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os


class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            print("Entered predict")
            model_path = os.path.join("artifacts","model.pkl")
            preprocessor_path =os.path.join("artifacts","preprocessor.pkl")
            print("Before loading")
            model = load_object(file_path=model_path)
            preprocessor = load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e, sys)


class CustomData:
    def __init__(self,
                 ph : float,
                 iron : float,
                 nitrate : float,
                 chloride : float,
                 lead : float,
                 zinc : float,
                 turbidity : float,
                 fluoride : float,
                 copper : float,
                 odor : float,
                 sulfate: float,
                 conductivity : float,
                 chlorine:float,
                 manganese : float,
                 total_dissolved_solids: float,
                 color: str,
                 source: str
                ):
        
        self.ph = ph
        self.iron = iron
        self.nitrate = nitrate
        self.chloride = chloride
        self.lead = lead
        self.zinc = zinc
        self.turbidity = turbidity
        self.fluoride=fluoride
        self.copper =copper
        self.odor =odor
        self.sulfate =sulfate
        self.conductivity = conductivity
        self.chlorine = chlorine
        self.manganese =manganese
        self.total_dissolved_solids = total_dissolved_solids
        self.color = color
        self.source = source
        
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "pH" :[self.ph],
                "Iron" : [self.iron],
                "Nitrate" :[self.nitrate], 
                "Chloride": [self.chloride],
                "Lead" : [self.lead],
                "Zinc" : [self.zinc],
                "Turbidity" : [self.turbidity],
                "Fluoride" : [self.fluoride],
                "Copper": [self.copper],
                "Odor":[self.odor],
                "Sulfate": [self.sulfate],
                "Conductivity":[self.conductivity],
                "Chlorine": [self.chlorine],
                "Manganese":[self.manganese],
                "Total Dissolved Solids":[self.total_dissolved_solids],
                "Color": [self.color],
                "Source":[self.source]
            }
                
            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)
