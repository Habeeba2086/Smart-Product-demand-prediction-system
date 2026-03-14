# 📊 Demand Prediction Using Machine Learning

This project demonstrates **demand prediction using Linear Regression**, a Machine Learning algorithm.
The model predicts product **sales demand** based on factors such as **day, price, promotions, and holidays**.
The goal of this project is to show how **Machine Learning can be used for sales forecasting in businesses**.

# 🚀 Project Overview
Demand prediction helps businesses:
* Forecast future product sales
* Manage inventory efficiently
* Plan promotions and pricing strategies
* Reduce stock shortages and overstock problems
This project uses **Linear Regression** to build a simple predictive model using Python.

# 🧠 Machine Learning Algorithm Used
### Linear Regression
Linear Regression is a **supervised learning algorithm** used for predicting continuous values.
It finds the relationship between:
**Independent Variables (Features)**
* Day
* Price
* Promotion
* Holiday
**Dependent Variable (Target)**
* Sales
The model learns patterns from historical data and predicts future sales.

# 📂 Project Structure

```
Demand-Prediction-ML
│
├── demand_prediction.py        # Main Python script
├── sales_data.csv              # Dataset (sales data)
├── report
│     └── Actual_vs_Predicted.png   # Visualization output
│
└── README.md                   # Project documentation
```

# 📊 Dataset Description
The dataset contains the following columns:
| Column    | Description                                   |
| --------- | --------------------------------------------- |
| Day       | Day number                                    |
| Price     | Product price                                 |
| Promotion | Whether promotion is active (1 = Yes, 0 = No) |
| Holiday   | Whether it is a holiday (1 = Yes, 0 = No)     |
| Sales     | Number of units sold                          |

Example:

| Day | Price | Promotion | Holiday | Sales |
| --- | ----- | --------- | ------- | ----- |
| 1   | 50    | 1         | 0       | 200   |
| 2   | 52    | 0         | 0       | 180   |
| 3   | 51    | 1         | 0       | 220   |

# ⚙️ Steps in the Project
### 1️⃣ Import Required Libraries
The project uses the following Python libraries:
* pandas
* matplotlib
* scikit-learn
  
### 2️⃣ Load Dataset
The dataset is created using Python dictionaries and converted into a **pandas DataFrame**.

### 3️⃣ Feature Selection
Input Features:
```
Day
Price
Promotion
Holiday
```
Target Variable:
```
Sales
```

### 4️⃣ Train-Test Split
The dataset is divided into:
* **Training Data (80%)**
* **Testing Data (20%)**
This helps evaluate the model performance.

### 5️⃣ Train the Model
The **Linear Regression model** is trained using the training dataset.

### 6️⃣ Model Evaluation
Two evaluation metrics are used:
**Mean Absolute Error (MAE)**
Measures the average difference between actual and predicted values.
**R² Score**
Measures how well the model fits the data.

# 📈 Visualization
The project generates a scatter plot showing **Actual vs Predicted Sales**.
* X-axis → Actual Sales
* Y-axis → Predicted Sales
If the model performs well, points will be close to a straight line.
![Actual vs Predicted](report/Actual_vs_Predicted.png)


# 🔮 Future Sales Prediction
The model also predicts future sales using new data:
Example:
| Day | Price | Promotion | Holiday |
| --- | ----- | --------- | ------- |
| 11  | 51    | 1         | 0       |
| 12  | 50    | 0         | 1       |
| 13  | 52    | 1         | 0       |
The trained model predicts **future sales demand** for these days.

# 🛠️ Technologies Used
* Python
* Machine Learning
* Pandas
* Matplotlib
* Scikit-learn
* GitHub

# ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/demand-prediction-ml.git
```

### Step 2: Install Required Libraries

```bash
pip install pandas matplotlib scikit-learn
```

### Step 3: Run the Python Script

```bash
python demand_prediction.py
```

The script will:
* Train the model
* Show evaluation results
* Generate the graph
* Predict future sales

# 📌 Applications of Demand Prediction

Demand prediction is widely used in:
* Retail
* E-commerce
* Supply chain management
* Inventory planning
* Marketing strategies
