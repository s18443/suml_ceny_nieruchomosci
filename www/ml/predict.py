import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

model_path = 'ml/data/'

def make_prediction(v, miasto):
    imported_model = pickle.load(open(model_path+miasto+'_pierwotny.pkl', 'rb'))

    return imported_model.predict(np.array(v).reshape(-1, 1))[0][0]
