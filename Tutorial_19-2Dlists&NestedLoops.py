#creating a 2D List
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(number_grid[1][2]) #row first then col and starts at 0

#nested for loop
for row in number_grid:
    for col in row:
        print(col)

for r in number_grid:
    print(r)
    #cycle = r
    #print(number_grid[cycle])
for j in range(3):
    i = number_grid[j][0] + number_grid[j][1]
    print(i)
