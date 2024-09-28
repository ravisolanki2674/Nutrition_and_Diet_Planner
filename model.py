import panda as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import make_pipeline

# Load dataset
data = pd.read_csv('diet_data.csv')

# Preprocessing
X = data[['calories', 'protein', 'fats', 'carbs', 'dietary_goal']]
y = data['recommendation']

# Convert categorical data to numeric
X['dietary_goal'] = LabelEncoder().fit_transform(X['dietary_goal'])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print(f'Model Accuracy: {accuracy:.2f}')

# Save the model
import joblib
joblib.dump(model, 'diet_model.pkl')
