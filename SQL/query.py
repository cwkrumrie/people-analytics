import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = sqlite3.connect("SQL\open_university.db")

# Test query: Average assessment score by gender
query = """
SELECT s.gender, ROUND(AVG(sa.score), 2) AS avg_score
FROM studentInfo s
JOIN studentAssessment sa
  ON s.id_student = sa.id_student
GROUP BY s.gender;
"""

# Run and store results in DataFrame
df = pd.read_sql_query(query, conn)

# Results display
print("Average Assessment Score by Gender:\n")
print(df)

# Export to CSV
df.to_csv("SQL/output_gender_scores.csv", index=False)
print("\n Results exported to SQL/output_gender_scores.csv")

# Plot Results
plt.figure(figsize=(6, 4))
sns.barplot(data=df, x="gender", y="avg_score", palette="Set2")
plt.title("Average Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")

# Export ot PNG
plt.tight_layout()
plt.savefig("SQL/avg_score_by_gender.png", dpi=300)

conn.close()