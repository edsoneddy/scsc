# solution handed in for the weekly exercise
import bisect


# NOTE: iterative binary search, returns an index or -1
def binary_search(data, target):
  low = 0
  high = len(data) - 1
  while low <= high:
    mid = (low + high) // 2
    if data[mid] == target:
      return mid
    elif data[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1


def lower_bound(data, target):
  low, high = 0, len(data)
  while low < high:
    mid = (low + high) // 2
    if data[mid] < target:
      low = mid + 1
    else:
      high = mid
  return low


# copies of the target = distance between the bounds of target and target + 1 (helper)
def count_occurrences(data, target):
  return lower_bound(data, target + 1) - lower_bound(data, target)


def main():
  data = []
  for token in input().split():
    data.append(int(token))
  data.sort()
  queries = int(input())
  total = 0
  for q in range(queries):
    target = int(input())
    index = binary_search(data, target)
    c = count_occurrences(data, target)
    if bisect.bisect_left(data, target) == lower_bound(data, target):
      check = "ok"
    else:
      check = "bad"
    if not index == -1 and c > 0:
      print(target, "found", c, "check", check)
    else:
      print(target, "missing", "check", check)
    total = total + c
  print("total matches", total)


# start the program
main()
