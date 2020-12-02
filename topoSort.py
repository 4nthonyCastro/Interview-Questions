# [Interview Question - December 2nd, 2020]
#
# Objective: 
#     Each 'task', has a list of objectives to complete.
#     Create a function to pass in a 'task', sort the 'task' respected objectives (values), and print the output.
#
# Note: 
#     Included an output file of the expected output for this question. 
#     Create and write to output file is not required to answer this question. 

def sortTask(task, myTask):
    myArr = []
    tempArr = []
    myArr = myTask.get(task)

    for x in myArr:
        tempArr.extend(x)
        tempArr.sort()
    print (tempArr)
    return tempArr

myTask = {
    "A" : [],
    "B" : ["A", "B"],
    "C" : ["C", "A", "B"],
    "D" : ["A"],
    "E" : ["B", "D", "A"],
}


outputList = sortTask('A', myTask)
outputList.append(sortTask('B', myTask))
outputList.append(sortTask('C', myTask))
outputList.append(sortTask('D', myTask))
outputList.append(sortTask('E', myTask))


with open("output.txt", "w") as outputFile: 
    for x in outputList:
        outputFile.write("%s\n" % x)

# outputFile = open("output.txt", "r")
# print(outputFile.read())
outputFile.close()
