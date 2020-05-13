def cellCompete(states, days):
    # copy states[] array into temp [] array 
    temp=[] 
    cellCount = len(states) # It should be 8 as that is given
    for i in range(cellCount+1): 
        temp.append(0) 
    for i in range(cellCount): 
        temp[i] = states[i] 
   
    # Update valye by iterating for given days 
    while (days>0): 
      
        # Finding next values for corner cells 
        temp[0]   = 0^states[1] 
        temp[cellCount-1] = 0^states[cellCount-2] 
   
        # Compute values of intermediate cells 
        # If both cells active or 
        # inactive, then temp[i]=0 
        # else temp[i] = 1. 
        for i in range(1,cellCount-2+1): 
            temp[i] = states[i-1] ^ states[i+1] 
   
        # Copy temp[] to states[] 
        # for next iteration 
        for i in range(cellCount): 
            states[i] = temp[i] 
        days-=1
    return states