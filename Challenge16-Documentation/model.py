from sklearn.ensemble import RandomForestRegressor
import numpy as np

class EmissionPredictor:
    """
    A machine learning model that predicts emissions based on input features
    using a Random Forest Regressor.
    
    Parameters
    ----------
    n_estimators : int, optional (default=100)
        The number of trees in the random forest.
    """

    def __init__(self, n_estimators=100):
        self.model = RandomForestRegressor(n_estimators=n_estimators)

    def train(self, X, y):
        """
        Train the Random Forest model using the provided features and target values.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data (input features).

        y : array-like of shape (n_samples,)
            Target values (emissions to be predicted).

        Returns
        -------
        None
        """
        self.model.fit(X, y)

    def predict(self, X):
        """
        Predict emissions using the trained Random Forest model.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Input data for which to predict emissions.

        Returns
        -------
        predictions : ndarray of shape (n_samples,)
            Predicted emission values.
        """
        return self.model.predict(X)
