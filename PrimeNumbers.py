#!/usr/bin/env python
# coding: utf-8

# # Print Every Prime Number Between 1 and 1000

# In[1]:


for candidate in range(1, 1001):            # Loop through possible primes
    failed = False                          
    
    # Loop through possible factors (factors can be no more than half the
    # candidate, so no need to check anything greater)
    for i in range(2, int(candidate/2)+1):
        if(candidate % i == 0):             # Check if i is a factor of the candidate
            failed = True                   
            break                           # Exit the loop on the first failure
    if(failed): continue                    # Move onto the next candidate after failure
    print(candidate)

