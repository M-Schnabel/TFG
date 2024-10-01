import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
from sklearn.tree import _tree
import numpy as np

# Define the function tree_to_code (From https://mljar.com/blog/extract-rules-decision-tree/)
def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    feature_names = [f.replace(" ", "_")[:-5] for f in feature_names]
    code = []

    def recurse(node, depth):
        indent = "    " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            code.append("{}if {} <= {}:".format(indent, name, np.round(threshold,2)))
            recurse(tree_.children_left[node], depth + 1)
            code.append("{}else:  # if {} > {}".format(indent, name, np.round(threshold,2)))
            recurse(tree_.children_right[node], depth + 1)
        else:
            code.append("{}return {}".format(indent, tree_.value[node]))

    recurse(0, 1)
    return code

# Define a function to generate code for all trees
def generate_decision_tree_code(rf_classifier, feature_names):
    tree_codes = []
    for i, tree in enumerate(rf_classifier.estimators_):
        code = tree_to_code(tree, feature_names)
        tree_codes.append('\n'.join(code))
    return tree_codes

# Step 1: Load the Data
df = pd.read_csv('features.csv')

# Step 2: Split the Data
X = df.drop('label', axis=1)  # Features
y = df['label']  # Labels

# Step 3: Split Data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Random Forest Classifier
rf_classifier = RandomForestClassifier(n_estimators=10, max_leaf_nodes=10, random_state=42)
rf_classifier.fit(X_train, y_train)

# Step 5: Evaluate the Model
y_pred = rf_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Generate code for all trees
tree_codes = generate_decision_tree_code(rf_classifier, feature_names=X.columns.tolist())

# Print the code for each tree
# for i, code in enumerate(tree_codes):
#     print(f"Tree {i+1}:\n{code}\n")

# Plot all trees in the Random Forest
for i in range(10):
    plt.figure(figsize=(10, 10))
    plot_tree(rf_classifier.estimators_[i], feature_names=X.columns, class_names=rf_classifier.classes_, filled=True)
    plt.title(f"Tree {i+1}")
    plt.show()

