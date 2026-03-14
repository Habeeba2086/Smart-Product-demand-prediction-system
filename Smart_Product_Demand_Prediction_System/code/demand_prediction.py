# ML Algorithm: Linear Regression for Demand Prediction

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Step 1: Dataset
data = {
    'Day': [1,2,3,4,5,6,7,8,9,10],
    'Price': [50,52,51,53,50,49,48,50,51,52],
    'Promotion': [1,0,1,0,1,0,1,0,1,0],
    'Holiday': [0,0,0,1,0,0,0,1,0,0],
    'Sales': [200,180,220,190,240,210,250,200,260,230] 
}

df = pd.DataFrame(data)

# Step 2: Features and Target
X = df[['Day', 'Price', 'Promotion', 'Holiday']]
y = df['Sales']

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Train Linear Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 5: Predict
y_pred = model.predict(X_test)

# Step 6: Evaluation
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Step 7: Actual vs Predicted Graph python
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")
plt.savefig("report/Actual_vs_Predicted.png")  
plt.show()

# Step 8: Future Prediction
future_data = pd.DataFrame({
    'Day': [11,12,13],
    'Price': [51,50,52],
    'Promotion': [1,0,1],
    'Holiday': [0,1,0]
})
future_sales = model.predict(future_data)
future_data['Predicted_Sales'] = future_sales
print("\nFuture Sales Prediction:")
print(future_data) 