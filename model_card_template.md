# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
This model is a Random Forest classifier trained to predict whether an individual's income exceeds $50K/year using the UCI Census Income dataset. The model preprocesses categorical features using one-hot encoding and uses a label binarizer for the label.

## Intended Use
The model is intended for educational and experimental purposes to demonstrate building an income classification pipeline. It should not be used for critical decision-making without further validation and fairness assessment.

## Training Data
The model was trained on the Census Income dataset (`census.csv`) containing demographic and employment attributes. The dataset was split into 80% training and 20% test sets.

## Evaluation Data
Evaluation was conducted on the held-out 20% test dataset. Performance was also measured on data slices corresponding to unique values of the categorical features to assess granular performance variations.

## Metrics
The model was evaluated using Precision, Recall, and F1 Score metrics.

### Overall performance on the test set:
- **Precision:** 0.7391
- **Recall:** 0.6384
- **F1 Score:** 0.6851

### Sample slice performance by `workclass` feature:

| workclass   | Count | Precision | Recall  | F1 Score |
|-------------|-------|-----------|---------|----------|
| ? (Unknown) | 389   | 0.6800    | 0.4048  | 0.5075   |
| Federal-gov | 191   | 0.7971    | 0.7857  | 0.7914   |
| Local-gov   | 387   | 0.7500    | 0.6818  | 0.7143   |
| Private     | 4,578 | 0.7362    | 0.6384  | 0.6838   |
| Self-emp-inc| 212   | 0.7586    | 0.7458  | 0.7521   |

*(Full slice performance recorded in `slice_output.txt`)*

## Ethical Considerations
The model may reflect biases present in training data, particularly related to underrepresented groups or missing data (e.g., workclass "?"). Careful evaluation for fairness and bias is necessary before real-world application.

## Caveats and Recommendations
- Recall is low for some slices such as unknown workclass ("?") indicating the model struggles with these instances.
- The model lacks hyperparameter tuning and advanced preprocessing.
- This is a baseline model intended for learning; do not deploy without further validation.
- Consider collecting more balanced data and implementing fairness-aware techniques in production scenarios.
