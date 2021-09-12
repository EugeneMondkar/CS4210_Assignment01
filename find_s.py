#-------------------------------------------------------------------------
# AUTHOR: Eugene Mondkar
# FILENAME: find_s.py
# SPECIFICATION: writing the Find-S algorithm
# FOR: CS 4200- Assignment #1
# TIME SPENT: 10 minutes
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv
import copy as cp

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
with open('.\data\contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\nThe initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here

starting_row = 0
for row in db:
  if row[4]== 'Yes':
    hypothesis = cp.deepcopy(row)[:4]
    break
  starting_row += 1

#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here

for i in range(starting_row + 1, len(db)):
  if db[i][4]== 'Yes':
    for j in range(4):
      if hypothesis[j] != db[i][j]:
        hypothesis[j] = '?'

print("\nThe Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:")
print(hypothesis)