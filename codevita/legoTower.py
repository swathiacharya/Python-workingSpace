'''
Lego Tower
Problem Description
Rahul and his friends are making LEGO towers out of their LEGO bricks. His friends arrive at different times and join the existing 
group in LEGO tower building activity. The rules that Rahul and friends are following are as follows:

To maintain the balance of the tower, they decide to impose a maximum limit on the height of the tower
Each friend brings whatever number of bricks he has, but less than or equal to the maximum height allowed for the tower
In order to differentiate between bricks belonging to different friend, they decide to insert a plate between bricks brought by two friends
Height of each brick as well as height of each plate is 1 unit
Actual height of the constructed tower is total number of (bricks + plates) in that tower
Plate can only be added if bricks above belong to a different friend
In order to avoid losing bricks, they also agree that all the bricks belonging to one friend will be used only in construction of one tower
Once the construction of a new tower has begun, no brick/plate can be added to the previous tower
Help Rahul and friends such that they are of maximum height and minimum number of towers possible
You also have to minimize height factor while maintaining minimum number of towers.

Height factor = ∑ ((Maximum height allowed - height of tower)2)

Example:

Maximum height allowed: 10

Bricks contributed by friends: 6 3 5 2 4

Here we can make 3 towers such that

· 1st tower has 6 + 1 + 3 bricks, total of 10 (1 is for the height of LEGO plate)

· 2nd tower has 5 + 1 + 2 bricks, total of 8 (1 is for the height of LEGO plate)

· 3rd tower has 4 bricks

In this case height factor is: (10 - 10)2 + (10 - 8)2 + (10 - 4)2 = 40

Another way is

· 1st tower has 6 bricks

· 2nd tower has 3 + 1 + 5 bricks, total of 09 (1 is for the height of LEGO plate)

· 3rd tower has 2 + 1 + 4 bricks, total of 07 (1 is for the height of LEGO plate)

In this case, height factor is: (10 - 6)2 + (10 - 9)2 + (10 - 7)2 = 26

It is clear that height factor is minimum in the second case, so the output will be: (6) (3-5) (2-4)

Note: There are no test cases with more than one occurrence of minimum height factor.

Constraints
10 <= H <= 100

1 <= bricks brought by friends <= H

1 <= number of friends <= 10000

Input
First line contains an integer H, which denotes maximum height of the tower allowed

Second line contains arbitrary number of space separated integers which corresponds to the number of bricks brought by the respective friend

Output
The number of bricks and plates in every tower, in the order that they are assembled in, enclosed in parenthesis. Repeat this for all constructed towers. A plate will be represented by "-".

Refer example section for better understanding.

Time Limit
1


Examples
Example 1

Input

10

6 3 5 2 4

Output

(6) (3-5) (2-4)

Explanation:

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@5cc09b8b:image1.png com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@5cc09b8b:image2.png com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@5cc09b8b:image3.png

Example 2

Input

13

2 2 8 9 1 3 1 1 10 8

Output

(2-2) (8) (9) (1-3-1-1) (10) (8)

Explanation:

There can be many possibilities of constructing towers. But with minimum height factor, the correct solution is: (2-2) (8) (9) (1-3-1-1) (10) (8)

'''
