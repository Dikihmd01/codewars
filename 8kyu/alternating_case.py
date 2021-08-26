def to_alternating_case(string):
  res=""
  for i in range(len(str(string))):
    if string[i].isupper():
      res = res + string[i].lower()
    else:
      res = res + string[i].upper()
  return res
