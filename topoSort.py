# ===============================================================================
# Title:  --- Interview Question - CE, Automation Specialist 
# Author: --- Anthony Castro
# Date:   --- December 2nd, 2020
# ===============================================================================
# Objective:
#     - Create a function to pass in a 'task', sort the 'task' respected 
#       objectives (values), and print the expected output
# ===============================================================================
# Notes:
#     - Could easily sort and print the key's values in the sortTask-function 
#       voluntarily implemented an alternative method for practicing purposes 
#
#     - This will pass a dictionary into a function, sorth the values of each 
#       key, and output the results to a txt file  
#
#     - Create and write to output file were not required by the original question 
# ================================================================================


#   Solution to Interview Question
def sortTask(task, myTask):
    myArr = []
    tempArr = []
    myArr = myTask.get(task)

    for x in myArr:
        tempArr.append(x)
        tempArr.sort()
    return tempArr

#   Dictionary named myTask, to be sorted 
myTask = {
    "A" : [],
    "B" : ["A", "B"],
    "C" : ["C", "A", "B"],
    "D" : ["A"],
    "E" : ["B", "D", "A"],
}

#   Prints original list to compare with our sorted list
print("\nOriginal Unsorted List")
for key, value in myTask.items():
    print (value)

#   Calls function sortTask to sort 
#   Sets sorted myTask values to outputList for write
outputList = []
print("\nModified Sorted List")
outputList.append(sortTask('A', myTask))
outputList.append(sortTask('B', myTask))
outputList.append(sortTask('C', myTask))
outputList.append(sortTask('D', myTask))
outputList.append(sortTask('E', myTask))

#   Opens Output file for write by iterating through outputList
with open("output.txt", "w") as outputFile: 
    for x in outputList:
        if outputList[0:]:
            outputFile.write("%s\n" % x)
        else:
            outputFile.write("%s" % x)
outputFile.close()

#   Reads Output file
readFile = open("output.txt", "r") 
expectedOutput = readFile.read()
expectedOutput = expectedOutput[:-1]
print(expectedOutput)
readFile.close()

