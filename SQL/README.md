# Open University Student Performance Analysis

This project analyzes academic performance and engagement data from The Open University Learning Analytics Dataset (OULAD). Using SQLite, Python, and Jupyter Notebook, it explores how demographic factors relate to assessment scores and uses both regression and classification models to predict student outcomes.

---

## Project Goals

- Combine multiple CSV datasets into a single SQL database
- Analyze average assessment scores across demographic groups
- Build interactive visualizations for age and gender-based comparisons
- Explore predictive models (regression and classification) for student success

---

## Data Overview

**Source:** [OULAD Dataset (Kaggle)](https://www.kaggle.com/datasets/openuniversity/oulad)

**Files Used:**

- `studentInfo.csv`: Demographic and outcome data
- `studentAssessment.csv`: Scores on assignments and exams
- `studentRegistration.csv`, `studentVle.csv`, `vle.csv`, `assessments.csv`, `courses.csv`: Additional student and course details

**Joined on:** `id_student`

---

## Tools & Technologies

- **Python 3.13**
- **SQLite**: Lightweight database for joining data
- **pandas & seaborn**: Data manipulation and visualization
- **matplotlib**: For plotting
- **scikit-learn**: Regression and classification modeling
- **ipywidgets**: Interactive selection in Jupyter Notebook

---

## File Structure

├── SQL/

│   ├── *.csv                 

│   ├── output_gender_scores.csv  

│   └── open_university.db    

├── load_data.py              

├── query.py                 

├── interactive_plot.ipynb    

└── README.md                 

---

## Key Analyses & Visualizations

- **Bar plots** comparing average scores by gender and age band
- **Interactive widgets** for dynamic chart generation
- **Linear regression** to model numeric average score using demographics
- **Logistic classification** to predict pass/fail outcomes
- **Scatter plots** showing regression trends and effect of weighting

---

## Sample Insights

- Male and female students have comparable average scores, but younger students tend to perform better overall.
- Linear regression shows low R², indicating limited predictive power using demographic data alone.
- Logistic models using gender, age, disability, and region provide modest accuracy in predicting pass/fail status.

---

## How to Use

1. Place all raw CSVs into a `SQL/` directory
2. Run `load_data.py` to create the SQLite database
3. Open and run `interactive_plot.ipynb` in Jupyter
4. Use widgets to explore data or modify the notebook to test your own queries

---

## 👤 Author

**Charity Krumrie**  
📍 Lakeland, FL  
📧 [cwkrumrie@gmail.com](mailto:cwkrumrie@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/ckrumrie)

---

> This project demonstrates applied SQL and Python analytics on a real-world education dataset, with an emphasis on demographic equity and predictive modeling.
