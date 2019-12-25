import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model

data = pd.read_excel("ENB2012_data.xlsx")

predict = "Y1"

header = data.keys().drop(['Y1', 'Y2'])

for i in range(len(header)):
    features = ['X5']
    features.append(header[i])
    cols = data[features]
    X = np.array(cols)
    Y = np.array(data[predict])

    sum = 0
    for _ in range(100):
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.1)

        linear = linear_model.LinearRegression()

        linear.fit(x_train, y_train)
        acc = linear.score(x_test, y_test)
        sum += acc

    print(features, sum / 100)