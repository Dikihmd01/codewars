def close_compare(a, b, margin=0):
    distance = abs(a-b)
    if distance <= margin:
      return 0
    elif a < b:
      return -1
    else:
      return 1
