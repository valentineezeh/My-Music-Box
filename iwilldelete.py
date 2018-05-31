
'''def count_evens(nums):
  evens = []
  for i in nums:
    if i%2 == 0:
      evens.append(i)

    else:
        return 0

    return evens
'''

'''def count_evens(nums):
    evens = []
    odd = []
    for i in nums:
        if i % 2 == 0:
            evens.append(i)
        elif i % 2 != 0:
            odd.append(i)


    print evens
    for i in range(len(evens)):
        evens[i]+=1

        return evens[i]

print(count_evens([2, 1, 2, 3, 4]))'''

'''def big_diff(nums):
    max_value = 0
    min_value = 0
    for i in nums:
        if i == max(nums):
            max_value = max(nums)
        elif i == min(nums):
            min_value = min(nums)
    return max_value - min_value

print(big_diff([10, 3, 5, 6]))'''





#sum13([1, 2, 2, 1, 13])


'''print(sum([1, 2, 2, 1, 13]))'''

'''def front_back(str):
    if len(str)<=1:
        print(str)
    else:
        i = str[-1]
        p = str[0]
        m = str[1:-1]
        print(i)
        print(p)
        print(m)

        print(i + m + p)


front_back('a')'''


'''def extra_end(str):
    m = str[:2]
    print m


extra_end('Hello')'''

'''def first_half(str):
  m = len(str)/2
  print str[:3]



first_half('WooHoo')'''

def in1to10(n, outside_mode):
  while outside_mode is False:
    if n in range(1, 11):
      return True
      break
    else:
      return False
  while outside_mode is True:
    if n <=1 or n >= 10:
      return True
      break
    else:
      return False


print(in1to10(11, True) )















