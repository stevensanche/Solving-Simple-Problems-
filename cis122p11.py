'''
CIS 122 Spring 2022 Project 1-1
Author: Steven Sanchez-Jimenez, C. Science
Description: Intro to computational problem-solving: use Python
numeric data types and operations to solve small problems.
'''


'''Part 1'''
cost_t = 20
ttl_shirts =101
ttl_green = (ttl_shirts//2)
ttl_yellow = (ttl_shirts - ttl_green)+(ttl_shirts%2)
'''since the problem stated that there is going to be one more yellow shirt than
green, the line of code +(ttl_shirts%2) should be on the tt_yellow result'''
ttl_green_cost = ttl_green*cost_t
cost_yellow = cost_t - (cost_t * .5)
ttl_yellow_cost = ttl_yellow * cost_yellow
ttl_cost = ttl_yellow_cost + ttl_green_cost
print('The total cost is', ttl_cost)

'''Part 2'''

orange_skittles = 7
green_skittles = orange_skittles * 3
purple_skittles = orange_skittles + green_skittles
red_skittles = purple_skittles / 2
yellow_skittles = 30
print (orange_skittles , green_skittles , purple_skittles , red_skittles , yellow_skittles)

'''In this section, I will be changing orange skittles to 6 instead of 7'''

orange_skittles = 6
green_skittles = orange_skittles * 3
purple_skittles = orange_skittles + green_skittles
red_skittles = purple_skittles / 2
yellow_skittles = 40
print (orange_skittles , green_skittles , purple_skittles , red_skittles , yellow_skittles)

'''Part 3'''

'''In this code, every number that is given is all in minutes, so as an example, one_day
will give you the number of how many minutes are in that day. '''

one_minute = 1
one_hour = one_minute * 60
one_day = one_hour * 24
one_y9ear = one_day * 365
print (bdskbfk)

