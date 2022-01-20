import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

model_path = 'ml/data/Warszawa_pierwotny.pkl'


def make_prediction(v):
    imported_model = pickle.load(open(model_path, 'rb'))

    return imported_model.predict(np.array(v).reshape(-1, 1))[0][0]
