# solution handed in for the weekly exercise
import sys


# NOTE: read the threshold and the list of daily temperatures
def read_input():
  threshold = float(input())
  temps = []
  for token in input().split():
    temps.append(float(token))
  return threshold, temps


def longest_streak(temps, threshold):
  best = 0
  current = 0
  best_end = -1
  i = 0
  while i < len(temps):
    if temps[i] > threshold:
      current = current + 1
      if current > best:
        best = current
        best_end = i
    else:
      current = 0
    i = i + 1
  return best, best_end


def main():
  threshold, temps = read_input()
  if len(temps) == 0:
    print("no data")
    sys.exit(0)
  best, best_end = longest_streak(temps, threshold)
  # collect the days above the threshold (helper)
  hot_days = []
  for d in range(len(temps)):
    if temps[d] > threshold:
      hot_days.append(d + 1)
  cool = 0
  for t in temps:
    if not t > threshold:
      cool = cool + 1
  if best >= 3:
    level = "heatwave"
  else:
    level = "normal"
  if best == 0:
    print("no day above", threshold)
  else:
    print("longest streak", best, "days, from day", best_end - best + 2, "to day", best_end + 1)
  print("hot days", hot_days, "cool days", cool, level)


# start the program
main()
