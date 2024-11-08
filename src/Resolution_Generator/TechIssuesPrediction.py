# Analyze past incident data to identify patterns and predict potential issues before they escalate.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

def feature_engineering(df):
    # Example: Using 'description' as text feature and 'category' as target
    X = df['description']
    y = df['category']
    return X, y

def train_model(X, y):
    # Text vectorization
    vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
    X_vect = vectorizer.fit_transform(X)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X_vect, y, test_size=0.2, random_state=42)
    
    # Model training
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    # Predictions
    y_pred = clf.predict(X_test)
    
    # Evaluation
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    
    # Save model and vectorizer
    joblib.dump(clf, 'rf_classifier.joblib')
    joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')
    
    return clf, vectorizer

# Example usage
# clean_df = preprocess_data(file_path)
# X, y = feature_engineering(clean_df)
# clf, vectorizer = train_model(X, y)