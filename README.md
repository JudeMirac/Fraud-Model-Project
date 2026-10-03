## Fraud Risk Modeling & Decision System

## Table of Contents
- [Project Overview](#project-overview)
- [Objective](#objective)
- [Analytics Workflow](#analytics-workflow)
- [Key Results](#key-results)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Tools Used](#tools-used)

## Project Overview 

This project walks through an end-to-end data science workflow using a fraud risk dataset. The goal here was not just to examine, summarize, interpret and predict fraud, but to turn the prediction into real-world decisions. In other words, instead of stopping at model accuracy, I focused on the prescriptive analytics, where predicted scores are used to decide whether a transaction should be allowed, reviewed, or blocked. 

## Objective

The main objectives of this project:
 - Identify high-risk transactions
 - Reduce fraud losses
 - Limit unnecessary manual reviews
 - Maintain good customer experience

A key challenge in the fraud dataset is the highly imbalanced target variable and model probabilities being compressed. The project addresses that issue by using a percentile-based-ranking rather than fixed probability thresholds. 

## Analytics Workflow

## 1. Descriptive Analytics
  - Examine overall fraud rate
  - Analyze fraud by merchant, category, payment method, and device type
  - Look at transaction velocity and prior chargeback behavior

## 2. Diagnostic Analytics
  - Explore relationships between features and fraud
  - Create interaction features to capture combined risk signals
  - Identify variables that are most associated with fraud risk

## 3. Predictive Analytics
  - Test multiple models, including logistic regression and RandomForest
  - Address class imbalance using class weighting
  - Tune decision thresholds and evaluate ROC-AUC

The Random Forest model showed strong ranking performance but produced tightly clustered probability scores.

## 4. Prescriptive Analytics
Instead of using fixed probability cut-offs, fraud scores are converted into percentile ranks. These percentiles are then grouped into risk tiers:
 - **Low** → bottom 80% = ALLOW
 - **Medium** → 80-95% = REVIEW
 - **High** → top 5% = BLOCK

This ensures:
 - Most transactions are automatically approved
 - Review volume stays manageable
 - The highest risk transactions are prioritized for blocking

## Key Results
 - Fraud capture rate: 61% of fraudulent transactions were intercepted through review or blocking
 - Fraud rates increased consistently from low to high risk tiers, showing that the ranking-based policy was effective

## Project Structure
```
Fraud-Model-Project/
├── Data/
│   └── fraud_risk_dataset.csv       # Fraud risk dataset
├── Notebooks/
│   ├── Descriptive.ipynb            # Exploratory data analysis
│   ├── Diagnostic.ipynb             # Feature relationships analysis
│   ├── Modeling_Fraud.ipynb         # Model training and evaluation
│   ├── Prescriptive.ipynb           # Decision policy implementation
│   ├── Feature_Engineering/
│   │   └── Feature_eng.py           # Feature engineering functions
│   └── Model/
│       └── best_model               # Trained Random Forest model
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/JudeMirac/Fraud-Model-Project.git
cd Fraud-Model-Project
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

The analysis is divided into four main notebooks that should be executed in order:

1. **Descriptive.ipynb** - Explore the fraud dataset and understand basic patterns
2. **Diagnostic.ipynb** - Analyze feature relationships and create interaction features
3. **Modeling_Fraud.ipynb** - Train and evaluate predictive models
4. **Prescriptive.ipynb** - Implement the risk-based decision policy

To run the notebooks:
```bash
jupyter notebook
```

Navigate to the `Notebooks/` directory and open the desired notebook.

## Tools Used
- **Python** - Programming language
- **pandas, numpy** - Data manipulation and analysis
- **scikit-learn** - Machine learning models and evaluation
- **jupyter notebook** - Interactive analysis environment
- **joblib** - Model serialization

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
