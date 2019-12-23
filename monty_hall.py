import random

# Monty Hall Door Problem Simulation
# A simple simulation of the infamous Monty Hall Door Problem. The original problem was as follows: A contestant on a game show is 
# attempting to win a prize car, which is hidden behind one of three doors alongside two goats. The contestant first picks a door, then,
# without opening the chosen door, the host opens one of the two remaining doors to reveal a goat. The problem is then whether or not 
# the contestant is better off switching to the remaining unopened door or sticking by his original #choice. Most people reason that
# because one car and one one goat remain between the two doors, there is no advantage to be gained by switching doors, and the 
# contestant could either switch  or stay with equal opportunity for success. The counterintuitive solution, however, is that the 
# contestant is always better off switching. While this can be shown formally, the  purpose of this program is to demonstrate the 
# validity of this claim statistically, by running trials of each strategy and noting the difference in average rate of success.


# Generates a list of three doors, with False representing a goat and True the prize car.
def generateDoors():
    doors = [False, False, False]
    prizeDoor = random.choice((0,1,2))
    doors[prizeDoor] = True
    return doors

# Selects a door for the host to open, given the original arrangment and the contestant's choice. Doors is a list of boolean values and
# contestant is an integer between 1 and 3 representing one of three doors.
def openDoor(doors, contestant):
    # Determine the remaining unopened doors
    remainingDoors = [1,2,3]
    remainingDoors.remove(contestant)
    # Determine which of the remaining two doors contains a goat, and make it the host's choice.  
    if not doors[remainingDoors[0] - 1]: 
        hostChoice = remainingDoors[0]
    elif not doors[remainingDoors[1] -1]:
        hostChoice = remainingDoors[1]
    return hostChoice

# Implements the indifferent strategy, swapping doors with a 50% chance. Takes a list of doors (booleans) and two selected doors. 
# (integer) as arguments. 
def indifferentStrat(doors, contestant, host):
    change = random.choice((True,False))
    if change:
        # As the sum of door numbers 1,2, and 3 is 6, the third door number can be found by subtracting the other two from 6. An 
        # additional 1 is subtracted to account for the zero-based indexing of the list of doors.
        return doors[5 - contestant - host] 
    else:
        # As above, 1 is subtracted from the contestant's door to subtract for zero-based indexing.
        return doors[contestant - 1]

# Implements the always change strategy, swapping doors 100% of the time. Takes a list of doors (booleans) and two selected doors 
# (integer) as arguments.
def alwaysChangeStrat(doors, contestant, host):
    return doors[5 - contestant - host]

# Runs a simulation of both strategies for n trials, returning the total number of trials and the rate of success for each.
def runSim(n):
    indifferentSuccesses = 0
    alwaysChangeSuccesses = 0
    for i in range(n-1):
        doors = generateDoors()
        contestantChoice = random.choice([1,2,3])
        hostChoice = openDoor(doors, contestantChoice)
        if indifferentStrat(doors, contestantChoice, hostChoice):
            indifferentSuccesses += 1
        if alwaysChangeStrat(doors, contestantChoice, hostChoice):
            alwaysChangeSuccesses += 1
        

    print('Total number of trials:', n)
    print('Sucesses for Indifferent Strategy:', indifferentSuccesses)
    print('Successes for Always Change Strategy:', alwaysChangeSuccesses)


runSim(10000)

        
        
        
