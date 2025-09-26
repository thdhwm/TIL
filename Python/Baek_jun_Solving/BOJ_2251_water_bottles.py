from collections import deque
import sys
sys.stdin = open('input.txt')

def bottle(arr):
  q = deque([arr])
  limits = [A, B, C]
  while q:
      jugs = q.popleft()   # ex. 0, 0, 10
      
      for i in range(3):   # 0, 1, 2
          if not jugs[i]:
              continue
          
          for j in range(3):
              next_jugs = jugs[:]
              if i == j:
                  continue    
              
              if jugs[j] == limits[j]:
                  continue
              
              waters = jugs[i] + jugs[j]
              next_jugs[j] = min(waters, limits[j])
              next_jugs[i] = waters - next_jugs[j]
              
              if tuple(next_jugs) in water_set:
                  continue
              
              if next_jugs[0] == 0:
                  result.add(next_jugs[2])
                
              water_set.add(tuple(next_jugs))
              q.append(next_jugs)


A, B, C = map(int, input().split())
water = C
water_set = set()
result = set()
bottles = [0, 0, water]

bottle(bottles)
ans = list(result)
ans.sort()

print(*ans)
