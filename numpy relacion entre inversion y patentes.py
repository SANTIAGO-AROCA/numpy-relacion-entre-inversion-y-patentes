# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z-BJuXNpqiGzXIlZp389ol68TFxjGPJY
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

study_hours = np.array([10, 15, 12, 8, 14, 5, 16, 7, 11, 13, 9, 4, 18, 3, 17, 6, 14, 2, 20, 1])
final_grade = np.array([3.8, 4.2, 3.6, 3.0, 4.5, 2.5, 4.8, 2.8, 3.7, 4.0, 3.2, 2.2, 5.0, 1.8, 4.9, 2.7, 4.4, 1.5, 5.0, 1.0])

x = study_hours.reshape(-1,1)
y = final_grade

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

r2 = model.score(x_test,y_test)

coeficients = model.coef_[0]
intercept = model.intercept_

print("R2 Score:",r2)
print("Coeficients:",coeficients)
print("Intercept:",intercept)

plt.scatter(x_test,y_test,color='red')
plt.plot(x_test,y_pred,color='black',linestyle = '-', linewidth = 2, label = 'predicted grades')
plt.xlabel('Study Hours')
plt.ylabel('Final Grade')
plt.title('Study Hours vs Final Grade')
plt.show()

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#datos de inversion (millones de dolares)
inversion_ID = np.array([2, 12, 5, 20, 8, 15, 25, 18, 7, 22, 10, 17, 30, 14, 19, 6, 24, 27, 13, 21,
                         9, 11, 28, 16, 26, 14, 11, 12, 10, 18, 9, 15, 13, 20, 11, 8, 16, 17,
                         10, 9, 10, 19, 6, 14, 15, 18, 12, 19, 7, 5, 20, 8, 19, 12, 9, 7,
                         6, 9, 19, 15, 14, 10, 17, 19, 16, 8, 6, 20, 13, 6, 16, 8, 20,
                         14, 18, 19, 9, 16, 6, 20, 19, 17, 8, 16, 19, 18, 13])

#datos de patentes
num_patentes = np.array([1, 8, 4, 15, 6, 10, 20, 12, 5, 18, 7, 11, 25, 9, 14, 3, 16, 22, 8, 13,
                        6, 7, 23, 10, 21, 19, 12, 13, 11, 18, 9, 16, 14, 20, 12, 9, 16, 17,
                        11, 10, 11, 19, 7, 15, 16, 18, 13, 19, 8, 6, 20, 9, 19, 13, 10, 8,
                        7, 10, 19, 16, 15, 11, 17, 19, 17, 9, 7, 20, 14, 7, 16, 9, 20,
                        15, 18, 19, 10, 16, 7, 20, 19, 18, 9, 16, 19, 18, 14])


x = inversion_ID.reshape(-1,1)
y = num_patentes


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(x_train, y_train)


y_pred = model.predict(x_test)


r2 = model.score(x_test, y_test)
print("r2 score:", r2)
coeficiente = model.coef_[0]
print("coeficiente (inversión I+D):", coeficiente)
intercepto = model.intercept_
print("Intercepto:", intercepto)


plt.scatter(x_test, y_test, color='red', label='datos')
plt.plot(x_test, y_pred, color='blue', linestyle='-', linewidth=2, label='predicción')
plt.xlabel('Datos de inversion (millones de dólares)')
plt.ylabel('Número de patentes')
plt.title('Relación entre inversion y patentes')
plt.legend()
plt.show()