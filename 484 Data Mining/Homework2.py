# Theodore Church
# G01127117
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split


def main():
    # read data in
    # TODO: NOTE: These need to be changed to your own filepath
    data = pd.read_csv(r'C:\Users\Grim\PycharmProjects\CS484\excel_train.csv', header=None)
    test = pd.read_csv(r'C:\Users\Grim\PycharmProjects\CS484\1614291944_0717268_test_no_label.csv', header=None)
    # copy last column to a new array
    answer = data.iloc[:, 54]
    # drop the last column because it's just results
    data = data.iloc[:, :-1]
    print("Running KNN.")
    # KNN ran at 0.77 accuracy the first attempt
    knn(data, answer, test)
    print("KNN done.\nRunning Decision Tree.")
    # decision tree ran at 0.72 accuracy the first attempt
    decision_tree(data, answer, test)
    print("Decision Tree Done.\nRunning Byes.")
    # gaussian byes ran at 0.44 accuracy the first attempt
    byes(data, answer, test)
    print("Byes Done.")
    print("Accuracy detection KNN.")
    # cross validation for KNN, computes accuracy of various K values. K = 1 should be optimal, I used 2
    accuracy(data, answer)
    print("Done.")


# this should be named cross validation
def accuracy(data, answer):
    X_train, X_test, y_train, y_test = train_test_split(data, answer, test_size=0.20)
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    error = []
    for i in range(1, 40):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        pred_i = knn.predict(X_test)
        error.append(np.mean(pred_i != y_test))
    print(error)


# knn function. Prints answers to "knnAnswer.txt"
def knn(data, answer, test):
    scalar = StandardScaler()
    scalar.fit(data)
    x_data = scalar.transform(data)
    x_test = scalar.transform(test)
    # I misread my data and used k = 2, upon review k=1 should be better.
    classifier = KNeighborsClassifier(n_neighbors=2)
    classifier.fit(x_data, answer)
    results = classifier.predict(x_test)
    f = open("knnAnswer.txt", "w")
    np.savetxt(f, results, fmt='%d')
    f.close()


# decision tree function. Prints answers to "dtreeAnswer.txt"
def decision_tree(data, answer, test):
    scalar = StandardScaler()
    scalar.fit(data)
    x_data = scalar.transform(data)
    x_test = scalar.transform(test)
    classifier = tree.DecisionTreeClassifier(criterion='entropy', max_depth=7)
    classifier = classifier.fit(x_data, answer)
    results = classifier.predict(x_test)
    f = open("dtreeAnswer.txt", "w")
    np.savetxt(f, results, fmt="%d")
    f.close()


# Byes function. Prints answers to "byesAnswers.txt"
def byes(data, answer, test):
    scalar = StandardScaler()
    scalar.fit(data)
    # mistake: I didn't run byes with the scaled data. This could be why it scored so low.
    # x_data = scalar.transform(data)
    # x_test = scalar.transform(test)
    # classifier = GaussianNB()
    # classifier.fit(data, answer)
    # results = classifier.predict(test)
    x_data = scalar.transform(data)
    x_test = scalar.transform(test)
    classifier = GaussianNB()
    classifier.fit(x_data, answer)
    results = classifier.predict(x_test)
    f = open("byesAnswers.txt", "w")
    np.savetxt(f, results, fmt="%d")
    f.close()


if __name__ == '__main__':
    main()
