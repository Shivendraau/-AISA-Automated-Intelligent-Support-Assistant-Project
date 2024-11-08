# Clean and preprocess incident data to ensure quality for ML and GenAI models.

import pandas as pd
import re
import os

def load_data(file_path):
    try:
        df = pd.read_csv("C:/Users/shive/OneDrive/Automated Intelligent Support Assistant/-AISA-Automated-Intelligent-Support-Assistant-Project/incident_data.csv", encoding='utf-8', on_bad_lines='skip')
        print(f"Data loaded successfully from {file_path}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def remove_pii(text):
    if not isinstance(text, str):
        return text
    # Redact SSN, phone numbers, and emails
    text = re.sub(r'\b\d{3}-\d{2}-\d{4}\b', 'SSN_REDACTED', text)
    text = re.sub(r'\b\d{10}\b', 'PHONE_REDACTED', text)
    text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'EMAIL_REDACTED', text)
    return text

def clean_data(df):
    pii_columns = ['description', 'resolution']
    for col in pii_columns:
        if col in df.columns:
            df[col] = df[col].astype(str).apply(remove_pii)
            print(f"PII removed from column: {col}")
        else:
            print(f"Column {col} not found in DataFrame")
    
    # Handle missing values
    df.fillna('', inplace=True)
    print("Missing values handled")
    
    # Additional cleaning steps can be added here
    return df

def save_clean_data(df, output_path):
    try:
        df.to_csv(output_path, index=False, encoding='utf-8')
        print(f"Clean data saved to {output_path}")
    except Exception as e:
        print(f"Error saving clean data: {e}")

def preprocess_data(file_path, output_path):
    data = load_data(file_path)
    if data is not None:
        clean_df = clean_data(data)
        save_clean_data(clean_df, output_path)
        return clean_df
    else:
        print("Data preprocessing failed")
        return None

if __name__ == "__main__":
    input_file = "C:/Users/shive/OneDrive/Automated Intelligent Support Assistant/-AISA-Automated-Intelligent-Support-Assistant-Project/incident_data.csv"  # Update with your actual file
    output_file = "C:/Users/shive/OneDrive/Automated Intelligent Support Assistant/-AISA-Automated-Intelligent-Support-Assistant-Project/clean_incident_data.csv"
    
    clean_df = preprocess_data(input_file, output_file)
    if clean_df is not None:
        print("First 5 rows of the clean data:")
        print(clean_df.head())