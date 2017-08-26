import keras
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import sys


# Purpose: Practice to write a deep neural network for rapid prototyping

#-----------------------------------------------------------------------------------------------------------------------
# Put your path here!
path = '/home/ckoguchi/Projects/VerBrose/Shared/Attrition_Dataset'
print('Changing path to: ' + path)
os.chdir(path)

#-----------------------------------------------------------------------------------------------------------------------
print('Loading data...')
train_df = pd.read_csv('AnalyticsChallenge1-Train.csv')

# print(train_df.head()) # see the first 5 rows
# print(train_df.columns) # names of variables here
# print(train_df.dtypes) # find categorical and numerical here


# Drop non-numerical values from train
#     This is throwing out useful information.  These categorical values can be encoded to numbers.
#     I'm just too lazy
#     During data exploration, I found that OverTime was one of the best features.  Go figure.

#-----------------------------------------------------------------------------------------------------------------------
non_numerical = ['Attrition', 'BusinessTravel', 'Department', 'EducationField',
                 'Gender', 'JobRole', 'MaritalStatus', 'Over18', 'OverTime']



X = train_df.drop(non_numerical, axis=1)
y = train_df.Attrition.map(dict(Yes=1, No=0)) # this is originally encoded as Yes/No and not 0/1

scaler = MinMaxScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# print(y_train.head(), y_train.shape)


# print(X_train.shape) # (1200, 26)
m, n = X_train.shape


#-----------------------------------------------------------------------------------------------------------------------
# AUC for a binary classifier
# def auc(y_true, y_pred):
#     ptas = tf.stack([binary_PTA(y_true,y_pred,k) for k in np.linspace(0, 1, 1000)],axis=0)
#     pfas = tf.stack([binary_PFA(y_true,y_pred,k) for k in np.linspace(0, 1, 1000)],axis=0)
#     pfas = tf.concat([tf.ones((1,)) ,pfas],axis=0)
#     binSizes = -(pfas[1:]-pfas[:-1])
#     s = ptas*binSizes
#     return K.sum(s, axis=0)
#-----------------------------------------------------------------------------------------------------------------------
# PFA, prob false alert for binary classifier
# def binary_PFA(y_true, y_pred, threshold=K.variable(value=0.5)):
#     y_pred = K.cast(y_pred >= threshold, 'float32')
#     # N = total number of negative labels
#     N = K.sum(1 - y_true)
#     # FP = total number of false alerts, alerts from the negative class labels
#     FP = K.sum(y_pred - y_pred * y_true)
#     return FP/N
#-----------------------------------------------------------------------------------------------------------------------
# P_TA prob true alerts for binary classifier
# def binary_PTA(y_true, y_pred, threshold=K.variable(value=0.5)):
#     y_pred = K.cast(y_pred >= threshold, 'float32')
#     # P = total number of positive labels
#     P = K.sum(y_true)
#     # TP = total number of correct alerts, alerts from the positive class labels
#     TP = K.sum(y_pred * y_true)
#     return TP/P



#-----------------------------------------------------------------------------------------------------------------------
# Define model as 2 layer Relu with Softmax

from keras import metrics


#-----------------------------------------------------------------------------------------------------------------------
# Build model - 2 Layer Neural network
model = keras.models.Sequential()

model.add(keras.layers.Dense(960, input_dim=n, activation='linear', name='layer1'))
# model.add(keras.layers.Dropout(0.5))
# model.add(keras.layers.Dense(64, activation='relu', name='layer2'))
# model.add(keras.layers.Dropout(0.5))
# model.add(keras.layers.Dense(64, activation='relu', name='layer3'))
# model.add(keras.layers.Dropout(0.5))
# model.add(keras.layers.Dense(64, activation='relu', name='layer4'))
# model.add(keras.layers.Dropout(0.5))
# model.add(keras.layers.Dense(64, activation='relu', name='layer5'))
# model.add(keras.layers.Dropout(0.5))
model.add(keras.layers.Dense(1 , activation='softmax', name='output'))


#-----------------------------------------------------------------------------------------------------------------------
# Defaults from keras API for binary classification
print('Compiling model...')
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['acc'])

#-----------------------------------------------------------------------------------------------------------------------
# Fit model and evaluate
print('Fitting model...')
model.fit(np.asarray(X_train), np.asarray(y_train), epochs=100, validation_split=0.1, verbose=2) # Aww yeh, u know I like it verbose
model_score = model.evaluate(np.asarray(X_test), np.asarray(y_test)) # I guess this doesn't work with custom error metrics? wtf

print('\nFinal Score:\n', model_score)