'''
The Angel vs Devil
Problem Description
In a board game of dimension(12x12) called Angels vs Devils, various Devils try to kill an Angel whose aim is to get across the board. 
Each Devil has different powers.

Starting point of the Angel can be on any border but not on the corners of the board. Starting point will be provided as input. 
Angel will walk in a straight line across the board. Starting points of all three types of devils will be provided as input. 
Their powers are as follows.

LUCIQUARE (L): His starting point can be on any of the four borders of the board. He leaves a poison trail and moves in 'L' 
shape such that it is possible to create the biggest square along with the borders of the board. Square may or may not be formed 
in 12 seconds within which the angel crosses from one end of the board to other.

THREE LEGGED EEK (E): She is a large three legged devil. She crushes the angel if he comes into any of those 3 boxes where her legs are placed.
 She can only walk diagonally and starts moving towards the cell A1. If she reaches the border she returns on the same path and keeps moving to
 and fro like this.

For example the image below she is where its mentioned E1 in the 1st second, she is at E2 in the 2nd second, E3 in the 3rd second, in the
 4th second she is again in the squares where E2 is mentioned, in the 5th second she is again in the squares where E1 is mentioned, in the
  6th second she is in the squares where E6 is mentioned, in the 7th second she is in the squares where E7 is mentioned since she has reached
   border of the board she will move back again in the same path.

MUTO (M): He can be move to other cells without the need to traverse the path. He can be present at vertically, diagonally, horizontally 
opposite cells at subsequent seconds. He makes these moves in clockwise manner. If angel comes on the same cell as him, he will convert the 
Angel into a Muto.

Note:- All four entities move at the speed of 1 cell per second.

com.tcs.cv.automata.ei.middleware.DocxToHtmlConverter@1a927370:image1.png

Constraints
Angel starts from any of the four borders but not from the corners.

Starting points of angel and all the devils will be different.

In case angel moves to a cell where he meets more than one devil, the angel dies.

It is possible that two or more devils are present in the same cell in the same second

Input
First Line provides the cell(row, col) which is the starting point of Angel

Second Line contains types of devils in order denoted by { L, E, M } separated by '|'

Third Line contains starting points of devils in order mentioned in the 2nd line of input separated by '|'

Output
Output depends on events that occur in 12 second window.

· If Angel successfully crosses the board print 'WON'

· If Angel gets converted into muto print 'MUTO'

· If Angel dies then print the cell number in which the Angel died

Time Limit
1


Examples
Example 1

Input

I12

E|M|L

D9|C2|F1

Output

WON

Explanation

Initial Board Position is displayed in the image by Bold Initials (A1, E1, M1, L1) on the board. Their positions in subsequent seconds is displayed by A2,A3, and E2,E3 and so on. At 2nd Second of the game, Angel will be at I11, EEK will be at B9,C8, and D7. Muto will be at J2 and Luciquare will move to F2 leaving the trail behind.

As shown in the image, EEK will be moving to and fro and will not come in the path of the Angel. Muto can only be at points C2,J2,J11, and C11 at any point in the game. These points also don't come in path of the Angel.

Angel will come at box I7 in the 6th second, Luciquare will take 10 seconds to reach there. Hence Angel will not be in the path of any of the devils. So the outcome will be that the angel will cross the board. Hence, the output will be 'WON'.

Example 2

Input

L3

M|L|E

C10|F12|G3

Output

MUTO

Explanation

MUTO and Angel will be in the same box in the third second and Muto will convert the Angel into a Muto. So the output will be 'MUTO'.

Example 3

Input

A5

E|L|M

H4|J1|K3

Output

J5

Explanation

Angel will be killed at position J5 because of Luciquares's poisonous trail.
'''