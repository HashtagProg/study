def solution(a, b):
  answer = 0
  nA = int(str(a) + str(b))
  nB = 2 * a * b
  if(nA < nB):
    answer = nB
  else:
    answer = nA

  return answer

solution(2, 91)