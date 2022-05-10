def linear_search(arr, x):
    
  for r in range(len(arr)):
    if arr[r] == x:
      return r
  return -1

