from sklearn.datasets import load_iris
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import RidgeClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from xgboost import XGBClassifier
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.layers import Dropout
from keras.wrappers.scikit_learn import KerasClassifier
import numpy as np

def get_dnn_model():
    model = Sequential()
    model.add(Dense(10, input_shape=(4, )))
    model.add(Activation('relu'))
    model.add(Dropout(0.1))
    model.add(Dense(6))
    model.add(Activation('relu'))
    model.add(Dropout(0.1))
    model.add(Dense(3))
    model.add(Activation('softmax'))
    model.compile(optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def logisticfunc(r):
    return(1/(1 + np.exp(-r)))

def get_models():
    dict = {}
    dict['Ridge classifier'] = RidgeClassifier()
    dict['perceptron'] = Perceptron()
    dict['Softmax Regression'] = LogisticRegression()
    dict['naive_bayes'] = GaussianNB()
    dict['k-neighbor'] = KNeighborsClassifier()
    dict['decision tree'] = DecisionTreeClassifier()
    dict['randomforest'] = RandomForestClassifier()
    dict['extra trees'] = ExtraTreesClassifier()
    dict['adaboost'] = AdaBoostClassifier()
    dict['gradient boost'] = GradientBoostingClassifier()
    dict['xgboost'] = XGBClassifier()
    dict['gaussian_process'] = GaussianProcessClassifier()
    dict['linear_discriminant_analysis'] = LinearDiscriminantAnalysis()
    dict['quadratic_discriminant_analysis'] = QuadraticDiscriminantAnalysis()
    dict['SVM linear'] = SVC()
    dict['LinearSVC'] = LinearSVC()
    dict['SVM poly'] = SVC()
    dict['SVM rbf'] = SVC()
    dict['rf+log+linsvm'] = VotingClassifier(estimators=[('rf', RandomForestClassifier(
        )), ('log', LogisticRegression()), (
            'linsvm', LinearSVC())])
    dict['Multi-layer perceptron'] = MLPClassifier()
    dict['deep learning'] = KerasClassifier(build_fn=get_dnn_model)
    return dict

def get_params():
    dict = {}
    dict['Ridge classifier'] = {'alpha': [0.5]}
    dict['perceptron'] = {'n_iter': [200]}
    dict['Softmax Regression'] = {
        'multi_class': ['multinomial'], 'solver': ['sag']}
    dict['naive_bayes'] = {}
    dict['k-neighbor'] = {'n_neighbors': [3,4,5]}
    dict['decision tree'] = {'max_depth': [2]}
    dict['randomforest'] = {'max_depth': [2]}
    dict['extra trees'] = {'max_depth': [2]}
    dict['adaboost'] = {'n_estimators': [10]}
    dict['gradient boost'] = {'n_estimators': [10]}
    dict['xgboost'] = {'max_depth': [2]}
    dict['gaussian_process'] = {'kernel': [1.0 * RBF(1.0)]}
    dict['linear_discriminant_analysis'] = {}
    dict['quadratic_discriminant_analysis'] = {}
    dict['SVM linear'] = {
        'kernel': ['linear']}
    dict['LinearSVC'] = {}
    dict['SVM poly'] = {
        'kernel': ['poly'], 'degree': [3]}
    dict['SVM rbf'] = {'kernel': ['rbf']}
    dict['rf+log+linsvm'] = {'estimators': [[('rf', RandomForestClassifier(max_depth=2)), (
        'log', LogisticRegression(multi_class='multinomial', solver='sag')), (
            'linsvm', LinearSVC())]], 'voting': ['hard']}
    dict['Multi-layer perceptron'] = {
        'hidden_layer_sizes': [(10,)], 'activation': ['logistic'],
        'max_iter': [2000], 'solver': ['adam'], 'random_state': [0]}
    dict['deep learning'] = {'epochs': [500], 'batch_size': [10], 'verbose': [1]}
    return dict

def print_svm_linear_cm_from_coef(model, data, target):
    print('confusion matrix from coefficients and intercepts')
    which_side_of_hyperplanes = np.sign(np.dot(np.array(data), np.array(
        model.coef_).T) + np.array(model.intercept_).T)
    num_target = len(np.unique(target))
    list_freq = []
    for which_side_of_hyperplane in which_side_of_hyperplanes:
        index = 0
        index2d = [0, 1]
        num_hyperplanes = int(num_target * (num_target - 1)/2)
        vec_freq = np.zeros(num_target)
        while index < num_hyperplanes:
            if which_side_of_hyperplane[index] > 0:
                vec_freq[index2d[0]] += 1
            elif which_side_of_hyperplane[index] < 0:
                vec_freq[index2d[1]] += 1
            index += 1
            if index2d[1] < num_target - 1:
                index2d[1] += 1
            else:
                index2d[0] += 1
                index2d[1] = index2d[0] + 1
        list_freq += [vec_freq]
    print(confusion_matrix(target, np.argmax(np.array(list_freq), axis=1)))

def print_cm_from_coef(model_name, model_cv, best_param, data, target):
    if model_name == 'LinearSVC':
        model = model_cv.best_estimator_
        print('confusion matrix from coefficients and intercepts')
        print(confusion_matrix(target, np.argmax(np.dot(np.array(data), np.array(
            model.coef_).T) + np.array(model.intercept_).T, axis=1)))
    if model_name == 'SVM linear':
        model = model_cv.best_estimator_
        print_svm_linear_cm_from_coef(model, data, target)
    if model_name == 'linear_discriminant_analysis':
        model = model_cv.best_estimator_
        print('confusion matrix from coefficients and intercepts')
        print(confusion_matrix(target, np.argmax(
            np.dot(np.array(
                data), np.array(model.coef_).T) + np.array(
                model.intercept_).T, axis=1)))
    if model_name == 'Softmax Regression':
        model = model_cv.best_estimator_
        print('confusion matrix from coefficients and intercepts')
        print(confusion_matrix(target, np.argmax(
            np.dot(np.array(
                data), np.array(model.coef_).T) + np.array(
                model.intercept_).T, axis=1)))
    if (model_name == 'Multi-layer perceptron'
        and len(best_param['hidden_layer_sizes']) == 1
        and best_param['activation'] == 'logistic'):
        model = model_cv.best_estimator_
        print('confusion matrix from coefficients and intercepts')
        print(confusion_matrix(target,
              np.argmax(logisticfunc(np.dot(logisticfunc
                        (np.dot(np.array(data), model.coefs_[0])
                         + model.intercepts_[0]), model.coefs_[1])
                         + model.intercepts_[1]), axis=1)))
    if model_name == 'perceptron':
        model = model_cv.best_estimator_
        print('confusion matrix from coefficients and intercepts')
        print(confusion_matrix(target, np.argmax(np.dot(model.coef_,
              np.array(data).T).T + model.intercept_, axis=1)))


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
    print_cm_from_coef(model_name, model_cv, best_param, data, target)

def main():
    cv = ShuffleSplit(n_splits=7, test_size=.25, random_state=0)
    scoring = 'accuracy'
    models = get_models()
    params = get_params()
    iris= load_iris()
    data = iris.data
    target = iris.target
    for model_name in models.keys():
        if model_name == 'deep learning':
            break
        print_cvs_and_cm(models, params, model_name, data, target, cv, scoring)

if __name__ == '__main__':
    main()
