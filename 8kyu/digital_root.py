def digital_root(n):
  if n < 10:
    return n
    
  n = n % 10 + digital_root(n // 10)
  return n
digital_root(123)
