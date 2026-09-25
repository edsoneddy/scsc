from collections import deque      
from queue import PriorityQueue    
import sys                         

def adEstructura(ope):          
    stack = []                     
    queue = deque()                
    pqueue = PriorityQueue(maxsize=len(ope))   
    esStack = esQueue = esPqueue = True        

    for op in ope:                             
        if op[0] == 1:                         
            stack.append(op[1])                
            queue.append(op[1])                
            pqueue.put(-op[1])                 
        else:
            if not stack or stack.pop() != op[1]: 
                esStack = False                    
            if not queue or queue.popleft() != op[1]: 
                esQueue = False                       
            if not pqueue or pqueue.get() != -op[1]:  
                esPqueue = False                      

    if esStack and not esQueue and not esPqueue: 
        return "stack"                           
    elif esQueue and not esStack and not esPqueue: 
        return "queue"                             
    elif esPqueue and not esStack and not esQueue: 
        return "priority queue"                    
    elif not esStack and not esQueue and not esPqueue: 
        return "impossible"                            
    else:                                         
        return "not sure"                         

for i in sys.stdin:                               
    if i == "\n":                                 
        break                                     
    N = int(i)                                    
    ope = []                                      
    for _ in range(N):                            
        ope.append(list(map(int, input().split())))
    print(adEstructura(ope))                      
