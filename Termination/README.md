# Employee Termination Analysis (FY23–24)

This project explores patterns in employee attrition using termination data from fiscal year 2023–2024. It was developed as part of a people analytics portfolio to showcase skills in Python, data visualization, and workforce strategy.

## Objective

To identify trends in employee turnover — including tenure, voluntary vs. involuntary exits, and departmental differences — and provide actionable insights to support retention strategy and organizational development.

## Data Extraction & Preparation

- **Data Source**: Raw employee records were exported from the organization’s Oracle Human Capital Management (HCM) system using built-in reporting tools.
- **Tools Used**:
  - **Oracle Reporting**: Used to pull termination data and demographic details.
  - **Excel with Power Query**: Employed to clean, normalize, and derive fields such as `Tenure_Years`, format dates, and remove duplicates.
  - **Python (pandas, seaborn, matplotlib)**: Used for analysis, visualization, and statistical summarization in a Jupyter Notebook environment.

The final dataset included 350+ employee termination records with key variables such as department, job title, termination type, reason, and calculated tenure.

## Key Analyses

- Distribution of tenure at time of exit (histogram + KDE curve)
- Termination type breakdown (voluntary vs. involuntary)
- Department-level turnover comparisons
- Average tenure by exit type
- Tenure-based bucket segmentation (<1 yr, 1–3 yrs, etc.)

## Sample Insights

- 33% of all voluntary exits occurred within the first year of employment, particularly in high-volume, front-line departments like Fire Rescue and Roads & Drainage.
- Involuntary terminations were more frequent in technical service roles and often followed tenure exceeding 3 years.
- Average tenure at exit across all terminations was 4.80 years.

## Recommendations

- Strengthen onboarding and early engagement programs in departments with high early exits.
- Evaluate managerial effectiveness in teams with elevated involuntary turnover.
- Incorporate exit data into continuous improvement efforts for employee experience.

## Summary

During this analysis, I used Python and real-world HR data to investigate employee terminations across a large public organization during FY23–24. By visualizing tenure distributions, comparing voluntary and involuntary exit patterns, and segmenting departures by department, I uncovered critical trends — including a high rate of early-stage turnover in frontline roles and long-tenure exits from technical departments. These findings support data-driven decisions around onboarding, training, and manager development, and demonstrate how people analytics can drive actionable strategy across the employee lifecycle.

## Author

Charity Krumrie  
[LinkedIn](https://www.linkedin.com/in/ckrumrie/)  
[Email](mailto:cwkrumrie@gmail.com)  
