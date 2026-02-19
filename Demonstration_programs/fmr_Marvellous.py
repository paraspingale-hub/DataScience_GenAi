
def FilterX(Task , Elements):
    result = list()                 
    for no in Elements:
        ret = Task(no)
        if(ret == True):
            result.append(no)
    return result

def MapX(task , elements):
    result = list()
    for no in elements:
        result.append(task(no))                     
    return result

def ReduceX(task , elements):
    sum = 0 
    #[11, 21, 23, 31]
    for no in elements:
        sum = task(sum ,no)
    return sum 
