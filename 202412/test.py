listA = ['A','B','C','D','B']
cnt = {}

for alpa in listA:
  try: cnt[alpa] += 1
  except: cnt[alpa] = 1

print(listA[1])
print(cnt)
