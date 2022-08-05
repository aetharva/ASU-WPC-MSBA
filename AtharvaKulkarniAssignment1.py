# Let's assume:
#  - Amy Hernandez is 10 years old.
#  - kids are 6 years old when they graduate 1st grade, 
#    and 18 years old when they graduate high school.

# Step 1:
# store the first name, last name and age of Amy in 3 variables.
# remember to use meaningful variable names
# You code here
AmyFN = "Amy"
AmyLN = "Hernandez"
AmyAge = 10

# Step 2:
# store the age at 1st grade and age at 12th grade in 2 variables.
# remember to use meaningful variable names
# You code here
GradAge1st = 6
GradAgeHS = 18    

# Step 3:
# Caculate current grade based on above variables and store in a variable
# remember to use meaningful variable names
# You code here
GradeAgeDiff = GradAge1st - 1
AmyGrade = AmyAge - GradeAgeDiff

# Step 4:
# Caculate number of years to graduation based on above variables 
#  and store in a variable
# remember to use meaningful variable names
# You code here
AmyY2G = GradAgeHS - AmyAge   

# Step 5:
# Print first name, last name, age, current grade, and # years to graduation
# remember to use meaningful messages when printing out the data
# You code here
print ("----- Amy's details -----")
print ("First Name: ", AmyFN)
print ("Last Name: ", AmyLN)
print ("Age: ", AmyAge)
print ("Current Grade: ", AmyGrade)
print ("Years to Graduate: ", AmyY2G)

# Step 6:
# Try running your program for ages 5, 7, 17, 18, 19
# Do you see expected results?
# Note: for ages >=18, we'll learn how to write "if-statements" in later
#       modules to control what gets stored/printed
# You code here

#Running for Amy's sibling Tony
TonyFN = "Tony"
TonyLN = "Hernandez"
TonyAge = 5   
#GradeAgeDiff = GradAge1st - 1
TonyGrade = TonyAge - GradeAgeDiff
TonyY2G = GradAgeHS - TonyAge
print ("----- Tony's details -----")
print ("First Name: ", TonyFN)
print ("Last Name: ", TonyLN)
print ("Age: ", TonyAge)
print ("Current Grade: ", TonyGrade)
print ("Years to Graduate: ", TonyY2G)

#Running for Amy's sibling Steve
SteveFN = "Steve"
SteveLN = "Hernandez"
SteveAge = 7   
SteveGrade = SteveAge - GradeAgeDiff
SteveY2G = GradAgeHS - SteveAge
print ("----- Steve's details -----")
print ("First Name: ", SteveFN)
print ("Last Name: ", SteveLN)
print ("Age: ", SteveAge)
print ("Current Grade: ", SteveGrade)
print ("Years to Graduate: ", SteveY2G)

#Running for Amy's sibling Bruce
BruceFN = "Bruce"
BruceLN = "Hernandez"
BruceAge = 17   
BruceGrade = BruceAge - GradeAgeDiff
BruceY2G = GradAgeHS - BruceAge
print ("----- Bruce's details -----")
print ("First Name: ", BruceFN)
print ("Last Name: ", BruceLN)
print ("Age: ", BruceAge)
print ("Current Grade: ", BruceGrade)
print ("Years to Graduate: ", BruceY2G)

#Running for Amy's sibling Natasha
NatashaFN = "Natasha"
NatashaLN = "Hernandez"
NatashaAge = 18   
NatashaGrade = NatashaAge - GradeAgeDiff
NatashaY2G = GradAgeHS - NatashaAge
print ("----- Natasha's details -----")
print ("First Name: ", NatashaFN)
print ("Last Name: ", NatashaLN)
print ("Age: ", NatashaAge)
print ("Current Grade: ", NatashaGrade)
print ("Years to Graduate: ", NatashaY2G)

#Running for Amy's sibling Thor
ThorFN = "Thor"
ThorLN = "Hernandez"
ThorAge = 19   
ThorGrade = ThorAge - GradeAgeDiff
ThorY2G = GradAgeHS - ThorAge
print ("----- Thor's details -----")
print ("First Name: ", ThorFN)
print ("Last Name: ", ThorLN)
print ("Age: ", ThorAge)
print ("Current Grade: ", ThorGrade)
print ("Years to Graduate: ", ThorY2G)