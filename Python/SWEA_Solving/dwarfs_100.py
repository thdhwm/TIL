heights = [0] * 9
for i in range(9):
    heights[i] = int(input())

diff = sum(heights) - 100


for i in range(9):
    for j in range(9):    # idx 변해서 pop 쓰면 안댐
        if i != j and heights[i] + heights[j] == diff:
            phony_1 = heights[i]
            phony_2 = heights[j]

heights.remove(phony_1)
heights.remove(phony_2)
heights = sorted(heights)

for height in heights:
    print(height)

