'''
Railway Station
Problem Description
Given schedule of trains and their stoppage time at a Railway Station, find minimum number of platforms needed.

Note -

If Train A's departure time is x and Train B's arrival time is x, then we can't accommodate Train B on the same platform as Train A.

Constraints
1 <= N <= 10^5

0 <= a <= 86400

0 < b <= 86400

Number of platforms > 0

Input
First line contains N denoting number of trains.

Next N line contain 2 integers, a and b, denoting the arrival time and stoppage time of train.

Output
Single integer denoting the minimum numbers of platforms needed to accommodate every train.

Time Limit
1

Examples
Example 1

Input

3

10 2

5 10

13 5

Output

2

Explanation

The earliest arriving train at time t = 5 will arrive at platform# 1. Since it will stay there till t = 15, train arriving at time t = 10 
will arrive at platform# 2. Since it will depart at time t = 12, train arriving at time t = 13 will arrive at platform# 2.

Example 2

Input

2

2 4

6 2

Output

2

Explanation

Platform #1 can accommodate train 1.

Platform #2 can accommodate train 2.

Note that the departure of train 1 is same as arrival of train 2, i.e. 6, and thus we need a separate platform to accommodate train 2.



'''

trainNum = int(input())
trainDic = {}
listVal = []
for i in range(1,trainNum+1):
    val = list(map(int, input().split()))
    val.append(sum(val))
    listVal.append(val)
# print(listVal)
listVal.sort()
print(listVal)
platFormCount = 1
initalVal = listVal[0]
for i in listVal[1:]:
    if(initalVal >i[0]):
        pass