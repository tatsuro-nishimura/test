from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.linear_model import Perceptron
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import numpy as np

def logisticfunc(r):
    return(1/(1 + np.exp(-r)))

def print_cvs_and_cm(iris, clf, perc = 0, mlp = 0):
    cv = ShuffleSplit(n_splits=4, test_size=.25, random_state=0)
    scores = cross_val_score(clf, iris.data, iris.target, cv=cv, scoring='f1_macro')
    print('\n' + 'cross validation score')
    print(scores.mean())
    clf.fit(iris.data, iris.target)
    print('\n' + 'confusion matrix')
    print(confusion_matrix(iris.target, clf.predict(iris.data)))
    if mlp == 1:
        print('confusion matrix from coefficients')
        print(confusion_matrix(iris.target,
              np.argmax(logisticfunc(np.dot(logisticfunc
                        (np.dot(np.array(iris.data), clf.coefs_[0])
                         + clf.intercepts_[0]), clf.coefs_[1])
                         + clf.intercepts_[1]), axis=1)))
    if perc == 1:
        print('confusion matrix from coefficients')
        print(confusion_matrix(iris.target, np.argmax(np.dot(clf.coef_,
              np.array(iris.data).T).T + clf.intercept_, axis=1)))


def main():
    iris = load_iris()

    print('\n' + 'perceptron')
    clf = Perceptron(n_iter=200)
    print_cvs_and_cm(iris, clf, perc=1)

    print('\n' + 'decision tree')
    clf = DecisionTreeClassifier(max_depth=2)
    print_cvs_and_cm(iris, clf)

    print('\n' + 'randomforest')
    clf = RandomForestClassifier(n_estimators=10, max_depth=2)
    print_cvs_and_cm(iris, clf)

    print('\n' + 'adaboost')
    clf = AdaBoostClassifier(n_estimators=10)
    print_cvs_and_cm(iris, clf)

    print('\n' + 'gradient boost')
    clf = GradientBoostingClassifier(n_estimators=10)
    print_cvs_and_cm(iris, clf)

    print('\n' + 'SVM linear')
    clf = SVC(kernel='linear', probability=True,
              decision_function_shape='ovr')
    print_cvs_and_cm(iris, clf)

    print('\n' + 'SVM poly')
    clf = SVC(kernel='poly', probability=True, degree=3)
    print_cvs_and_cm(iris, clf)

    print('\n' + 'SVM rbf')
    clf = SVC(kernel='rbf', probability=True)
    print_cvs_and_cm(iris, clf)

    print('\n' + 'Multi-layer perceptron')
    clf = MLPClassifier(hidden_layer_sizes=(10,), activation='logistic',
                        max_iter=2000, solver='adam')
    print_cvs_and_cm(iris, clf, mlp=1)

if __name__ == '__main__':
    main()
