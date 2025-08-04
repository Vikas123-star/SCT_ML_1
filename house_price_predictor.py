# House Price Predictor using Linear Regression

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
# Sample housing data (can be replaced with a CSV file)
data = {
    'square_feet': [1200, 1500, 1800, 2000, 2200, 2500],
    'bedrooms': [2, 3, 3, 4, 4, 5],
    'bathrooms': [1, 2, 2, 2, 3, 3],
    'price': [200000, 250000, 300000, 350000, 400000, 450000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['square_feet', 'bedrooms', 'bathrooms']]
y = df['price']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Model training
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------
# Predict price based on user input
# ------------------

print("\n📊 House Price Prediction")
print("-" * 30)
sq_ft = int(input("Enter square footage: "))
beds = int(input("Enter number of bedrooms: "))
baths = int(input("Enter number of bathrooms: "))

user_input = [[sq_ft, beds, baths]]
predicted = model.predict(user_input)

print(f"\n💰 Estimated House Price: ₹{int(predicted[0]):,}")
