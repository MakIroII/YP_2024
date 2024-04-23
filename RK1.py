import random
rows = int(input())
colls=int(input())
minutes=0
matrix = [[random.choice([0,1,2]) for j in range(rows)] for i in range(colls)]
print(matrix)


def matr(matrix,rows,colls):
    minutes = 0
    change=False
    for i in range (rows):
        for j in range(colls):
            if matrix[i][j]==2:
                minutes+=1
                if i>0 and matrix[i-1][j]==1:
                    matrix[i-1][j]=2
                    change=True
                if i<rows-1 and matrix[i+1][j]==1:
                    matrix[i+1][j]=2
                    change=True
                if j>0 and matrix[i][j-1]==1:
                    matrix[i][j-1]=2
                    change=True
                if j<colls-1 and matrix[i][j+1]==1:
                    matrix[i][j+1]=2
                    change=True
                return change
while matr(matrix,rows,colls)==True:
    minutes+=1
if minutes==0:
    minutes=-1
print(minutes)