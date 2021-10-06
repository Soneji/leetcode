'''
https://leetcode.com/discuss/interview-question/586284/facebook-interview-question-reverse-to-make-equal
'''

def are_they_equal(array_a, array_b):
  hm = {}
  for i in array_a:
    if i not in hm:
      hm[i] = 1
    else:
      hm[i] += 1

  for i in array_b:
    if i not in hm:
      return False
    else:
      hm[i] -= 1

  for i in hm:
    if hm[i] != 0:
      return False
  return True
