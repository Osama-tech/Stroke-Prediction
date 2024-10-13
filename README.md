Overview
This project explores the use of various machine learning and deep learning techniques to predict stroke based on clinical data. The models used include traditional ML algorithms and advanced DL models to achieve high prediction accuracy.

Models Used:
- Random Forest (RF)
- Decision Tree (DT)
- Extreme Gradient Boosting (XGBoost)
- Gradient Boosting (G-Boost)
- K-Nearest Neighbors (KNN)
- Logistic Regression (LR)
- Gaussian Naive Bayes (Gauss-NB)
- AdaBoost
- Support Vector Machine (SVM)
- Deep Neural Network (DNN)

Data Preprocessing:
- Handling Missing Values: Multivariate Imputation by Chained Equations (MICE)
- Balancing Classes: Adaptive Synthetic Sampling (ADASYN)
- Data Splitting: 5 different split strategies were used to evaluate the models.

Evaluation Metrics:
The following metrics were used to evaluate the performance of the models:

- Accuracy
- Precision
- Recall (Sensitivity)
- F1-Score
- Specificity
- Area Under the Curve (AUC)

Best Model:
- The Gradient Boosting (G-Boost) model with the 70-20-10 split ratio achieved the highest accuracy (99%), precision, F1-score, and AUC, making it the best model for stroke prediction in this study.

Future Work:
- Integration of Image Data: Combining clinical data with brain scans like CT and MRI.
- Incorporation of Additional Data Sources: Including genetic data, medical histories, and lifestyle factors.
- Advanced Feature Engineering: Exploring deep learning for feature generation.
- Deep Learning Architectures: Using CNNs and RNNs for image and sequential data.