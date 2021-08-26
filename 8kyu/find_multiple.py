def find_multiples(integer, limit):
  lists = []
  for i in range(integer, (limit+1)):
    if (i % integer == 0):
      lists.append(i)
  return lists
find_multiples(2, 6)
