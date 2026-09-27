# solution handed in for the weekly exercise
import math


# NOTE: greatest common divisor with euclid's algorithm
def gcd_two(a, b):
  while b != 0:
    a, b = b, a % b
  return a


def lcm_two(a, b):
  return a // gcd_two(a, b) * b


# fold gcd and lcm over the whole list (helper)
def gcd_list(nums):
  result = nums[0]
  for i in range(1, len(nums)):
    result = gcd_two(result, nums[i])
  return result


def lcm_list(nums):
  result = 1
  for n in nums:
    result = lcm_two(result, n)
  return result


def coprime_pairs(nums):
  pairs = []
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if gcd_two(nums[i], nums[j]) == 1:
        pairs.append((nums[i], nums[j]))
  return pairs


def main():
  values = []
  for token in input().split():
    number = abs(int(token))
    if number > 0 and number < 100000:
      values.append(number)
  if not values:
    print("no valid numbers")
    return
  g = gcd_list(values)
  l = lcm_list(values)
  if g == math.gcd(*values):
    status = "ok"
  else:
    status = "mismatch"
  print("gcd", g, "lcm", l, status)
  pairs = coprime_pairs(values)
  total = 0
  for a, b in pairs:
    total = total + a + b
  print("coprime pairs:", len(pairs), "sum", total)


# start the program
main()
