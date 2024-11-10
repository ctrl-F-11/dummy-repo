from itertools import combinations

# Brute force
def compatible(set):
  m = len(set)
  for i in range(m):
    for j in range(m):
      if i != j and ((set[i][0] < set[j][1] and set[j][0] <= set[i][0])
                     or
                     (set[j][0] < set[i][1] and set[i][0] <= set[j][0])):
        return False
  return True

def bruteForce(A):
  if A is None or len(A) == 0:
    return A
  counter = 0
  max_subset = []
  for i in range(len(A)+1):
    for subset in combinations(A,i):
      if len(subset)> len(max_subset) and compatible(subset):
        max_subset = subset
  return list(max_subset)

# An activity Selection Problem greedy approach
def greedyAS(A):
  if A is None or len(A) == 0:
    return A
  A.sort(key = lambda a:a[1])
  sol = [A[0]]
  n = 0
  for i in range(1,len(A)):
    if A[i][0] >= sol[n][1]:
      sol.append(A[i])
      n+=1
  return sol

if __name__ == '__main__':
  print('index.py')
  print('version4')

  start = [1, 3, 0, 5, 8, 5]
  finish = [2, 4, 6, 7, 9, 9]

  activities = [(a_i,a_f) for a_i,a_f in zip(start,finish)]

  print(activities)
  print(bruteForce(activities))
  print(greedyAS(activities))