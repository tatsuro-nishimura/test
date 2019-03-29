from sklearn import datasets
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from xgboost import XGBRegressor
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.core import Activation
from keras.wrappers.scikit_learn import KerasRegressor

def get_dnn_model():
    model = Sequential()
    model.add(Dense(10, input_dim=10))
    model.add(Activation('relu'))
    model.add(Dense(12))
    model.add(Activation('relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

def get_models():
    dict = {}
    dict['linear regression'] = LinearRegression()
    dict['Ridge regression'] = Ridge()
    dict['Lasso regression'] = Lasso()
    dict['decision tree'] = DecisionTreeRegressor()
    dict['randomforest'] = RandomForestRegressor()
    dict['extra trees'] = ExtraTreesRegressor()
    dict['adaboost'] = AdaBoostRegressor()
    dict['gradient boost'] = GradientBoostingRegressor()
    dict['xgboost'] = XGBRegressor()
    dict['SVM linear'] = SVR()
    dict['SVM poly'] = SVR()
    dict['SVM rbf'] = SVR()
    dict['Multi-layer perceptron'] = MLPRegressor()
    dict['keras regressor'] = KerasRegressor(build_fn=get_dnn_model)
    return dict

def get_params():
    dict = {}
    dict['linear regression'] = {}
    dict['Ridge regression'] = {'alpha': [0.5]}
    dict['Lasso regression'] = {'alpha': [0.1]}
    dict['decision tree'] = {'max_depth': [2]}
    dict['randomforest'] = {'max_depth': [2]}
    dict['extra trees'] = {'max_depth': [2]}
    dict['adaboost'] = {'n_estimators': [10]}
    dict['gradient boost'] = {'n_estimators': [10]}
    dict['xgboost'] = {'max_depth': [2]}
    dict['SVM linear'] = {
        'kernel': ['linear'], 'C': [1000]}
    dict['SVM poly'] = {
        'kernel': ['poly'], 'C': [1000], 'gamma': ['auto'], 'degree': [3],
        'epsilon': [.1], 'coef0': [1]}
    dict['SVM rbf'] = {'kernel': ['rbf'], 'C': [1000], 'gamma': [.1]}
    dict['Multi-layer perceptron'] = {
        'hidden_layer_sizes': [(5,)], 'activation': ['relu'],
        'learning_rate': ['adaptive'], 'learning_rate_init': [.01],
        'alpha': [.01], 'max_iter': [1000], 'solver': ['adam'],
        'random_state': [0]}
    dict['keras regressor'] = {'epochs': [100], 'batch_size': [10], 'verbose': [1]}
    return dict

def relu(r):
    return np.maximum(0, r)

def rmse(v0, v1):
    return np.sqrt(mean_squared_error(v0, v1))

def print_rmse_from_coef(model_name, model, best_param, data, target):
    if model_name in ['linear regression', 'SVM linear']:
        print('\n' + 'RMSE from coefficients and intercepts')
        print(rmse(target, np.dot(np.array(
            data), np.array(model.coef_).T) + np.array(model.intercept_).T))
    if (model_name == 'Multi-layer perceptron'
        and len(best_param['hidden_layer_sizes']) == 1
        and best_param['activation'] == 'relu'):
        print('\n' + 'RMSE from coefficients and intercepts')
        print(rmse(target,
              relu(np.dot(relu(np.dot(
                np.array(data), model.coefs_[0]) + model.intercepts_[0]),
                    model.coefs_[1]) + model.intercepts_[1])))


def print_cvs_rmse(models, params, model_name, data, target, cv, scoring):
    model = models[model_name]
    param = params[model_name]
    model_cv = GridSearchCV(model, param, cv=cv, scoring=scoring)
    model_cv.fit(data, target)
    print('\n')
    print('\n' + model_name)
    print('\n' + 'scoring: ' + scoring)
    print('\n' + 'best parameter')
    best_param = model_cv.best_params_
    print(best_param)
    print('\n' + 'cross validation score')
    print(model_cv.best_score_)
    model = model_cv.best_estimator_
    print('\n' + 'RMSE')
    print(rmse(target, model.predict(data)))
    print_rmse_from_coef(model_name, model, best_param, data, target)


def main():
    cv = ShuffleSplit(n_splits=7, test_size=.25, random_state=0)
    scoring = 'r2'
    models = get_models()
    params = get_params()
    diabetes = datasets.load_diabetes()
    data = diabetes.data
    target = diabetes.target
    for model_name in models.keys():
        if model_name == 'keras regressor':
            break
        print_cvs_rmse(models, params, model_name, data, target, cv, scoring)

if __name__ == '__main__':
    main()
