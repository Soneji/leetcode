def numberOfWays(arr, k):
  ways = 0
  hm = {}
  for i in arr:
    if i not in hm:
      hm[i] = 1
    else:
      hm[i] += 1

  print(hm)
  
  if (k / 2) in hm:
    x = hm[k/2]
    ways += x * (x - 1 ) / 2

  for i in arr:
    if (k - i) in hm:
      ways += 1
  
  print(ways)
  print(ways/2)
  
  return ways // 2
