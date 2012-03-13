class state(object):
    '''
    this class represents number of cannibals, missionaries on left bank and boat position (either left or right of the river)
    '''
    m = 3#missionaries
    c = 3#cannibals
    b = True#True if boat on left  bank, False otherwise
    predecessor_state = None#where we came from,None if this is start state
    
    def __init__(self):
        pass
    
    def isSafe(self):
        """
        check if the current positions for missionaries and cannibals is safe
        if missionaries are out numbered by cannibals on either side, it is non safe (for missionaries of course) 
        """
        if(self.m < 0 or self.m > 3 or self.c<0 or self.c > 3):
            return False
        elif(3-self.m < 0 or 3-self.m > 3 or 3-self.c <0 or 3-self.c > 3):
            return False
        elif(self.m > 0 and self.c > self.m):
            return False
        elif(3-self.m >0 and 3-self.c > 3-self.m):
            return False
        return True;    
    
    def move(self,M,C):
        """
        apply the transfer of M missionaries and C cannibals
        returns new state object
        """
        s = state()
        if (self.b == True):
            s.m = self.m-M
            s.c = self.c-C
            s.b = False
        else:
            s.m = self.m + M
            s.c = self.c + C
            s.b = True
        #remember where we came from        
        s.predecessor_state = self
        return s
    
    def display(self):
        """
        print positions of missionaries, cannibals and boat on left bank
        """
        if (self.b):
            print str(self.m) + "\t\t" + str(self.c )+ "\t\tleft"
        else:
            print str(self.m) + "\t\t" + str(self.c )+ "\t\tright"