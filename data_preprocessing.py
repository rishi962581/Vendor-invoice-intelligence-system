import sqlite3
from sklearn.model_selection import train_test_split
import pandas as pd

def load_vendor_invoice_data(db_path: str):
    """
    Load vendor invoice data from SQLite database.
    """
    conn = sqlite3.connect(db_path)
    query = "SELECT * FROM vendor_invoice"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def prepare_features(df: pd.DataFrame):
    """
    Select features and target variable.
    """
    X = df[["Dollars"]]
    y = df["Freight"]
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split dataset into train and test sets.
    """
    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )

# Load data
df = load_vendor_invoice_data("vendor_invoice.db")

# Prepare data
X, y = prepare_features(df)

# Split data
X_train, X_test, y_train, y_test = split_data(X, y)

print("X Train Shape:", X_train.shape)
print("X Test Shape:", X_test.shape)
print("Y Train Shape:", y_train.shape)
print("Y Test Shape:", y_test.shape)