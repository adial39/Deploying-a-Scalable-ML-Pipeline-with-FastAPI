import pytest
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import train_model, compute_model_metrics, inference

# TODO: add necessary import
# Imports added above

# TODO: implement the first test. Change the function name and input as needed
def test_process_data_return_types():
    """
    Test that process_data returns expected types for X, y, encoder, and label binarizer.
    """
    data = pd.DataFrame({
        "workclass": ["Private", "Self-emp-not-inc"],
        "education": ["Bachelors", "HS-grad"],
        "age": [25, 38],
        "salary": [">50K", "<=50K"]
    })
    cat_features = ["workclass", "education"]
    X, y, encoder, lb = process_data(data, categorical_features=cat_features, label="salary", training=True)

    assert isinstance(X, np.ndarray), "X should be numpy ndarray"
    assert isinstance(y, np.ndarray), "y should be numpy ndarray"
    assert hasattr(encoder, "transform"), "encoder should have transform method"
    assert hasattr(lb, "transform"), "label binarizer should have transform method"

# TODO: implement the second test. Change the function name and input as needed
def test_train_model_algorithm():
    """
    Test the train_model function returns a RandomForestClassifier instance.
    """
    X_train = np.array([[0, 1], [1, 0], [1, 1]])
    y_train = np.array([0, 1, 1])
    model = train_model(X_train, y_train)

    from sklearn.ensemble import RandomForestClassifier
    assert isinstance(model, RandomForestClassifier), "Model should be a RandomForestClassifier"

# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics_values():
    """
    Test that compute_model_metrics outputs expected precision, recall, and f1 for perfect predictions.
    """
    y = np.array([0, 1, 1, 0])
    preds = np.array([0, 1, 1, 0])

    precision, recall, fbeta = compute_model_metrics(y, preds)

    assert precision == 1.0, "Precision should be 1.0 for perfect predictions"
    assert recall == 1.0, "Recall should be 1.0 for perfect predictions"
    assert fbeta == 1.0, "F1 should be 1.0 for perfect predictions"

