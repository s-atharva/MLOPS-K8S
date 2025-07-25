# train_iris_model.py
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle

# Load data
X, y = load_iris(return_X_y=True)

# Train model
model = LogisticRegression(max_iter=200)
model.fit(X, y)

# Save model
with open("iris_model.pkl", "wb") as f:
    pickle.dump(model, f)
