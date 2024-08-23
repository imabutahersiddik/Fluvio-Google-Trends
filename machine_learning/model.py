import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model(data):
    # Assuming data is a DataFrame with features and target
    X = data[['feature1', 'feature2']]
    y = data['target']
    
    model = LinearRegression()
    model.fit(X, y)
    
    return model

if __name__ == "__main__":
    # Load your data here
    data = pd.read_csv('trends_data.csv')
    model = train_model(data)
    print("Model trained successfully.")
