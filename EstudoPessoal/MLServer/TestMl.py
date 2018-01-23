# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 08:51:00 2018

@author: lcristovao
"""

import ML_MegaFunction as ml
import pandas as pd
import numpy as np



dataset=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data')
#dataset=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')
p=ml.Predictor()
predictor=p.ReturnPredictor(dataset)

dataset.iloc[:,:-1]=p.TurnDatasetToNumeric(dataset.iloc[:,:-1])

print(np.array_str(dataset.iloc[300,:].values)+'\n')
print('prediction:'+np.array_str(predictor.predict(dataset.iloc[300:301,:-1].values)))

