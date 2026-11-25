# PROGRAM
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42)

model = DecisionTreeClassifier(criterion='entropy', random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", round(accuracy_score(y_test, y_pred), 4))
print("\nDecision Tree Rules:")
print(export_text(model, feature_names=iris.feature_names))

sample = [[5.1, 3.5, 1.4, 0.2]]
print("Prediction for", sample, "->", iris.target_names[model.predict(sample)[0]])

# OUTPUT
# Accuracy: 0.9778
#
# Decision Tree Rules:
# |--- petal length (cm) <= 2.45
# |   |--- class: 0
# |--- petal length (cm) > 2.45
# |   |--- petal length (cm) <= 4.75
# |   |   |--- petal width (cm) <= 1.60
# |   |   |   |--- class: 1
# |   |   |--- petal width (cm) > 1.60
# |   |   |   |--- class: 2
# |   |--- petal length (cm) > 4.75
# |   |   |--- petal length (cm) <= 5.15
# |   |   |   |--- petal width (cm) <= 1.75
# |   |   |   |   |--- sepal width (cm) <= 2.35
# |   |   |   |   |   |--- class: 2
# |   |   |   |   |--- sepal width (cm) > 2.35
# |   |   |   |   |   |--- petal length (cm) <= 5.05
# |   |   |   |   |   |   |--- class: 1
# |   |   |   |   |   |--- petal length (cm) > 5.05
# |   |   |   |   |   |   |--- sepal length (cm) <= 6.15
# |   |   |   |   |   |   |   |--- class: 1
# |   |   |   |   |   |   |--- sepal length (cm) > 6.15
# |   |   |   |   |   |   |   |--- class: 2
# |   |   |   |   |--- petal width (cm) > 1.75
# |   |   |   |   |   |--- sepal width (cm) <= 3.10
# |   |   |   |   |   |   |--- class: 2
# |   |   |   |   |   |--- sepal width (cm) > 3.10
# |   |   |   |   |   |   |--- class: 1
# |   |   |--- petal length (cm) > 5.15
# |   |   |   |--- class: 2
#
# Prediction for [[5.1, 3.5, 1.4, 0.2]] -> setosa
