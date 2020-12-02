

myTask = {
    "A" : [],
    "B" : ["A", "B"],
    "C" : ["C", "A", "B"],
    "D" : ["A"],
    "E" : ["B", "D", "A"],
}

def sortTask(task, myTask):
    myArr = []
    tempArr = []
    myArr = myTask.get(task)

    for x in myArr:
        tempArr.extend(x)
        tempArr.sort()

    print(tempArr)
        

sortTask('A', myTask)
sortTask('B', myTask)
sortTask('C', myTask)
sortTask("D", myTask)
sortTask("E", myTask)
        
