import joblib
def make_prediction(model_name, input_data):
    """
    Load the saved model and make a prediction for the input data.
    
    Parameters:
    - model_name: str, name of the model to use ('Random Forest', 'Gradient Boosting', 'Decision Tree', 'LinearRegression')
    - input_data: dict, input data with keys as feature names and values as feature values
    
    Returns:
    - Prediction from the model.
    """
    # Load the saved model
    model = joblib.load(f'model/Gradient Boosting_model.pkl')  #Provide path to the downloaded model
    
    # Convert input_data to a DataFrame (because the model expects it)
    input_df = pd.DataFrame([input_data])
    
    # Make prediction
    prediction = model.predict(input_df)
    
    return prediction

# Provide/Edit field for new input prediction
user_input = {
    'Area': 'Algeria',
    'Item': 'Wheat',
    'Year': 1993,
    'average_rain_fall_mm_per_year': 200,
    'pesticides_tonnes': 100,
    'avg_temp': 18.5
}

# Predict using Random Forest
predicted_yield = make_prediction('RandomForest', user_input)
print(f"Predicted yield: {predicted_yield[0]:.2f}")
