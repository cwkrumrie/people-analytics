# 📊 Demographics & Pay Equity Analysis

This project investigates workforce demographics, tenure, and compensation patterns using real-world HR data. The analysis focuses on identifying potential gender-based disparities in pay and representation across departments and salary bands.

By combining visual analysis with linear regression modeling, this project highlights areas of organizational inequity and offers data-driven recommendations for more inclusive workforce planning.

---

## 🎯 Objective

- Explore the relationship between **gender, salary, and tenure**
- Visualize **gender representation** across departments and salary bands
- Use **regression modeling** to test whether gender and tenure predict salary
- Identify potential **equity gaps** to support further HR analysis and action

---

## 🛠️ Tools Used

- **Python** (pandas, matplotlib, seaborn, scikit-learn)
- **Jupyter Notebook** (VS Code)
- **Excel** + PowerQuery (for data cleaning and salary band definition)

---

## 📁 Dataset Summary

| Field            | Description                          |
|------------------|--------------------------------------|
| `Gender`         | Categorical gender (F/M)             |
| `Salary`         | Current salary (annualized)          |
| `Tenure_Years`   | Time employed with the organization  |
| `Department`     | Organizational unit                  |
| `Job_Title`      | Current job classification           |

Data was pulled using Oracle HCM reporting and cleaned in Excel before analysis.

---

## 📊 Key Analyses

### 👥 Gender Representation by Department
- Departments like **Fire Rescue** and **Roads & Drainage** show male dominance
- **Health & Human Services** and **Court Services** lean female

### 💰 Gender Distribution Across Salary Bands
- Male employees are overrepresented in the **$100K+** salary band
- Mixed representation exists in mid-range salaries ($40K–$70K)

### 📈 Linear Regression: Salary Prediction
- Used `Tenure_Years` and encoded `Gender` as predictors
- Found that **being male is associated with a ~$6,736 salary increase**, holding tenure constant
- Model explains ~26% of salary variance (R² = 0.26)

---

## 📋 Regression Summary

| Component           | Value        |
|---------------------|--------------|
| Intercept           | \$44,315     |
| Tenure Coefficient  | \$1,375/year |
| Gender Coefficient  | \$6,736 (M)  |
| R² Score            | 0.26         |
| Mean Squared Error  | \$364M       |

---

## ✅ Key Insights

- A measurable **gender-based pay gap** exists, even after controlling for tenure.
- **Departmental imbalances** suggest limited representation in certain job families.
- **Regression results** support the need for deeper compensation and promotional audits.

---

## 💡 Recommendations

- Conduct a full **pay equity audit** controlling for role, performance, and department.
- Expand internal analysis to include **promotion velocity**, **hiring trends**, and **managerial roles**.
- Strengthen efforts to diversify representation in **high-compensation job families**.

---

## 📎 Files

- `Demographics_Analysis.ipynb`: Full notebook with code, charts, and model
- `gender_salary_distribution.png`: Chart showing gender by salary band
- `gender_by_department.png`: Chart showing gender by department

---

## 👤 Author

Charity Krumrie  
[LinkedIn](https://www.linkedin.com/in/ckrumrie)  
[Email](mailto:cwkrumrie@gmail.com)