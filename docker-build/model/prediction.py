import pickle
import pandas as pd
import os

model_path = os.path.join(os.path.dirname(__file__), '5.2_pipeline.pkl')
def load_model():
    
    with open(model_path,'rb') as f:
        model = pickle.load(f)
    return model
#
def predict_price(data_dict : dict) -> float:
    
    #convert the input data to dataframe
    input_df = pd.DataFrame([data_dict])
    
    #load the model
    model = load_model()

    #predict the price
    predicted_price = model.predict(input_df)[0]

    return predicted_price
