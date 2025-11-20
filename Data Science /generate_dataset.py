import numpy as np
import pandas as pd 

#want to generate salary data of some employees and export as csv 

np.random.seed(42)

years = np.random.uniform(0.5, 10, 100).round(2) #give me values from 0.5 to 10 and 100 rows of it 

salaries = (30000 + (years * 6000) + np.random.normal(0, 4000, size=100)).round(2)

df = pd.DataFrame({ 
    "YearsExperience": years,
    "Salary": salaries
})

df.to_csv("Experience_salary.csv")

