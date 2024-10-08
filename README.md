# Crop Yield Prediction Using Regression
This project predicts crop yield based on various environmental factors (rainfall, pesticides, temperature). Selected regression models Random Forest, Gradient Boosting, Decision Tree, and Linear Regression are
compared based on performance.

R-squared, often denoted as R^2 is a statistical measure used in regression analysis to assess the goodness of fit of a model. It quantifies the proportion of variance in the dependent variable that can be predicted or explained by one or more independent variables. Here’s a detailed overview:

# Definition
Coefficient of Determination:It is defined as the ratio of the variance explained by the regression model to the total variance in the dependent variable. It ranges from 0 to 1 (or 0% to 100% when expressed as a percentage).

## How to Use
1. Clone the repository.
2. Install required packages using:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the Python script:
    ```bash
    python src/Prediction_from_User_Input.py
    ```

## Models
- Random Forest Regressor
- Gradient Boosting Regressor
- Decision Tree Regressor
- Linear Regression

|Feature   |Decision Tree   |Random Forest   | Gradient Boosting  |Linear Regression   |
|---|---|---|---|---|
|Basic Algorithm   |Single tree   |Ensemble of trees   |Sequential ensemble   |Linear equation   |
|Performance   |Prone to overfitting   |Robust against noise   |High accuracy   |Limited by linearity   |
|Interpretability   |Highly interpretable   |Less interpretable   |Black-box   |Highly interpretable   |
|Training Time   |Fast   |Moderate   |Slow   |Fast   |
|Hyperparameter Sensitivity   |Low   |Low   |High   |None   |
|Data Handling   |Categorical & numerical   |Categorical & numerical   |Categorical & numerical   |Numerical only   |


# Use Cases
## When to Use Each Model:
- Use Decision Trees for simple problems requiring interpretability.
- Choose Random Forest when you need robust performance across various datasets with less concern for interpretability.
- Opt for Gradient Boosting when seeking high accuracy on complex datasets and you can afford longer training times and hyperparameter tuning.
- Select Linear Regression for problems where relationships are expected to be linear or when interpretability is paramount with fewer predictors.

				
				
				
				
				
 				
				

