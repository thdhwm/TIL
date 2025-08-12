heights = [0] * 9
for i in range(9):
    heights[i] = int(input())

diff = sum(heights) - 100


for i in range(9):
    for j in range(9):
        if i != j and heights[i] + heights[j] == diff:
            pass

# idx 변해서 pop 안댐
print(*heights)

