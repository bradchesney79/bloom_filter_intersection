#!/usr/bin/python

# use python3

# requires cython & pybloomfiltermmap3 (install cython first)
import pybloomfilter

# 2017 Indians Jersey Roster Numbers
indians_numbers = [1,6,7,8,9,10,11,12,22,23,24,26,27,28,30,31,34,35,36,37,39,41,43,44,47,48,51,52,54,55,57,58,59,61,65,66,71,73,74,76]

# 2017 Cubs Jersey Roster Numbers
cubs_numbers = [2,5,6,7,9,12,13,17,18,19,20,22,24,27,28,29,30,32,34,37,38,40,41,43,44,46,47,49,51,52,53,56,71,73,74,75,76]

# manually figured expected result
expected_result = [6,7,9,12,22,24,27,28,30,34,37,41,43,44,47,51,52,71,73,74,76]

# empty result list
actual_result = []

# create a bloom filter
indians = pybloomfilter.BloomFilter(100,0.0001)

# add player jersey numbers to the bloom filter
for player in indians_numbers:
    indians.add(player)

# check for cubs jersey numbers in indians bloom filter
for player in cubs_numbers:
    print("====player #"+str(player)+"====")
    print(str(player in indians))
    if (player in indians):
        # intersecting datapoint, add to result list
        actual_result.append(player)

print("=======================================")
print("==========ACTUAL RESULT================")
for player in actual_result:
    print(str(player))
print("=======================================")
print("=========EXPECTED RESULT===============")
for player in expected_result:
    print(str(player))
print("=======================================")
print("==========RESULTS EQUAL================")
if (set(actual_result)==set(expected_result)):
    print("TRUE")
else:
    print("FALSE")
print("=======================================")
