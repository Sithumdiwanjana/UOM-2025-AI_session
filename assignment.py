# --- 1. Import Libraries ---
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder
import numpy as np

# --- 2. Load the Dataset ---
print("Loading data...")
try:
    # Ensure 'sleep_lifestyle.csv' is in the same directory as your notebook
    df = pd.read_csv('sleep_lifestyle.csv')
    print(f"Data loaded successfully with {df.shape[0]} rows.")
except FileNotFoundError:
    print("FATAL ERROR: 'sleep_lifestyle.csv' not found. Please check the file path.")
    exit()

# --- 3. Data Preprocessing and Feature Engineering ---

# A. Drop the 'Person ID' column as it is an identifier
df = df.drop('Person ID', axis=1)

# B. Feature Engineering: Handle 'Blood Pressure' column
# Split the 'Blood Pressure' string (e.g., '120/80') into two numeric columns
print("Processing 'Blood Pressure' column...")
df[['Systolic BP', 'Diastolic BP']] = df['Blood Pressure'].str.split('/', expand=True).astype(float)
df = df.drop('Blood Pressure', axis=1)

# C. Target Variable Encoding ('Sleep Disorder')
# The target variable is categorical, so we must convert it to numerical labels (0, 1, 2)
le = LabelEncoder()
df['Sleep Disorder Encoded'] = le.fit_transform(df['Sleep Disorder'])

# Check the mapping for reference
print("\nTarget Variable Mapping:")
target_map = dict(zip(le.transform(le.classes_), le.classes_))
for k, v in target_map.items():
    print(f"  {v}: {k}")

# D. One-Hot Encoding for remaining Categorical Features
# Convert nominal categories like 'Gender', 'Occupation', and 'BMI Category' into numerical features
categorical_cols = ['Gender', 'Occupation', 'BMI Category']
df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

# --- 4. Define Features (X) and Target (y) ---
# X: Features (all columns except the original and encoded targets)
# y: Target (the encoded 'Sleep Disorder' column)
X = df.drop(['Sleep Disorder', 'Sleep Disorder Encoded'], axis=1)
y = df['Sleep Disorder Encoded']

# --- 5. Split Data into Training and Testing Sets ---
# Use a 70% training and 30% testing split, maintaining the class distribution (stratify)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(f"\nTraining set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")

# --- 6. Model Training (Random Forest Classifier) ---
print("\nTraining Random Forest Classifier...")
# Initialize and train the model
model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
model.fit(X_train, y_train)
print("Model training complete.")

# --- 7. Model Evaluation ---
# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate and print metrics
print("\n--- Model Evaluation ---")
accuracy = accuracy_score(y_test, y_pred)
print(f"Overall Accuracy: {accuracy:.4f}\n")

print("Classification Report:")
# Use the label encoder classes for clear output
print(classification_report(y_test, y_pred, target_names=le.classes_))

# --- 8. Feature Importance ---
# Identify which features are most critical for the model's prediction
print("\n--- Feature Importance ---")
feature_importances = pd.Series(model.feature_importances_, index=X.columns)

# Display the top 5 most important features
print("Top 5 Most Important Features:")
print(feature_importances.sort_values(ascending=False).head(5))