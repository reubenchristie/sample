#!/usr/bin/python
from Queue import Queue
from state import state

def contains(argList, argState):
    """
    check if argList contains argState 
    """
    for item in argList:
        if (item.m == argState.m and item.c == argState.c and item.b == argState.b):
            return True        
    return False

visited = []#visited states
path = []#complete path to the solution
q = Queue()
start = state() #in the beginning there were 3 missionaries and 3 cannibals on left bank of the river

#bredth first solution
q.put(start)
while(q.qsize()): #while queue is non empty go in loop
    next = q.get() #get the head state from the queue
    if (next.m == 0 and next.c == 0 and next.b == False):
        #done! we have found solution print the complete path by traversing q
        x = next        
        count =0
        while(x != None):
            #x.display()
            path.append(x)
            x = x.predecessor_state            
            count = count+1
        print "total river crossings:"+ str(count-1)+"\n"+"Miss(on L) Cann(on L) \t\tBoat At"
        #print path to the solution
        path.reverse()
        for item in path:
            item.display()                            
    else:
        #generate neighbors and enqueue Also, generate non visited neighbors        
        for i in xrange(3):
            j=0
            while(i+j<=2):
                if(i==0 and j==0):
                    j=j+1
                    continue
                #generate next state by moving i missionaries and j cannibals
                new_state =  next.move(i,j)
                #check if new_state can be considered as safe
                if(new_state.isSafe() == False):
                    j=j+1
                    continue
                #check if this state is already been explored before
                if(contains(visited,new_state)):
                    j=j+1
                    continue
                visited.append(new_state)
                q.put(new_state)                    
                j=j+1