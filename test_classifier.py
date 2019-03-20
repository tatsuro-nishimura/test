from sklearn.datasets import load_iris
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.gaussian_process.kernels import RBF
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from xgboost import XGBClassifier
import numpy as np

def logisticfunc(r):
    return(1/(1 + np.exp(-r)))

def get_models():
    dict = {}
    dict['perceptron'] = Perceptron()
    dict['naive_bayes'] = GaussianNB()
    dict['k-neighbor'] = KNeighborsClassifier()
    dict['decision tree'] = DecisionTreeClassifier()
    dict['randomforest'] = RandomForestClassifier()
    dict['extra trees'] = ExtraTreesClassifier()
    dict['adaboost'] = AdaBoostClassifier()
    dict['gradient boost'] = GradientBoostingClassifier()
    dict['xgboost'] = XGBClassifier()
    dict['gaussian_process'] = GaussianProcessClassifier()
    dict['QDA'] = QuadraticDiscriminantAnalysis()
    dict['SVM linear'] = SVC()
    dict['SVM poly'] = SVC()
    dict['SVM rbf'] = SVC()
    dict['Multi-layer perceptron'] = MLPClassifier()
    return dict

def get_params():
    dict = {}
    dict['perceptron'] = {'n_iter': [200]}
    dict['naive_bayes'] = {}
    dict['k-neighbor'] = {'n_neighbors': [3,4,5]}
    dict['decision tree'] = {'max_depth': [2]}
    dict['randomforest'] = {'n_estimators': [10], 'max_depth': [2]}
    dict['extra trees'] = {'max_depth': [2]}
    dict['adaboost'] = {'n_estimators': [10]}
    dict['gradient boost'] = {'n_estimators': [10]}
    dict['xgboost'] = {'max_depth': [2]}
    dict['gaussian_process'] = {'kernel': [1.0 * RBF(1.0)]}
    dict['QDA'] = {}
    dict['SVM linear'] = {
        'kernel': ['linear'], 'probability': [True],
        'decision_function_shape': ['ovr']}
    dict['SVM poly'] = {
        'kernel': ['poly'], 'probability': [True], 'degree': [3]}
    dict['SVM rbf'] = {'kernel': ['rbf'], 'probability': [True]}
    dict['Multi-layer perceptron'] = {
        'hidden_layer_sizes': [(10,)], 'activation': ['logistic'],
        'max_iter': [2000], 'solver': ['adam'], 'random_state': [0]}
    return dict

def print_cvs_and_cm(models, params, model_name, data, target, cv, scoring):
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
    print('\n' + 'confusion matrix')
    print(confusion_matrix(target, model_cv.predict(data)))
    if (model_name == 'Multi-layer perceptron'
        and len(best_param['hidden_layer_sizes']) == 1
        and best_param['activation'] == 'logistic'):
        model = model_cv.best_estimator_
        print('confusion matrix from coefficients')
        print(confusion_matrix(target,
              np.argmax(logisticfunc(np.dot(logisticfunc
                        (np.dot(np.array(data), model.coefs_[0])
                         + model.intercepts_[0]), model.coefs_[1])
                         + model.intercepts_[1]), axis=1)))
    if model_name == 'perceptron':
        model = model_cv.best_estimator_
        print('confusion matrix from coefficients')
        print(confusion_matrix(target, np.argmax(np.dot(model.coef_,
              np.array(data).T).T + model.intercept_, axis=1)))


def main():
    cv = ShuffleSplit(n_splits=7, test_size=.25, random_state=0)
    scoring = 'f1_macro'
    models = get_models()
    params = get_params()
    iris= load_iris()
    data = iris.data
    target = iris.target
    for model_name in models.keys():
        print_cvs_and_cm(models, params, model_name, data, target, cv, scoring)

if __name__ == '__main__':
    main()
