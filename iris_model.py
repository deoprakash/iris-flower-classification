import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

iris = load_iris()
x, y = iris.data, iris.target

clf = RandomForestClassifier()
clf.fit(x,y)

joblib.dump(clf, 'app/model.pkl')