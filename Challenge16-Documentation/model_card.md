# Model Card: EmissionPredictor

## Model Details
- **Model Type**: Random Forest Regressor
- **Framework**: scikit-learn
- **Purpose**: Predict emissions based on structured input data.
- **Author**: Wael Lejmi
- **Version**: 1.0

## Intended Use
This model is designed to assist researchers or regulatory bodies in estimating emissions based on measurable parameters. It can be used in:
- Environmental impact studies
- Industrial emissions audits

## Training Data
- **Source**: Egypt Carbon Emission Dataset
- **Format**: Preprocessed CSV (Excel-compatible) 
- **Size**: N/A
- **Preprocessing**: The dataset has been cleaned and encoded to be suitable for training a Random Forest model. Categorical variables are encoded; missing values are handled. Normalization is not required.


## Evaluation Data
- **Split**: 20% of the Egypt Carbon Emission Dataset is reserved as the validation set.
- **Methodology**: The evaluation data is held out before training. Alternatively, k-fold cross-validation can be used for robust evaluation.


## Metrics
- **R² Score**: Measures proportion of variance explained.
- **Mean Absolute Error (MAE)**: Measures average magnitude of errors.
- **Mean Squared Error (MSE)**: Penalizes larger errors more heavily.

## Ethical Considerations
- **Bias**: Model accuracy may vary across different subgroups if the training data is not representative.
- **Transparency**: As a black-box ensemble model, interpretability is limited.
- **Accountability**: Predictions should be reviewed by domain experts before making policy or safety decisions.

## Caveats and Recommendations
- This model does not explain *why* emissions occur. It only estimates *how much*.
- Ensure consistent feature engineering between training and inference.
- Not suitable for extrapolation far outside the training data range.

