from itertools import count

gennum = dict()

def gensym(x):
    if x not in gennum:
       gennum[x] = count() 
    return x+str(gennum[x].__next__())


def some_condition(conds,obj):
    if len(conds) == 0: return False
    elif conds[0](obj) == True: return True
    else: return some_condition(conds[1:],obj)

def forall(list,cond):
    if list == []: return True
    elif cond(list[0]) == True: return forall(list[1:],cond)
    else: return False

def forsome(list,cond):
    if list == []: return False
    elif cond(list[0]) == True: 
        return True
    else:
        return forsome(list[1:],cond)
    
def show(obj):
    if isinstance(obj,str):
        return obj
    elif isinstance(obj,list):
        return '['+ ', '.join([show(x) for x in obj])+']'
    elif isinstance(obj,tuple):
        return '('+ ', '.join([show(x) for x in obj])+')'
    elif isinstance(obj,dict):
        return '{'+', '.join([show(i[0])+' = '+show(i[1]) for i in obj.items()])+'}'
    elif 'show' in dir(obj):
        return obj.show()
    else:
        return str(obj)
        

def showall(objs):
    return [show(obj) for obj in objs]

def substitute(obj,v,a):
    if obj == v:
        return a
    elif isinstance(obj,list):
        return [substitute(x,v,a) for x in obj]
    elif 'subst' in dir(obj):
        return obj.subst(v,a)
    else: 
        return obj

def example(num):
    print('\n\nExample '+str(num)+':\n')
 
