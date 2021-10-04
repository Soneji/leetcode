def numberOfWays(arr, k):
  ways = 0
  sols = []
  for i in range(len(arr)):
     for j in range(len(arr)):
        
        if i == j or (j, i) in sols:
           continue
        
        if arr[i] + arr[j] == k:
          print(arr[i], arr[j])
          ways += 1
          sols.append((i,j))

  return ways
 
