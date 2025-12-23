# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 21:31:01 2022

First-year introductory Python project: GPA calculator (4.33 scale).

"""
# Assignment 1

"""
This program will help the user determine their GPA for the term, and then
tell them if they have reached their desired GPA, which will be asked from
them in the program. The highest and lowest point grades will be displayed.
If the user has not reached their desired GPA, it will calculate a different
mark for their lowest point grade and tell them if they had the calculated
mark, they would have reached their GPA. It won't be accurate if they had an
exteremely low mark and wanted a high GPA, but it gives them an idea of how 
they need to improve their marks. 
"""

def markAndWeightInput(userCourses):    #gets user input based on how much courses they want to calculate
    markList = []    #list to store their letter grades
    weightList = []    #corresponding list to store each grade's weight
    counts = int(userCourses)    #converts string to integer
    for x in range(0, counts):    #loops as much as the number of user's courses
        b = input("Enter your letter grade: ")
        c = float(input("Enter the weight for that course: "))
        b = b.upper()    #compares the string and converts to upper case if the user entered a lower case for the letter grade to make it easy in further steps
        markList.append(b)    #adds user grade input to list
        weightList.append(c)    #adds user weight input to list
    return markList, weightList 
    
def markConvert(letter):    #converts the user's letter grades to number grades
    letters = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']    #list of all the possible letter grades in order
    pointGrade = [4.33, 4.0, 3.67, 3.33, 3.0, 2.67, 2.33,  2.0, 1.67, 1.33, 1.0, 0.67, 0]    #list of all the corrsponding point grades in order     

    for x in range(len(letters)):    #loops for the length of user's courses
        if letter == letters[x]:    #if statement to see which letter from the list is the same as the user's letter grade
            return pointGrade[x]    #gets the point grade corresponding to the letter grade index
        
    print("Invalid letter grade entered, counted as F.")
    return 0.0
        
def highestAndLowestMark(numberGrades):   #gets the highest point grade and lowest point grade
    highestMark = 0    #set variable to 0
    lowestMark = numberGrades[0]    #set varaible to the first in the point grade list
    for x in range(len(numberGrades)):    #loops for the amount of user courses
        if numberGrades[x]>highestMark:    #if the current loops value is greater than the declared highest mark
            highestMark = numberGrades[x]    #changes highest mark to current loop value when if statement is true
    
    for x in range(len(numberGrades)): 
        if numberGrades[x]<lowestMark:    #if the current loops value is less than the declared lowest mark
            lowestMark = numberGrades[x]   #changes lowest mark to current loop value when if statement is true
    
    print("Is the determined highest mark higher than the determined lowest mark?")    #boolean data type checks to see that highest mark is larger than the lowest mark, to see if it declared correctly
    print(highestMark >= lowestMark)
    
    return highestMark, lowestMark
        
def totalGPA(numberGrades, weight):    #calculate the user GPA with parameters of the point grades and the weight list
    markSum = 0    #initializes mark sum to 0
    weightSum = 0    #initializes weight sum to 0
    gpa = 0    #initializes GPA to 0
    for x in range(len(numberGrades)):    #loops for the amount of user grades
        markSum += numberGrades[x]    #adds the current loop grade to the total mark sum
        weightSum += weight[x]    #adds the current loop weight to the total weight sum
    
    gpa = markSum/weightSum    #calculates for GPA by dividing the total marks by total weight
    return gpa
             
def compareGPA(earnedGPA, wantedGPA, numberList, weights, lowestMark): #to compare the desired GPA and the user's actual GPA by passing parameters for their earned GPA, desired GPA, thier point grade list, their course weight list and their lowest mark
    weightPlace = 0    #initialized to 0 and is the weight value for their lowest mark, used later if their desired GPA is not reached and to figure out what their lowest mark should be to reach the goal
    markSum = 0    #initialized to 0 for marks sum
    weightSum = 0    #initialized to 0 for weights sum
    neededGrade = 0     #initalized to 0, used only if desired goal is not met, and is used to replace the lowest grade
    gpaFirst = str(earnedGPA) + '0' + '0' + '0'    #convert to string and adds three decimal places in case it only had one, helps compare and not be out of range
    gpaBeg = gpaFirst[0]    #gets the first digit of their current GPA
    gpaAfter = gpaFirst[2]    #gets the first decimal, tenths, of their current GPA
    gpaSecond = gpaFirst[3]    #gets the hundreths decimal of their current GPA
    gpaThird = gpaFirst[4]    #gets the thousandths value decimal from their current GPA
    gpaBeg = int(gpaBeg)     #converts to integer to compare
    gpaAfter = int(gpaAfter)    
    gpaSecond = int(gpaSecond)     
    gpaThird = int(gpaThird)     
    wantedGPA = float(wantedGPA)
    wanted_str = f"{wantedGPA:.3f}" 
    wantedBeg = int(wanted_str[0]) #gets the first digit of their desired GPA
    wantedAfter = int(wanted_str[2]) #gets the first decimal, tenths, of their desired GPA
    wantedSecond = int(wanted_str[3]) #gets the hundreths of their desired GPA
    wantedThird = int(wanted_str[4])  #gets the thousandths value decimal of their desired GPA

    for x in range(len(numberList)):    #loops for number of user courses
        markSum += numberList[x]    #adds current grade to mark sum
        weightSum += weights[x]    #adds current weight to weight sum
    for x in range (len(numberList)):   #loops for number of user courses  
        if lowestMark == numberList[x]:    #if the determined lowest mark is the same as the current index's value in the loop
            weightPlace = weights[x]    #gets the weight of the lowest mark
    
    if gpaBeg<wantedBeg:    #if the first digit of user's GPA is lower than their desired GPA, tells them they did not reach their desired goal
        print("\nYou did not reach you desired GPA.")   
      
      
        markSum = markSum - lowestMark    #removes lowest mark value from total marks
        neededGrade = (wantedGPA*weightSum) - markSum    #gets desired GPA total marks and subtracts with their current GPA without the lowest mark
        neededGrade = neededGrade/weightPlace    #gets the needed grade by dividing by the lowest grade's weight
        neededGrade = str(neededGrade)   
        print("If you replaced your lowest mark with " + neededGrade + ", you would get your desired GPA.")   #tells user what their lowest mark could be to get their goal
   
        
    elif gpaBeg==wantedBeg and gpaAfter>=wantedAfter and gpaSecond >= wantedSecond and gpaThird >= wantedThird:     #if all the digits of the current GPA are the same as or greater than the goal's GPA, tells them they succeeded in getting their goal 
        print("\nYou succeeded in getting your desired GPA.")
    
    elif gpaBeg==wantedBeg and gpaAfter>=wantedAfter and gpaSecond >= wantedSecond and gpaThird < wantedThird:      #if all the digits of the current GPA are the same as or greater than the goal's GPA except for the thousandths place digit, tells user they did not reach their goal 
        print("\nYou did not reach your desired GPA.")
        markSum = markSum - lowestMark
        neededGrade = (wantedGPA*weightSum) - markSum
        neededGrade = neededGrade/weightPlace    #calculates for what their lowest mark could be
        neededGrade = str(neededGrade)
        print("If you replaced your lowest mark with " + neededGrade + ", you would get your desired GPA.")
                    
    elif gpaBeg==wantedBeg and gpaAfter>=wantedAfter and gpaSecond < wantedSecond:    #if the first digit and the tenths decimal of the current GPA are the same as or greater than the goal's GPA values except for the hundreths place digit, tells user they did not reach their goal 
        print("\nYou did not reach your desired GPA.")    #only goes to hundreths place since it would not matter after for the thousandths
        markSum = markSum - lowestMark
        neededGrade = (wantedGPA*weightSum) - markSum
        neededGrade = neededGrade/weightPlace
        neededGrade = str(neededGrade)
        print("If you replaced your lowest mark with " + neededGrade + ", you would get your desired GPA.")
                
    elif gpaBeg==wantedBeg and gpaAfter<wantedAfter:    #if the first digit of the current GPA is the same as or greater than the goal GPA's first digit but the tenths digit is lower, tells user they did not reach their goal 
        print("\nYou did not reach your desired GPA.")
        markSum = markSum - lowestMark
        neededGrade = (wantedGPA*weightSum) - markSum
        neededGrade = neededGrade/weightPlace
        neededGrade = str(neededGrade)
        print("If you replaced your lowest mark with " + neededGrade + ", you would get your desired GPA.")
   
    else:    #if above conditions were not met, that leaves user with succeeding in desired GPA
        print("\nYou succeeded in getting your desired GPA.")


if __name__ == "__main__":   #gets input from user 
    userInput = input("How many courses do you have?: ")
    marks, weights = markAndWeightInput(userInput)   #gets values for their marks and weight from function
    
    numberGrade = []   #initalizes list to get point grades
    for x in range(len(marks)):    #loops for the amount of marks user entered
        numberGrade.append(markConvert(marks[x]))    #adds point grade to the list by calling the markConvert function
    
    print("")
    highest, lowest = highestAndLowestMark(numberGrade)    #gets hgihest and lowest grades from the function
    print(f"Highest point grade: {highest}")
    print(f"Lowest point grade: {lowest}")
    
    print(f"\nYour point grades in order: {numberGrade}")
        
    userGPA = totalGPA(numberGrade, weights)
    print(f"\nYour calculated GPA: {userGPA}")
    
    gpaGoal = input("\nWhat GPA are you trying to reach for your goal? Please enter with at least three decimal places (use zero if no decimal places): ")     #asks user for what their goal GPA is 
    
    compareGPA(userGPA, gpaGoal, numberGrade, weights, lowest)