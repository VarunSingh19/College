# implementation Of stack using list.
def new_stack():
    var = list()
    return var

def is_empty(var):
    return len(var)==0

def push(var, var2):
    var.append(var2)
    print("Item added " + var2)

def pop(var):
    if (is_empty(var)):
        return "Stack Is Empty."
    else:
        return var.pop()
    
def show(var):
    print("The Element of Stack Are ")
    for i in var:
        print(i)

var = new_stack()
push(var,str(13))
push(var,str(1))
push(var,str(4))
push(var,str(54))
push(var,str(23))
push(var,str(13))

show(var)
print("Last Item removed is "+ pop(var))
show(var)