from fastapi import FastAPI,Path
from fastapi.responses import JSONResponse


from api.schema.user_input import UserInput
from api.model.prediction import predict_price

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
