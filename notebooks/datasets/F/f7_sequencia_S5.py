import sys

# read the threshold and the list of daily temperatures
def read_input():
    threshold = float(input())
    temps = [float(token) for token in input().split()]
    return threshold, temps

# longest run of consecutive days strictly above the threshold
def longest_streak(temps, threshold):
    best_end = -1
    best = 0
    current = 0
    for i in range(len(temps)):
        if temps[i] > threshold:
            current += 1
            if current > best:
                best = current
                best_end = i
        else:
            current = 0
    return best, best_end

def main():
    threshold, temps = read_input()
    if len(temps) == 0:
        print("no data")
        sys.exit(0)
    best, best_end = longest_streak(temps, threshold)
    # collect the days above the threshold
    hot_days = [d + 1 for d in range(len(temps)) if temps[d] > threshold]
    cool = sum(1 for t in temps if not t > threshold)
    level = "heatwave" if best >= 3 else "normal"
    if best == 0:
        print("no day above", threshold)
    else:
        print("longest streak", best, "days, from day", best_end - best + 2, "to day", best_end + 1)
    print("hot days", hot_days, "cool days", cool, level)

main()
