""" ----------------------------------------------------------------------------
******** Search Code for DFS,BFS and other search methods
******** (expanding front and extending queue)
******** author:  Jonathan Baxevanidis
********
"""
 

import copy

spaces = {
    1: [2,4],
    2: [1,3],
    3: [2,4,5],
    4: [1,3,6],
    5: [3,6],
    6: [4,5]
}

def enter(state):
    if state[0]!=0 and state[1][0][0]=='P' and state[1][1]=='NO': # υπάρχει πλατφόρμα στο χώρο εισόδου χωρίς αυτοκίνητο (NO)
        new_state=[state[0]-1] + [[state[1][0], 'YES']] + state[2:] # είσοδος αυτοκινήτου στο parking  
        return new_state


def swap(state_l, i, j): 
    state_l[i], state_l[j] = state_l[j], state_l[i] 
    return state_l



def neighbour1(state):    
    
    elem=['E','NO']
    i=state.index(elem) if elem in state else -1
    if i >=0:
        swap(state, i, spaces[i][0])
        return state
        

def neighbour2(state):
    
    elem=['E','NO']
    i=state.index(elem) if elem in state else -1
    if i >=0:
        swap(state, i, spaces[i][1])
        return state

def neighbour3(state):

    elem=['E','NO']
    i=state.index(elem) if elem in state else -1
    if i >=0 and len(spaces[i]) >= 3:
        swap(state, i, spaces[i][2])  #with spaces[i][1] runs only for max 3 cars with both algorithms || with spaces[i][2] BFS ends with a solution but DFS run forever no error though
        return state

""" ----------------------------------------------------------------------------
**** FRONT
**** Διαχείριση Μετώπου
"""
def find_children(state):
    
    children=[]
    
    enter_state=copy.deepcopy(state)
    enter_child=enter(enter_state)
    
    tr1_state=copy.deepcopy(state)
    tr1_child=neighbour1(tr1_state)
    
    tr2_state=copy.deepcopy(state)
    tr2_child=neighbour2(tr2_state)
    
    tr3_state=copy.deepcopy(state)
    tr3_child=neighbour3(tr3_state)
    
    if tr1_child is not None: 
        children.append(tr1_child)
           
    if tr2_child is not None:
        children.append(tr2_child) 
    
    if tr3_child is not None:
        children.append(tr3_child) 
   
    if enter_child is not None: 
        children.append(enter_child)
        
    return children


""" ----------------------------------------------------------------------------
** initialization of front
** Αρχικοποίηση Μετώπου
"""

def make_front(state):
    return [state]

""" ----------------------------------------------------------------------------
**** expanding front
**** επέκταση μετώπου    
"""

def expand_front(front, method):  
    if method=='DFS':        
        if front:
            print("Front:")
            print(front)
            node=front.pop(0)
            for child in find_children(node):     
                front.insert(0,child)
    
    elif method=='BFS':
        if front: 
            print("Front:")
            print(front)
            node=front.pop(0)
            for child in find_children(node):     
                front.append(child)
    return front
'''
    elif method=='BestFS':
        if front:
            if front=='BestFS':
                print("Front:")
                print(front)
 #'''           
    #else: "other methods to be added"        
    

""" ----------------------------------------------------------------------------
**** QUEUE
**** Διαχείριση ουράς
"""

""" ----------------------------------------------------------------------------
** initialization of queue
** Αρχικοποίηση ουράς
"""

def make_queue(state):
    return [[state]]

""" ----------------------------------------------------------------------------
**** expanding queue
**** επέκταση ουράς
"""

def extend_queue(queue, method):
    if method=='DFS':
        print("Queue:")
        print(queue)
        node=queue.pop(0)
        queue_copy=copy.deepcopy(queue)
        children=find_children(node[-1])
        for child in children:
            path=copy.deepcopy(node)
            path.append(child)
            queue_copy.insert(0,path)
    
    elif method=='BFS': 
        if queue:
            print("Queue:")
            print(queue)
            node=queue.pop(0)
            queue_copy=copy.deepcopy(queue)
            children=find_children(node[-1])
            for child in children:
                path=copy.deepcopy(node)
                path.append(child)
                queue_copy.append(path)
    '''
    elif method=='BestFS':
        new = list(queue)
        new.sort(key=lambda x:x[1])
    #'''
    #else: "other methods to be added" 
    
    return queue_copy
            
""" ----------------------------------------------------------------------------
**** Problem depending functions
**** ο κόσμος του προβλήματος (αν απαιτείται) και υπόλοιπες συναρτήσεις σχετικές με το πρόβλημα

  #### to be  added ####
"""

""" ----------------------------------------------------------------------------
**** Basic recursive function to create search tree (recursive tree expansion)
**** Βασική αναδρομική συνάρτηση για δημιουργία δέντρου αναζήτησης (αναδρομική επέκταση δέντρου)
"""

def find_solution(front, queue, closed, method):
       
    if not front:
        print('_NO_SOLUTION_FOUND_')
    
    elif front[0] in closed:
        new_front=copy.deepcopy(front)
        new_front.pop(0)
        new_queue=copy.deepcopy(queue)
        new_queue.pop(0)
        find_solution(new_front, new_queue, closed, method)
    
    elif is_goal_state(front[0]):
        print('_GOAL_FOUND_')
        print(queue[0])
    
    else:
        closed.append(front[0])
        front_copy=copy.deepcopy(front)
        front_children=expand_front(front_copy, method)
        queue_copy=copy.deepcopy(queue)
        queue_children=extend_queue(queue_copy, method)
        closed_copy=copy.deepcopy(closed)
        find_solution(front_children, queue_children, closed_copy, method)
        
        
"""" ----------------------------------------------------------------------------
** Executing the code
** κλήση εκτέλεσης κώδικα
"""

def is_goal_state(state):   #otan den exoun meinei alla autokinita
    if state[0] == 0:
        return True 

def main():
    
    initial_state = [2, ['E', 'NO'], ['P1', 'YES'], ['P2', 'YES'], ['P3', 'NO'], ['P4', 'YES'], ['P5', 'NO']]  
    print("Select rhe searching method. \n")
    
    print("Select searching method.\n" 
        "BFS" + "\n"
        "DFS" + "\n"
        "BestFS" +  "\n"
        "Usage: Input the name of the method you want as it is shown"
    )

    print("Input your method:")
    method=input()
    
    """ ----------------------------------------------------------------------------
    **** starting search
    **** έναρξη αναζήτησης
    """
    
    print('____BEGIN__SEARCHING____')
    find_solution(make_front(initial_state), make_queue(initial_state), [], method)
        

if __name__ == "__main__":
    main()
    
# with BFS [0, ['P4', 'YES'], ['E', 'NO'], ['P2', 'YES'], ['P3', 'YES'], ['P5', 'NO'], ['P1', 'YES']]]
#with DFS runs and never stops
