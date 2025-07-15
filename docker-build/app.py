#Dynamically Add the Base Path to sys.path  -> This is necessary to ensure that the API can import modules correctly both on local development and in production environments like Docker.
# This ensures both:
# 	•	The api folder itself
# 	•	Its parent directory (e.g., DWELLWELL-AI/ if running locally)
# …are included in Python’s module search path.

import sys
import os

# Add the current working directory to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

######################################################################
from fastapi import FastAPI,Path
from fastapi.responses import JSONResponse

from schema.user_input import UserInput
from model.prediction import predict_price

#create fast api object
app = FastAPI()


@app.post('/predict')
def prediction(data : UserInput):
        #converting pydantic model to dictionary
        data_dict = data.model_dump() 
        #pass the data to price predictioon module
        try:
            predicted_price = predict_price(data_dict)
        except Exception as e:
             return JSONResponse(status_code=500,  content={'error':str(e)})
        
        return JSONResponse(status_code = 200, content={'Predicted_price':predicted_price})
