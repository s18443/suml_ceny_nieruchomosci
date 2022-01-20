import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

data_path = 'ml/data/10_points.csv'
model_path = 'ml/data/fresh_pickle_model.pkl'

def lr(data):
    x = data['x'].values.reshape(-1, 1)
    y = data['y'].values.reshape(-1, 1)

    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)

    return linear_regressor

def add_values_train(a, b):
    pd.read_csv(data_path).append(pd.DataFrame({
        "x": [*a],
        "y": [*b]
    })).to_csv(data_path, index=False)

    inp = pd.read_csv(data_path)

    pickle.dump(lr(inp), open(model_path, 'wb'))

