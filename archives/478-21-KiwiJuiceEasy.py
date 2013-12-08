import math
import string

class KiwiJuiceEasy:
    def thePouring(self, capacities, bottles, fromId, toId):

        for i in range(len(fromId)):
            f = fromId[i]
            t = toId[i]
            vol = bottles[f]
            space = capacities[t] - bottles[t]
            if vol <= space:
                bottles[t] = bottles[t] + vol
                bottles[f] = 0
            else:
                bottles[t] = capacities[t]
                bottles[f] = bottles[f] - space
        return bottles

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, p2, p3, hasAnswer, p4):
    sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("{"))
    for i in range(len(p0)):
        if (i > 0):
            sys.stdout.write(str(","))

        sys.stdout.write(str(p0[i]))

    sys.stdout.write(str("}") + str(",") + str("{"))
    for i in range(len(p1)):
        if (i > 0):
            sys.stdout.write(str(","))

        sys.stdout.write(str(p1[i]))

    sys.stdout.write(str("}") + str(",") + str("{"))
    for i in range(len(p2)):
        if (i > 0):
            sys.stdout.write(str(","))

        sys.stdout.write(str(p2[i]))

    sys.stdout.write(str("}") + str(",") + str("{"))
    for i in range(len(p3)):
        if (i > 0):
            sys.stdout.write(str(","))

        sys.stdout.write(str(p3[i]))

    sys.stdout.write(str("}"))
    print(str("]"))
    obj = KiwiJuiceEasy()
    startTime = time.clock()
    answer = obj.thePouring(p0, p1, p2, p3)
    endTime = time.clock()
    res = True
    print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
    if (hasAnswer):
        print(str("Desired answer:"))
        sys.stdout.write(str("\t") + str("{"))
        for i in range(len(p4)):
            if (i > 0):
                sys.stdout.write(str(","))

            sys.stdout.write(str(p4[i]))

        print(str("}"))

    print(str("Your answer:"))
    sys.stdout.write(str("\t") + str("{"))
    for i in range(len(answer)):
        if (i > 0):
            sys.stdout.write(str(","))

        sys.stdout.write(str(answer[i]))

    print(str("}"))
    if (hasAnswer):
        if (len(answer) != len(p4)):
            res = False
        else:
            for i in range(len(answer)):
                if (answer[i] != p4[i]):
                    res = False




    if (not res):
        print(str("DOESN'T MATCH!!!!"))
    elif ((endTime - startTime) >= 2):
        print(str("FAIL the timeout"))
        res = False
    elif (hasAnswer):
        print(str("Match :-)"))
    else:
        print(str("OK, but is it right?"))

    print(str(""))
    return res

all_right = True


# ----- test 0 -----
p0 = [20,20]
p1 = [5,8]
p2 = [0]
p3 = [1]
p4 = [0,13]
all_right = KawigiEdit_RunTest(0, p0, p1, p2, p3, True, p4) and all_right
# ------------------

# ----- test 1 -----
p0 = [10,10]
p1 = [5,8]
p2 = [0]
p3 = [1]
p4 = [3,10]
all_right = KawigiEdit_RunTest(1, p0, p1, p2, p3, True, p4) and all_right
# ------------------

# ----- test 2 -----
p0 = [30,20,10]
p1 = [10,5,5]
p2 = [0,1,2]
p3 = [1,2,0]
p4 = [10,10,0]
all_right = KawigiEdit_RunTest(2, p0, p1, p2, p3, True, p4) and all_right
# ------------------

# ----- test 3 -----
p0 = [14,35,86,58,25,62]
p1 = [6,34,27,38,9,60]
p2 = [1,2,4,5,3,3,1,0]
p3 = [0,1,2,4,2,5,3,1]
p4 = [0,14,65,35,25,35]
all_right = KawigiEdit_RunTest(3, p0, p1, p2, p3, True, p4) and all_right
# ------------------

# ----- test 4 -----
p0 = [700000,800000,900000,1000000]
p1 = [478478,478478,478478,478478]
p2 = [2,3,2,0,1]
p3 = [0,1,1,3,2]
p4 = [0,156956,900000,856956]
all_right = KawigiEdit_RunTest(4, p0, p1, p2, p3, True, p4) and all_right
# ------------------

if (all_right):
    print(str("You're a stud (at least on the example cases)!"))
else:
    print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# Taro has prepared delicious kiwi fruit juice. He poured it into N bottles numbered from 0 to N-1. The capacity of the i-th bottle is capacities[i] liters, and he poured bottles[i] liters of kiwi juice into this bottle.
#
#
# Now he wants to redistribute juice in the bottles. In order to do this, he will perform M operations numbered from 0 to M-1 in the order in which he will perform them. For the i-th operation, he will pour kiwi juice from bottle fromId[i] to bottle toId[i]. He will stop pouring when bottle fromId[i] becomes empty or bottle toId[i] becomes full, whichever happens earlier.
#
#
# Return an tuple (integer) that contains exactly N elements and whose i-th element is the amount of kiwi juice in the i-th bottle after all pouring operations are finished.
#
#
#
# DEFINITION
# Class:KiwiJuiceEasy
# Method:thePouring
# Parameters:tuple (integer), tuple (integer), tuple (integer), tuple (integer)
# Returns:tuple (integer)
# Method signature:def thePouring(self, capacities, bottles, fromId, toId):
#
#
# CONSTRAINTS
# -capacities will contain between 2 and 50 elements, inclusive.
# -Each element of capacities will be between 1 and 1,000,000, inclusive.
# -capacities and bottles will contain the same number of elements.
# -For each i, bottles[i] will be between 0 and capacities[i], inclusive.
# -fromId will contain between 1 and 50 elements, inclusive.
# -fromId and toId will contain the same number of elements.
# -Each element of fromId and toId will be between 0 and N-1, inclusive, where N is the number of elements in capacities.
# -For each i, fromId[i] and toId[i] will be distinct.
#
#
# EXAMPLES
#
# 0)
# {20, 20}
# {5, 8}
# {0}
# {1}
#
# Returns: {0, 13 }
#
# He pours kiwi juice from bottle 0 to bottle 1. After pouring, bottle 0 will become empty and bottle 1 will contain 13 liters of kiwi juice.
#
# 1)
# {10, 10}
# {5, 8}
# {0}
# {1}
#
# Returns: {3, 10 }
#
# He will stop pouring when bottle 1 becomes full.
#
# 2)
# {30, 20, 10}
# {10, 5, 5}
# {0, 1, 2}
# {1, 2, 0}
#
# Returns: {10, 10, 0 }
#
#
#
# 3)
# {14, 35, 86, 58, 25, 62}
# {6, 34, 27, 38, 9, 60}
# {1, 2, 4, 5, 3, 3, 1, 0}
# {0, 1, 2, 4, 2, 5, 3, 1}
#
# Returns: {0, 14, 65, 35, 25, 35 }
#
#
#
# 4)
# {700000, 800000, 900000, 1000000}
# {478478, 478478, 478478, 478478}
# {2, 3, 2, 0, 1}
# {0, 1, 1, 3, 2}
#
# Returns: {0, 156956, 900000, 856956 }
#
#
#
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
