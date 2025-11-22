import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

attendance = np.random.randint(40, 100, n)
study_hours = np.random.randint(1, 30, n)
assignments = np.random.randint(2, 10, n)
internals = np.random.randint(20, 50, n)
extra = np.random.randint(0, 2, n)

performance = []

for a, s, ass, inte in zip(attendance, study_hours, assignments, internals):
    score = (0.3*a) + (1.5*s) + (3*ass) + (2*inte)

    if score > 190:
        performance.append("High")
    elif score > 120:
        performance.append("Medium")
    else:
        performance.append("Low")

df = pd.DataFrame({
    "attendance": attendance,
    "study_hours": study_hours,
    "assignments_completed": assignments,
    "internal_marks": internals,
    "extracurricular": extra,
    "performance": performance
})

df.to_csv("data/dataset.csv", index=False)

print("dataset.csv generated successfully!")