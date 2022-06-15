# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:24:56 2021

@author: AM4
"""
import pandas as pd
import numpy as np
from neural import MLP


df = pd.read_csv('data.csv')

df = df.iloc[np.random.permutation(len(df))]
y = df.iloc[0:100, 4].values
y = np.where(y == "Iris-setosa", 1, 0).reshape(-1,1)
X = df.iloc[0:100, [0, 2]].values

inputSize = X.shape[1] # количество входных сигналов равно количеству признаков задачи 
hiddenSizes = 10 # задаем число нейронов скрытого (А) слоя 
outputSize = 1 if len(y.shape) else y.shape[1] # количество выходных сигналов равно количеству классов задачи

iterations = 50
learning_rate = 0.1

net = MLP(inputSize, outputSize, learning_rate, hiddenSizes)
# Обучаем сеть
i = 0
while sum(abs(y-(net.predict(X) > 0.5))) != 0:
    i += 1
    net.train(X, y)

# считаем ошибку на обучающей выборке
pr = net.predict(X)
print(sum(abs(y-(pr>0.5))))
print("Обучили за " + str(i) + " итераций")