# Crop Yield Prediction Using Regression
This project predicts crop yield based on various environmental factors (rainfall, pesticides, temperature). Selected regression models Random Forest, Gradient Boosting, Decision Tree, and Linear Regression are
compared based on performance.

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

Feature	Decision Tree	Random Forest	Gradient Boosting	Linear Regression
Basic Algorithm	Single tree	Ensemble of trees	Sequential ensemble	Linear equation
Performance	Prone to overfitting	Robust against noise	High accuracy	Limited by linearity
Interpretability	Highly interpretable	Less interpretable	Black-box	Highly interpretable
Training Time	Fast	Moderate	Slow	Fast
Hyperparameter Sensitivity	Low	Low	High	None
Data Handling	Categorical & numerical	Categorical & numerical	Categorical & numerical	Numerical only

