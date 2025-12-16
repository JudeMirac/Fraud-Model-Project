## Fraud Risk Modeling & Decsision System

## Project Overview 

This project walks through an end-to-end data science workflow using a fraud risk dataset. The goal here was not just to examine, summarize, interpret and predict fraud, but to turn the prediction into real world decisions. 
In otherwords, instead of stopping at model accuracy, I focused on the prescriptive analytics, where predicted scores are used to decide whether a transactions should be allowed, reviewed, or blocked. 

## Objective

The main objectives of this project: 
 - identify high risk transactions
 - Reduce fraud losses
 - Limit unneccessary manaual reviews
 - Maintain good customer experience

A key challenge in the fraud dataset is the highly imbalanced target variable and model probabilties being compressed. The Project adresses that issue by using a percentile-based-rankinng rather than fixed probability thresholds 

## Analytics Workflow
## 1. Descriptive Analytics
  - Examine overalll fraud rate
  - Analyzed fraud by merchant, category, pament method, and device type
  - Looked at transaction velocity and prior chargeback behavior
## 2. Diagnotic Analytics
  - Explored relationships between features and fraud
  - Created interaction features to capture combibed risk signals
  - Identified variables that were most associated with fraud risk
## 3. Predictive Analytics 
  - Tested multiple models, including logistic regression and RandomForest
  - Adressed class imbalance using class weighing
  - Tuned decision thresholds and evaluated ROC-AUC

The Random Forest Model showed strong ranking perfomrnace but produced tightly clustered probability score.
## 4. prescriptive Analytics 
Instead of using fixed probabiliy cutt offs, fraud scores were converted into percentile ranks. These percentiles were then grouped into risk tiers:
 - Low -> bottom 80% = ALLOW
 - Medium -> 80 - 95% = REVIEW
 - High -> top 5% = BLOCK

This ensures:
 - Most transactions are automatically approved
 - Review volume stays manageable
 - The highest risk transactions are prioritiezed for blocking

# Key Results 
 - Fraud capture rate: 61% of transactions were intercepted through review or blocking
 - Fraud rates increased consistenlty from low to high risk tiers, showing that the ranking based policy was effective

# Tools Used
- Python
- pandas, numpy
- scikit-learn
- jupyter notebook
- joblib
