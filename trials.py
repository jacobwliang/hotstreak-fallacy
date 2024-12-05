# trial functions
# last 3 digits: 428, p = 28 + 30, streak length 2
import random

def trial(prob: float, n: int): # create the trial array
    '''
    parameters: prob is true shooting percentage, n is number of shots to be taken
    return: array of 50 0s and 1s, 0 meaning miss and 1 meaning hit
    '''
    res = []
    for i in range(n):
        if random.random() > prob: # if a random float 0.0 - 1.0 is less than 0.58
            res.append(0)
        else:
            res.append(1)
    return res

def hstreak_p(t: list): # 2 pointer approach to find hotstreaks
    '''
    parameter: t is a trial of shots
    return: probability of hotstreaking after hitting 2 shots
    '''
    hcount = 0
    fcount = 0
    i = 0
    while i < len(t): 
        c = 0
        if t[i] == 1: # if the curr is a shot make
            c += 1 # increment a count that will be checked for streak length
            r = i + 1
            while r < len(t) and t[r] == 1:
                c += 1
                r += 1
            if c == 2 and r != len(t):
                fcount += 1
            elif c > 2:
                hcount += 1
            
        i += 1
    if hcount + fcount == 0:
        return -1
    return hcount / (hcount + fcount) 

def runtrials(n: int):
    '''
    parameters: n is the number of trials to analyze hotstreaks on
    return: array of hotstreak probabilities
    '''
    res = []
    for i in range(n):
        currtrial = hstreak_p(trial(0.58,50))
        while currtrial == -1: # when there are no streaks, replace trial
            currtrial = hstreak_p(trial(0.58,50))
        res.append(currtrial)
    return res


        
        