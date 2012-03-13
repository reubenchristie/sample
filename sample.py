#!/usr/bin/env python
import math 
def prepare_expr(tree={}):
    """
    tree representing a basic mathematical expression, where the number of children extending from
    any node is 2. Each of the leaves is a real number and each node represents a mathematical
    operator from the set(+, -, *, /) that is to be applied to all of the leaves of that node.
    returns the calculated value of the tree.
    """
    expr=''
    for op, values in tree.items():        
        for item in values:
            if type(item) == int or type(item) == float:
                #append to expr
                if expr == "":
                    expr =  '('+str(item)
                else:
                    expr = expr + op + str(item)
            elif type(item) ==  dict:
                if expr == "":
                    expr = '(' + prepare_expr(item)
                else:
                    expr = expr + op + prepare_expr(item)
            else:
                pass
    return expr+')'

def number_spiral(h, w):
    """
    this function accepts an integer width and height and generates a number spiral.
    the numbers are right-aligned and padded with spaces in columns which are as wide 
    as the widest number in the spiral. Each column is then separated by a single space
    """
    #caclulate max possible digits for a number in the spiral
    digits = int(math.log10(h*w))+1    
    # total number of elements in array
    n = w * h
    # start at top left (row 0 column 0)
    row, column = 0,0
    # first move is on the same row, to the right
    d_row, d_column = 0, 1
    # fill 2d array with dummy values we'll overwrite later
    arr = [[None ]* w for z in range(h)]
    for i in xrange(1,n+1):
        arr[row][column] = i 
        # next row and column
        nrow, ncolumn = row + d_row, column + d_column
        if 0 <= nrow < h and 0 <= ncolumn < w and arr[nrow][ncolumn] == None:
            # no out of bounds accesses or overwriting already-placed elements.
            row, column = nrow, ncolumn
        else:
            # change direction
            d_row , d_column = d_column, -d_row
            row, column = row + d_row, column + d_column
    # print it out!
    for a in range(h):
        for b in range(w):
            print str(arr[a][b]).rjust(digits),            
        print 

def longest_substring(s1, s2):
    """
    accepts two strings of arbitrary and possibly different length. returns the set of longest
    possible substrings common to both, if any exists. 
    """
    m_d_arry = [[0]*(1+len(s2)) for i in xrange(1+len(s1))]
    longest, x_longest = 0, 0
    for x in xrange(1,1+len(s1)):
        for y in xrange(1,1+len(s2)):
            if s1[x-1] == s2[y-1]:
                m_d_arry[x][y] = m_d_arry[x-1][y-1] + 1
                if m_d_arry[x][y]>longest:
                    longest = m_d_arry[x][y]
                    x_longest  = x
            else:
                m_d_arry[x][y] = 0
    return s1[x_longest-longest: x_longest]

def getChange(coins = [],amt=0.0):
    """
    coins is an array representing the quantity of pennies, dimes,nickles,quarters and halves
    and a floating point dollar value and returns array of the smallest possible number of coins
    necessary to represent the dollar amount. 
    """
    change = []
    current_amt=0.0
    for denom, counts in coins:        
        if current_amt>=amt: continue
        if denom+current_amt > amt: continue
        elif current_amt<amt:
            for cnt in xrange(1,counts+1):                
                current_amt+=denom                
                if current_amt>amt:
                    current_amt-=denom
                    cnt-=1
                    break                    
            change.append([denom,cnt])
    #print amt, '-', current_amt, '-',change
    if (current_amt !=amt):
        print 'can not make exact change, closest  change found $',current_amt/100         
    return change

def sortword(word):
    """
    sort a string by characters
    """
    return ''.join(sorted(word))

def print_anagrams(f,wl):
    """
    accepts object f, is the file object containing dictionary words. there is one word per line.
    and, word list. print a data structure which maps each word in the word list to a list of all
    anagrams of that word from the file.
    """    
    filewords = {}    
    words = [sortword(word) for word in wordlist]
    for line in fin:
        w = sortword((line.strip('\n')))
        if (w in filewords):
            filewords[w].append(line.strip('\n'))
        else:
            filewords[w] = [line.strip('\n')]    
    for wrd in words:
        if wrd in filewords:
            print ','.join(filewords[wrd])

if __name__ == '__main__': 
    #test1   
    tree={'+':[1,{'-':[4,3]}]}    
    print eval(prepare_expr(tree))
    #test2
    number_spiral(5, 5)
    #test3    
    print longest_substring('i am testing something','i am that i am who is always doing something')
    #test4
    #this is sorted array , It should be sorted on denomination if it is not sorted.
    chillar = [(50,4),(25,10),(10,9),(5,8),(1,17)]
    dollar_value = 3.17
    #convert dollar amount in to equivalent cents for ease of computing
    chg = getChange(chillar,dollar_value*100)
    print chg
    
    #test5
    #create file called dictionary.txt, with following words one per line,bar use, read, army, mary
    fin = open('dictionary.txt')
    wordlist = ['mary','joe', 'sue', 'dear']
    print_anagrams(fin,wordlist)   
