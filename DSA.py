def max_sum_subarray(arr): 
 currrent_sum = 0

 max_so_far = arr[0]
 si = 0; ei =0; poi = 0
 for i in range(0, len(arr)):
  currrent_sum = currrent_sum + arr[i]

  if(max_so_far < currrent_sum):
   max_so_far = currrent_sum
   si = poi
   ei=i

  if(currrent_sum<0):
   currrent_sum = 0
   poi = i+ 1

 print(max_so_far)

arr = [2,-2,5,6,8,-6]
max_sum_subarray(arr)
  