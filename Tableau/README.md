# 📘 Employee Engagement & Experience Dashboard

This project visualizes employee sentiment and development using real-world-inspired HR data. Built in Tableau Public and supported by Python preprocessing, it offers a clean, interactive overview of satisfaction, engagement, and training trends across divisions. This work demonstrates the use of visualization to drive workforce insight and improve the employee experience.

---

## 🔍 Objective

To explore patterns in employee engagement, satisfaction, and training participation — identifying key areas of strength and concern across divisions, and presenting them in a format that supports action by HR leaders and people managers.

---

## 🛠️ Data Extraction & Preparation

- **Data Source**: Publicly available HR datasets from Kaggle (simulated engagement, training, and employee records).
- **Tools Used**:
  - **Python (pandas)**: Used to clean, join, and merge datasets on `Employee_ID` across engagement, employee info, recruitment, and training records.
  - **Excel/PowerQuery**: Used for initial validation and exploratory formatting.
  - **Tableau Public**: Used to create a polished, high-contrast dashboard with KPI tiles, heatmaps, and scatter plots.

The merged dataset included employee IDs, department and division names, engagement scores, satisfaction metrics, and training hours. Pivoting and aggregation enabled custom visualizations in Tableau.

---

## 📊 Key Analyses

- **KPI Tiles**:
  - Average Engagement Score (Org-wide)
  - % of Employees Trained (2022–2023)
  - Top Division by Satisfaction Score

- **Division-Level Visualizations**:
  - Heatmap showing sentiment (Engagement, Satisfaction, Work-Life Balance) by division
  - Scatter plot: Training Hours vs Engagement Index

- **Calculated Fields & LOD Expressions**:
  - Custom FIXED calculations to extract division-specific scores
  - Dynamic top-performing department card
  - Percent trained metric filtered by training year

---

## 📈 Sample Insights

- The average engagement score across the organization was **2.98** (on a 4-point scale)
- **IT Division** had the highest satisfaction score at **3.42**
- All employees included in the dataset received training in either 2022 or 2023

---

## 💡 Recommendations

- Investigate the engagement strategies used by high-performing divisions like IT
- Ensure that training programs continue to support key performance areas such as work-life balance and overall satisfaction
- Consider department-specific interventions where scores lag

---

## 📖 Summary

This dashboard illustrates how employee engagement, satisfaction, and training can be combined into a cohesive, accessible people analytics tool. Using Python for data joining and Tableau for visualization, I translated raw public HR data into actionable insights. The result is a clean, high-contrast dashboard suitable for HR leaders, organizational developers, and people analytics professionals seeking to build evidence-based strategy.

---

## 🔗 View the Dashboard

**[View on Tableau Public](https://public.tableau.com/app/profile/c.krumrie/viz/PeopleExperienceInsights/Dashboard1)**  

---

## 🧑‍💻 Author

**Charity Krumrie**  
[LinkedIn](https://www.linkedin.com/in/ckrumrie/)  
[Email](mailto:cwkrumrie@gmail.com)
