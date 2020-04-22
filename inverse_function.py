#OM NAMO NARAYANA
import pandas as pd
import numpy as np
df = pd.read_csv('FinalAllotmentList.csv')


n_mentors = df.shape[0]
lst = []
for i in range(n_mentors):
    mentors = df.iloc[i]
    mentees = list(mentors[1].split(','))
    for mentee in mentees:
        mentor = mentors[0]
        lst.append((mentee, mentor))

for mentee, mentor in lst:
    print("mentee: {} mentor: {}".format(mentee, mentor))

df = pd.DataFrame(lst)
print(df)
csv = df.to_csv('AllocationCompleted.csv', index=False)