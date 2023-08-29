def friend(x):
    
    for person in x:
        if len(person) != 4:
            x.remove(person)
            
    print(x) 
    return(x)
        