# ROSSMAN Store Sales Prediction - DSR Mini Competition
Building a ml algorithim for forcast sales
​
* Contents
​
    * Overview
    * Objective
    * Dataset
    * Approach
    * Evaluation
    * Dependencies
    * Usage
    * Project Structure
    * Results
    * Acknowledgments
​
# Overview
​
This repository contains the solution and code for the "Rossmann Store Sales Prediction" DSR Mini competition. The goal of this competition is to predict the sales for Rossmann stores for a given period, considering various features such as promotions, holidays, and store information.
​
# Objective
​
The objective of this project is to build a predictive model that accurately forecasts the sales for each store in the test set.
​
# Dataset
​
* The dataset provided for this competition consists of two main files:
​
    * train.csv: Contains historical data for each store, including sales, promotions, holidays, etc.
    * test.csv: Contains data for the prediction period, where sales need to be forecasted.
For this competition, an additional store.csv file is provided, which contains store-specific information.
​
# Approach
​
1. Data Exploration: Understanding the structure of the dataset, handling missing values, and analyzing data distributions.
2. Feature Engineering: Creating additional relevant features to improve model performance.
3. Data Preprocessing: Handling categorical variables, scaling, and splitting the dataset into training and validation sets.
4. Model Selection: Trying out various regression models like XGBoost, RandomForest, etc.
5. Model Tuning: Fine-tuning the hyperparameters of the selected model.
6. Model Evaluation: Evaluating the model's performance on the validation set using appropriate evaluation metrics.
7. Final Predictions: Making predictions on the test set using the trained model.
​
# Evaluation
​
The submissions are evaluated using the Root Mean Squared Percentage Error (RMSPE) metric, which penalizes large errors.
RMSPE is calculated using:
![](./assets/rmspe-errorcheck.png)
​
​
# Dependencies
​
    ° Python 3.10
    ° pandas
    ° numpy
    ° scikit-learn
    ° xgboost
    ° matplotlib
    ° seaborn
​
# Usage
​
Clone the repository.
Install the required dependencies using pip install -r requirements.txt.
```bash
#  during the competition run
python data.py
​
#  at test time run
python data.py --test 1
```
Find the dataset from data/ directory.
Execute the Jupyter notebook rossmann_store_sales.py to run the code step-by-step.
​
# Project Structure
├── data
│   ├── df_merged_optimized.csv
│   ├── store.csv
│   └── train.csv
├── notebooks
│   ├── baseline_model.ipynb
│   ├── cleaning.ipynb
│   ├── visualizations.ipynb
├── src
│   ├── data_cleaner.py
│   ├── data.py
├── .gitignore
└── README.md
​
​
# Results
​
The final model achieved an RMSPE of ____ on the validation set and ____ on the test set.
​
# Acknowledgments
​
Special thanks to DSR, Kaggle and Rossmann for providing the dataset and hosting the competition.
​
