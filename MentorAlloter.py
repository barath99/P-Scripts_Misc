import csv
import random
import math as mt
from itertools import islice

# Reading the csv file containing the list of Mentee----------
f = open('D:\menteeXL.csv',encoding='utf-8-sig')
readFile = csv.reader(f)
for col in readFile:
    MenteeData =list(readFile)
# print (MenteeData)
#-------------------------------------------------------------

# Reading the csv file containing the list of Mentors---------
g = open('D:\mentorXL.csv',encoding='utf-8-sig')
readFileM = csv.reader(g)
for col in readFileM:
    MentorData =list(readFileM)
# print (MentorData)
#-------------------------------------------------------------

# logic for maximizing equality in allocating mentees -> 
# N is number of Mentee overall
# M is number of Mentors
# Then ceil(N/M) students for first (N mod M) mentors
# Remaining Mentors get floor(N/M) mentees

No_of_Groups = len(MenteeData) / len(MentorData)
N = len(MenteeData)
M = len(MentorData)


# using Fisher–Yates shuffle Algorithm incase if we need to shuffle the students
#--------------------------------------------------------------------------------
# Shuffle Algorithm for Mentees
Shuffle = MenteeData

for i in range(len(MenteeData)-1, 0, -1): 
      
    # Pick a random index from 0 to i  
    j = random.randint(0, i + 1)  
    
    # Swap arr[i] with the element at random index  
    Shuffle[i], Shuffle[j] = Shuffle[j], Shuffle[i]  

print ("The shuffled Mentee list is : " +  str(Shuffle)) 

#---------------------------------------------------------------------------------------------------
# Shuffle Algorithm for Mentors (Necessary)
Shuffle1 = MentorData

for i in range(len(MentorData)-1, 0, -1): 
      
    # Pick a random index from 0 to i  
    j = random.randint(0, i + 1)  
    
    # Swap arr[i] with the element at random index  
    Shuffle1[i], Shuffle1[j] = Shuffle1[j], Shuffle1[i]  

print ("The shuffled Mentee list is : " +  str(Shuffle1))

# The New Shuffled list of Mentee and Mentors---------------

MenteeData = Shuffle
MentorData = Shuffle1

# Allocation Process ---------------------------------------

x = mt.ceil(N/M)
y = mt.floor(N/M)
w = N % M
z = M - w

group_split = []

for k in range(1,w+1,1):
    group_split.append(x)

for a in range(1,z+1,1):
    group_split.append(y)

#print(group_split)

#-----------Chunking MenteeData into Sublists of required size

# Using islice 
Inputt = iter(MenteeData) 
MentoringGroups = [list(islice(Inputt, elem)) 
          for elem in group_split] 

#print("Groups of Mentees for Corresponding Mentors -> ", MentoringGroups)

# print(len(MentoringGroups))

def add_column_in_csv(input_file, output_file, transform_row):
    """ Append a column in existing csv using csv.reader / csv.writer classes"""
    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = csv.reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = csv.writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)

with open("D:\out.csv", "w", newline="") as q:
    writer = csv.writer(q)
    writer.writerows(MentorData)

add_column_in_csv('D:\out.csv', 'D:\FinalAllotmentList.csv', lambda row, line_num: row.append(MentoringGroups[line_num - 1]))
#-------------------------------------

f.close()
g.close()

# --------------- Relax Now!!!! ---------------------