import math
import string

class BinaryCode:
    def decode(self, message):

        q = list(map(int, message))
        p0 = []
        p0.append(0)
        p0.append(q[0] - p0[0])
        p1 = []
        p1.append(1)
        p1.append(q[0] - p1[0])
        i = 2

        isP0Correct = 1
        isP1Correct = 1

        if q[0] > 1:
            isP0Correct = 0
        if q[0] > 2:
            isP1Correct = 0

        for qn in q[1:-1]:
            p0_num = qn - p0[i-2] - p0[i-1]
            p0.append(p0_num)
            if p0_num != 0 or p0_num != 1:
                isP0Correct = 0
            p1_num = qn - p1[i-2] - p1[i-1]
            p1.append(p1_num)
            if p1_num != 0 or p1_num != 1:
                isP1Correct = 0
            i = i + 1

        if p0[-1]+p0[-2] != q[-1]:
            isP0Correct = 0
        if p1[-1]+p1[-2] != q[-1]:
            isP1Correct = 0

        if isP0Correct:
            p0_ans = "".join(map(str, p0))
        else:
            p0_ans = "NONE"

        if isP1Correct:
            p1_ans = "".join(map(str, p1))
        else:
            p1_ans = "NONE"
        return [p0_ans, p1_ans]

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
    sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("\"") + str(p0) + str("\""))
    print(str("]"))
    obj = BinaryCode()
    startTime = time.clock()
    answer = obj.decode(p0)
    endTime = time.clock()
    res = True
    print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
    if (hasAnswer):
        print(str("Desired answer:"))
        sys.stdout.write(str("\t") + str("{"))
        for i in range(len(p1)):
            if (i > 0):
                sys.stdout.write(str(","))

            sys.stdout.write(str("\"") + str(p1[i]) + str("\""))

        print(str("}"))

    print(str("Your answer:"))
    sys.stdout.write(str("\t") + str("{"))
    for i in range(len(answer)):
        if (i > 0):
            sys.stdout.write(str(","))

        sys.stdout.write(str("\"") + str(answer[i]) + str("\""))

    print(str("}"))
    if (hasAnswer):
        if (len(answer) != len(p1)):
            res = False
        else:
            for i in range(len(answer)):
                if (answer[i] != p1[i]):
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
p0 = "123210122"
p1 = ["011100011","NONE"]
all_right = KawigiEdit_RunTest(0, p0, True, p1) and all_right
# ------------------

# ----- test 1 -----
p0 = "11"
p1 = ["01","10"]
all_right = KawigiEdit_RunTest(1, p0, True, p1) and all_right
# ------------------

# ----- test 2 -----
p0 = "22111"
p1 = ["NONE","11001"]
all_right = KawigiEdit_RunTest(2, p0, True, p1) and all_right
# ------------------

# ----- test 3 -----
p0 = "123210120"
p1 = ["NONE","NONE"]
all_right = KawigiEdit_RunTest(3, p0, True, p1) and all_right
# ------------------

# ----- test 4 -----
p0 = "3"
p1 = ["NONE","NONE"]
all_right = KawigiEdit_RunTest(4, p0, True, p1) and all_right
# ------------------

# ----- test 5 -----
p0 = "12221112222221112221111111112221111"
p1 = ["01101001101101001101001001001101001","10110010110110010110010010010110010"]
all_right = KawigiEdit_RunTest(5, p0, True, p1) and all_right
# ------------------

if (all_right):
    print(str("You're a stud (at least on the example cases)!"))
else:
    print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# Let's say you have a binary string such as the following:
#
# 011100011
#
# One way to encrypt this string is to add to each digit the sum of its adjacent digits.  For example, the above string would become:
#
# 123210122
#
# In particular, if P is the original string, and Q is the encrypted string, then Q[i] = P[i-1] + P[i] + P[i+1] for all digit positions i.  Characters off the left and right edges of the string are treated as zeroes.
#
# An encrypted string given to you in this format can be decoded as follows (using 123210122 as an example):
#
# Assume P[0] = 0.
# Because Q[0] = P[0] + P[1] = 0 + P[1] = 1, we know that P[1] = 1.
# Because Q[1] = P[0] + P[1] + P[2] = 0 + 1 + P[2] = 2, we know that P[2] = 1.
# Because Q[2] = P[1] + P[2] + P[3] = 1 + 1 + P[3] = 3, we know that P[3] = 1.
# Repeating these steps gives us P[4] = 0, P[5] = 0, P[6] = 0, P[7] = 1, and P[8] = 1.
# We check our work by noting that Q[8] = P[7] + P[8] = 1 + 1 = 2.  Since this equation works out, we are finished, and we have recovered one possible original string.
#
# Now we repeat the process, assuming the opposite about P[0]:
#
# Assume P[0] = 1.
# Because Q[0] = P[0] + P[1] = 1 + P[1] = 1, we know that P[1] = 0.
# Because Q[1] = P[0] + P[1] + P[2] = 1 + 0 + P[2] = 2, we know that P[2] = 1.
# Now note that Q[2] = P[1] + P[2] + P[3] = 0 + 1 + P[3] = 3, which leads us to the conclusion that P[3] = 2.  However, this violates the fact that each character in the original string must be '0' or '1'.  Therefore, there exists no such original string P where the first digit is '1'.
#
# Note that this algorithm produces at most two decodings for any given encrypted string.  There can never be more than one possible way to decode a string once the first binary digit is set.
#
# Given a string message, containing the encrypted string, return a tuple (string) with exactly two elements.  The first element should contain the decrypted string assuming the first character is '0'; the second element should assume the first character is '1'.  If one of the tests fails, return the string "NONE" in its place.  For the above example, you should return {"011100011", "NONE"}.
#
# DEFINITION
# Class:BinaryCode
# Method:decode
# Parameters:string
# Returns:tuple (string)
# Method signature:def decode(self, message):
#
#
# CONSTRAINTS
# -message will contain between 1 and 50 characters, inclusive.
# -Each character in message will be either '0', '1', '2', or '3'.
#
#
# EXAMPLES
#
# 0)
# "123210122"
#
# Returns: { "011100011",  "NONE" }
#
# The example from above.
#
# 1)
# "11"
#
# Returns: { "01",  "10" }
#
# We know that one of the digits must be '1', and the other must be '0'.  We return both cases.
#
# 2)
# "22111"
#
# Returns: { "NONE",  "11001" }
#
# Since the first digit of the encrypted string is '2', the first two digits of the original string must be '1'.  Our test fails when we try to assume that P[0] = 0.
#
# 3)
# "123210120"
#
# Returns: { "NONE",  "NONE" }
#
# This is the same as the first example, but the rightmost digit has been changed to something inconsistent with the rest of the original string.  No solutions are possible.
#
# 4)
# "3"
#
# Returns: { "NONE",  "NONE" }
#
# 5)
# "12221112222221112221111111112221111"
#
# Returns: { "01101001101101001101001001001101001",  "10110010110110010110010010010110010" }
#
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
