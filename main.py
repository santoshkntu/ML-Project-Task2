# This is a sample Python script


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import requests
url ="https://data.gov.sg/api/action/datastore_search?resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84&q=jones"
result = requests.get(url).json()
# Try out the following codes
# Try to understand the result and figure out how is the data stored in json.
print(result.keys())
print(result['result'].keys())
print(result['result']['records'])

### Todo
# Print out the part where data is stored.

import requests
url ="https://data.gov.sg/api/action/datastore_search?resource_id=f9dbfc75-a2dc-42af-9f50-425e4107ae84&q=2019%2090%20Years%20Total%20Residents"
result = requests.get(url).json()
print(result['result']['records'][1])

import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
df = pd.read_csv("churning.csv")
# we use only the first 2 variables as features
# account length,number vmail messages
x = df.iloc[:, [0, 1]]
y = df.iloc[:,-1] # classification
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
classifier = AdaBoostClassifier(n_estimators=10, learning_rate=0.8, random_state=0, algorithm='SAMME')
classifier.fit(x, y)
y_pred = classifier.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
print(accuracy_score(y_test, y_pred))
while True:
    var1 = float(input("Enter value for account length:"))
    var2 = float(input("Enter value for number vmail messages:"))
    pred = classifier.predict([[var1, var2]])
    print(pred)
    if pred == [1]:
        print("Yes, likely will churn.")
    else:
        print("Unlikely will churn.")
    cont = input("Do you want to continue? y/n")
    if cont == "n":
        break
    