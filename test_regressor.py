from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
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

    print('\n' + 'extra tree')
    reg = ExtraTreesRegressor(max_depth=2)
    print_cv_score(reg, diabetes.data, diabetes.target)

    print('\n' + 'xgboost')
    reg = XGBRegressor(max_depth=2)
    print_cv_score(reg, diabetes.data, diabetes.target)


if __name__ == '__main__':
    main()
