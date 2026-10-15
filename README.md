# Fraud Risk Modeling & Decision System

## Table of Contents

- [Project Overview](#project-overview)
- [Objective](#objective)
- [Analytics Workflow](#analytics-workflow)
- [Key Results](#key-results)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Tools Used](#tools-used)
- [License](#license)
- [Contributing](#contributing)

## Project Overview

This project walks through an end-to-end data science workflow using a fraud risk dataset. The goal is to examine, summarize, interpret, and predict fraud, then use model scores to propose whether a transaction should be allowed, reviewed, or blocked. This is an offline analysis of a decision policy; it does not demonstrate a deployed system or realized loss reductions.

## Objective

The main objectives of this project:

- Identify high-risk transactions
- Reduce fraud losses
- Limit unnecessary manual reviews
- Maintain a good customer experience

The dataset has an imbalanced target, which the Random Forest model addresses through class weighting. The prescriptive analysis uses percentile-based ranking to allocate transactions to risk tiers when scores are tightly clustered. Ranking controls the intended action volumes; it does not correct class imbalance or calibrate probabilities.

## Analytics Workflow

### 1. Descriptive Analytics

- Examine overall fraud rate
- Analyze fraud by merchant, category, payment method, and device type
- Look at transaction velocity and prior chargeback behavior

### 2. Diagnostic Analytics

- Explore relationships between features and fraud
- Create interaction features to capture combined risk signals
- Identify variables that are most associated with fraud risk

### 3. Predictive Analytics

- Train and tune a Random Forest classifier (logistic regression is imported but not fitted in the modeling notebook)
- Address class imbalance using class weighting
- Tune decision thresholds and evaluate ROC-AUC

The modeling notebook's saved output reports a probability-based ROC-AUC of approximately 0.720 on its test split. The prescriptive notebook shows tightly clustered scores.

### 4. Prescriptive Analytics

Instead of using fixed probability cut-offs, fraud scores are converted into percentile ranks. These percentiles are then grouped into the following intended risk tiers:

- **Low** → bottom 80% = ALLOW
- **Medium** → above the 80th through the 95th percentile = REVIEW
- **High** → top 5% = BLOCK

The intended allocation is 80% ALLOW, 15% REVIEW, and 5% BLOCK. Because the notebook assigns average ranks to tied scores, exact proportions can vary. The tiers prioritize transactions by relative score; they do not establish that low-risk transactions are fraud-free.

## Key Results

- The saved prescriptive output reports approximately **61% fraud capture**: the fraction of labeled fraudulent transactions assigned to REVIEW or BLOCK in that offline analysis.
- Saved fraud rates increase from **3.55%** in the low tier to **18.13%** in the medium tier and **34.00%** in the high tier.

These are historical notebook outputs, not verified production outcomes or an independent held-out policy evaluation. The prescriptive notebook scores the full source dataset, which includes training records. The modeling notebook also selects its F1 threshold using the test labels, so the resulting threshold metrics are not an unbiased final evaluation. In addition, the saved decision outputs are inconsistent with the checked-in decision-mapping cells; see the usage notes below. These results have not been recomputed.

## Project Structure

```
Fraud-Model-Project/
├── Data/
│   └── fraud_risk_dataset.csv       # Fraud risk dataset
├── Notebooks/
│   ├── Descriptive.ipynb            # Exploratory data analysis
│   ├── Diagnostic.ipynb            # Feature relationships analysis
│   ├── Modeling_Fraud.ipynb         # Model training and evaluation
│   ├── Prescriptive.ipynb           # Decision policy implementation
│   ├── Feature_Engineering/
│   │   └── Feature_eng.py           # Feature engineering functions
│   └── Model/
│       └── best_model               # Serialized Random Forest pipeline
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
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

Or in Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

The analysis is organized into four notebooks. Read them in this order; apply the path and decision-mapping corrections below before attempting a fresh run:

1. **Descriptive.ipynb** - Explore the fraud dataset and understand basic patterns
2. **Diagnostic.ipynb** - Analyze feature relationships and create interaction features
3. **Modeling_Fraud.ipynb** - Train and evaluate predictive models
4. **Prescriptive.ipynb** - Implement the risk-based decision policy

To run the notebooks:

```bash
cd Notebooks
jupyter notebook
```

Open the desired notebook with its kernel working directory set to `Notebooks/`.

### Paths required for a fresh run

The checked-in notebooks still contain author-specific absolute paths or bare filenames that do not match the repository layout. With `Notebooks/` as the working directory:

- Replace each CSV load path with `../Data/fraud_risk_dataset.csv`.
- Before `from Feature_eng import add_interactions` in the modeling and prescriptive notebooks, add the feature module directory to the import path:

  ```python
  import sys
  from pathlib import Path

  sys.path.insert(0, str(Path("Feature_Engineering").resolve()))
  from Feature_eng import add_interactions
  ```

- Change the modeling notebook's export to `joblib.dump(best_estimator, "Model/best_model")` and the prescriptive load to `joblib.load("Model/best_model")`. Training and exporting will overwrite that model artifact.

### Decision-mapping limitation

The initial prescriptive decision cell passes numeric scores to a function expecting uppercase tier labels, producing all ALLOW decisions. A later function uses lowercase tiers but returns `Review` and is never applied to refresh `df["decision"]`. Consequently, running the committed cells in order does not reproduce the saved 61% capture output.

After the final percentile-based `risk_tier` assignment, replace the later decision-mapping cell with:

```python
df["decision"] = df["risk_tier"].map(
    {"low": "ALLOW", "medium": "REVIEW", "high": "BLOCK"}
)
df["decision"].value_counts()
```

Then rerun the evaluation cells to calculate results from the refreshed decisions. The historical metrics above should not be treated as guaranteed rerun results.

## Tools Used

- **Python** - Programming language
- **pandas, numpy** - Data manipulation and analysis
- **scikit-learn** - Machine learning models and evaluation
- **jupyter notebook** - Interactive analysis environment
- **matplotlib, seaborn** - Visualization
- **joblib** - Model serialization

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
