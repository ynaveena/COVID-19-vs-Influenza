import pandas as pd
import warnings
warnings.filterwarnings('ignore')


train=pd.read_csv("3Class_Train_80_Factorized_Final.csv")
train.drop(['Season'], axis=1,inplace=True)
print(train.shape)
train = train[train.Class != 2]
print("shape",train.shape)


X_train=train.iloc[:,1:-1]
y_train=train.iloc[:,-1]


test=pd.read_csv("3Class_Test_20_Factorized_Final.csv")
test.drop(['Season'], axis=1,inplace=True)
print(test.shape)
test = test[test.Class != 2]
print("shape",test.shape)


X_test=test.iloc[:,1:-1]
y_test=test.iloc[:,-1]


import numpy as np
from sklearn import metrics 
import matplotlib.pyplot as pyplot
from xgboost import plot_importance
import seaborn as sns


import xgboost as xgb
model=xgb.XGBClassifier(random_state=1,learning_rate=0.02,max_depth=4,min_child_weight=1,gamma=1,colsample_bytree=1.0,subsample=0.8,n_estimators=600, objective='binary:logistic')
# Fit on training data
model.fit(X_train, y_train,sample_weight=compute_sample_weight("balanced", y_train))
y_pred=model.predict(X_test)


print(metrics.accuracy_score(y_test, y_pred))
print(metrics.confusion_matrix(y_test,y_pred))
print(metrics.classification_report(y_test,y_pred))

print(metrics.f1_score(y_test, y_pred))
cf_matrix=metrics.confusion_matrix(y_test,y_pred)
sns.heatmap(cf_matrix, annot=True,cmap='Blues')

from matplotlib.ticker import MaxNLocator
fig=plot_importance(model,importance_type="gain")
fig_size = pyplot.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 8
pyplot.rcParams["figure.figsize"] = fig_size
pyplot.show()

shap.initjs()
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(test.drop(['PATID', 'Class'], axis=1))
f = shap.summary_plot(shap_values, test.drop(['PATID', 'Class'], axis=1))


