def remove(s):
  if "!" in s[-1]:
    return s.rstrip(s[-1])
  else:
    return s
