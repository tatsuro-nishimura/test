from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor

def print_cv_score(reg, data, target):
    cv = ShuffleSplit(n_splits=4, test_size=.25, random_state=0)
    scores = cross_val_score(reg, data, target.ravel(), cv=cv, scoring='r2')
    print('\n' + 'Cross Validation Score')
    print(scores.mean())


def main():
    diabetes = datasets.load_diabetes()

    print('\n' + 'decision tree')
    reg = DecisionTreeRegressor(max_depth=2)
    print_cv_score(reg, diabetes.data, diabetes.target)

    print('\n' + 'random forest')
    reg = RandomForestRegressor(max_depth=2)
    print_cv_score(reg, diabetes.data, diabetes.target)

    print('\n' + 'extra trees')
    reg = ExtraTreesRegressor(max_depth=2)
    print_cv_score(reg, diabetes.data, diabetes.target)

    print('\n' + 'adaboost')
    reg = AdaBoostRegressor(n_estimators=10)
    print_cv_score(reg, diabetes.data, diabetes.target)

    print('\n' + 'xgboost')
    reg = XGBRegressor(max_depth=2)
    print_cv_score(reg, diabetes.data, diabetes.target)

    print('\n' + 'SVM linear')
    reg = SVR(kernel='linear', C=1000)
    print_cv_score(reg, diabetes.data, diabetes.target)

    print('\n' + 'SVM poly')
    reg = SVR(kernel='poly', C=1000, gamma='auto', degree=3, epsilon=.1, coef0=1)
    print_cv_score(reg, diabetes.data, diabetes.target)

    print('\n' + 'SVM rbf')
    reg = SVR(kernel='rbf', C=1000, gamma=0.1)
    print_cv_score(reg, diabetes.data, diabetes.target)

    print('\n' + 'Multi-layer perceptron')
    reg = MLPRegressor(hidden_layer_sizes=(5,), activation='relu', solver='adam',
        learning_rate='adaptive', max_iter=1000, learning_rate_init=0.01,
        alpha=0.01, random_state=0)
    print_cv_score(reg, diabetes.data, diabetes.target)


if __name__ == '__main__':
    main()
