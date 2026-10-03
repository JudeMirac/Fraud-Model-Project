# Fraud risk modeling: Codex working instructions

## Scope

Maintain the notebook-based fraud analysis, model evaluation, and risk-tier workflow.

The user's current request takes precedence. This package authorizes no project changes by itself. Preserve the existing analytical intent and do not invent metrics, source data, successful tests, or model results.

## Repository baseline

Repository: JudeMirac/Fraud-Model-Project
Inspected branch: main
Inspected commit: 370f3857b561f9a74d8ca5b21e6cae4c8b7a3964
This is a remote source assessment, not proof of a clean local worktree. Recheck branch, current HEAD, existing changes, and any nested instructions before implementation.

- Notebooks/Descriptive.ipynb, Diagnostic.ipynb, Modeling_Fraud.ipynb, and Prescriptive.ipynb cover the analysis stages.
- Notebooks/Feature_Engineering/Feature_eng.py contains feature transformations; Notebooks/Model/best_model is a serialized artifact.
- Data/fraud_risk_dataset.csv is the input; requirements.txt lists notebook and modeling dependencies.

## Multi-agent workflow

Keep the lead focused on planning, integration, ambiguous decisions, and final review.

- fraud_explorer: Read-only repository mapping, dependency tracing, data-flow inspection, and targeted investigation. Model: gpt-6-luna; reasoning: high.
- fraud_worker: Small, clearly scoped code, notebook, documentation, and configuration changes. Model: gpt-6-luna; reasoning: high.
- fraud_engineer: Complex implementation, cross-file debugging, data-pipeline failures, and integration decisions. Model: gpt-6.1-sol; reasoning: medium.
- fraud_reviewer: Independent review for correctness, regressions, data leakage, reproducibility, and missed requirements. Model: gpt-6.1-sol; reasoning: medium.

Use one or two specialists for ordinary work. Delegate only bounded work with a clear output. Parallelize independent tasks and never give concurrent writers overlapping files. Ask the engineer to handle hard failures rather than repeatedly widening a routine worker's scope. Use independent review for meaningful analytical or functional changes. Do tiny tasks directly.

Read the relevant source before editing. Preserve unrelated user changes and established names. Review the final diff, perform proportionate verification, fix introduced regressions, and report changed paths, checks actually run, and limitations. Do not run expensive training, notebook execution, dataset regeneration, downloads, or external services merely for package validation.

## Project-specific rules

- Preserve notebook stages and the distinction between analytical evaluation and production outcomes.
- Review preprocessing and feature engineering for leakage before changing splits, models, scores, or ALLOW/REVIEW/BLOCK tiers.
- Do not replace reported 61% capture or 80/15/5 tier allocations without reproducible evidence.
- Preserve filenames and relative paths; installation instructions must use the actual Fraud-Model-Project repository name.
- Avoid notebook output churn, full dataset dumps, and untrusted model deserialization.

## Verification

- Parse changed notebook JSON and, when available, validate with nbformat without executing cells. Inspect code cells for execution-order dependencies.
- Parse Feature_eng.py with ast without importing it.
- Run notebooks only when execution is requested and dependencies, inputs, split boundaries, and artifact destinations are understood.
- No automated test command was identified.

Do not install dependencies or regenerate artifacts for documentation-only edits. For code changes, choose the smallest relevant check and distinguish syntax validation from runtime or analytical validation. Preserve train/test boundaries where applicable. Stop broadening checks once the relevant risks are covered.

## Assessment limitations

- Notebook outputs and model artifact contents were not validated; no training or scoring was executed.

Do not infer a deployment from another repository. Major redesign, destructive data changes, repository visibility changes, and deployment-architecture changes require explicit user authorization unless already part of the current request.
