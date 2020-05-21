#Assignment 1 - Student Grade Program
#Programmer by: Aaron Tan

#Define functions:

def calculateGrade(result):
    if result < 50:
        nameGrade = "Fail"
    elif result < 60:
        nameGrade = "Pass"
    elif result < 70:
        nameGrade = "Credit"
    elif result < 80:
        nameGrade = "Distinction"
    else:
        nameGrade = "High Distinction"
    return nameGrade

def inputInt(prompt):
    while True:
        value = input(prompt)
        try:
            numResponse = int(value)
            if numResponse >8:
                print("Invalid input. Cannot be more then 8 assessments.")
                continue
            elif numResponse < 1:
                print("Invalid input. Cannot be less then 1 assessment.")
        except ValueError:
            print("Invalid Input. Type an integer number.")
            continue
        return numResponse        

def inputMarks(prompt, minValue, maxValue):
    while True:
        value = input(prompt)
        try:
            numResponse = int(value)
            if numResponse > maxValue:
                print("Invalid input. Cannot be more then 100 marks.")
                continue
            elif numResponse < minValue:
                print("Invalid input. Cannot be less then 1 mark.")
                continue
        except ValueError:
            print("Invalid input. Type an integer number.")
            continue
        return numResponse

def inputStr(prompt):
    while True:
        name = input(prompt)
        if len(name) < 3:
            print("Inavlid name. Enter at least more then 3 characters.")
            continue
        elif name.isspace() == True:
            print("Invalid name")
            continue
        else:
            return(name)

def studentMarkInput(prompt, assessmentMarkList, assessmentList, listCounter):
    while True:
        studentInput = input(prompt)
        try:
            studentMark = int(studentInput)
            #If the user inputed more then the assessmentMark in a list then
            if studentMark > assessmentMarkList[listCounter]:
                print("You have inputed: " + str(studentMark) + ". The assessment named: "\
                    + assessmentList[listCounter] + ", has a full mark of: " \
                    + str(assessmentMarkList[listCounter]))
                continue

            #If the user inputed less then 0 then.
            elif studentMark < 0:
                print("You cannot input " + currentName + "'s mark to be " \
                    + str(studentMark))
                continue
            else:
                return(studentMark)
        except ValueError:
            print("Invalid input. Type an integer number.")
            continue
    
#End of define functions

#Initalise Lists
assessmentList = [] #Lists all of the assessment names.
assessmentMarkList = [] #List all of the assessment marks.

#Initalise counters
counter = 0
studentCounter = 0
listCounter = 0
finalCounter = 0
topCounter = 0

#Initalise marks
totalMarks = 0 
classMark = 0

#Initalise min and max values
minValue = 1
maxValue = 100

#Begin
numAssessments = inputInt("Enter the number of assessments: ")
for x in range(numAssessments): 
    
    counter = counter + 1
    assessmentName = input("Enter name of assessment " + str(counter) + ": ")
    currentMark = inputMarks("How many marks is the " + assessmentName.strip(" ") + " worth?: ", minValue, maxValue) 
   
    #Adds the new item (add the variable as an item) to the list
    assessmentList.append(assessmentName)
    assessmentMarkList.append(currentMark)
    
    totalMarks = totalMarks + currentMark

if int(totalMarks) != 100: 
    print("You have not add all the assessmentMarks to 100. End Program.")
else:
    numStudents = inputInt("\nHow many students?: ")
    
    for x in range(numStudents):
        #Adds the studentCounter by 1 to count each student.
        studentCounter = studentCounter + 1
        currentName = inputStr("\nWhat is the name of student " + str(studentCounter) + ": ")

        listCounter = 0

        #Resets the totalStudentMarks to be 0 for each student to loop through.
        totalStudentMarks = 0        

        for x in range(numAssessments):
            studentMark = studentMarkInput("What did " + currentName.strip(" ") + " get out of " \
                                        + str(assessmentMarkList[listCounter]) + \
                                      " in the " + str(assessmentList[listCounter]) + ": ",
                                      assessmentMarkList, assessmentList, listCounter)

            #Calculates the result for each assessment
            result = studentMark/int(assessmentMarkList[listCounter]) * 100
            result = calculateGrade(result)

            print(str(studentMark) + " out of " \
                  + str(assessmentMarkList[listCounter]) + " is a " + result)
            listCounter = listCounter + 1

            #Adds all the student's marks for each assessment into totalStudentMarks
            totalStudentMarks = totalStudentMarks + studentMark

        finalStudentResults = (totalStudentMarks/totalMarks) * 100
        finalStudentResults = int(finalStudentResults)
        finalGrade = calculateGrade(finalStudentResults)

        #Outputs the final Student's name, all the student's marks and display
        #the student's finalGrade by using the variable (finalGrade) shown above.
        print(currentName.strip(" ") + " has a total mark of " + str(finalStudentResults) \
              + " (" + finalGrade + ")") 

        #Adds the student's finalStudentResults marks to classMarks.
        classMark = classMark + finalStudentResults
        finalCounter = finalCounter + 1

        #Setting the topStudent and topMark code
        if topCounter == 0:
            topStudent = currentName
            topMark = finalStudentResults

        #If the topCounter is more then 1 (more then 1 student)
        elif topCounter >= 1:
            #Update the topStudent and the topMark.
            if finalStudentResults > topMark:
                topStudent = currentName
                topMark = finalStudentResults
                
        topCounter = topCounter + 1

    #After all the number of assessments and number of students has been looped
    #Outputs a message.
    print("\nAll marks have been entered.")

    classAverage = int(classMark)/finalCounter
    classAverage = int(classAverage)
    classGrade = calculateGrade(classAverage)

    print("The class average is " + str(classAverage) + " (" + classGrade + ")")
    print("The top student is " + topStudent.strip(" ") + " with a total mark of " + str(topMark))

