from sklearn import datasets
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor

def get_models():
    dict = {}
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
    return dict

def get_params():
    dict = {}
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
    return dict

def print_cvs(models, params, model_name, data, target, cv, scoring):
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


def main():
    cv = ShuffleSplit(n_splits=7, test_size=.25, random_state=0)
    scoring = 'r2'
    models = get_models()
    params = get_params()
    diabetes = datasets.load_diabetes()
    data = diabetes.data
    target = diabetes.target
    for model_name in models.keys():
        print_cvs(models, params, model_name, data, target, cv, scoring)

if __name__ == '__main__':
    main()
