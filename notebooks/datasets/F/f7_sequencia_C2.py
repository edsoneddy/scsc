import sys

# read the threshold and the list of daily temperatures
def load():
    limit_t = float(input())
    readings = []
    for piece in input().split():
        readings.append(float(piece))
    return limit_t, readings

# longest run of consecutive days strictly above the threshold
def max_run(readings, limit_t):
    top = 0
    cur = 0
    top_end = -1
    day = 0
    while day < len(readings):
        if readings[day] > limit_t:
            cur = cur + 1
            if cur > top:
                top = cur
                top_end = day
        else:
            cur = 0
        day = day + 1
    return top, top_end

def run():
    limit_t, readings = load()
    if len(readings) == 0:
        print("no data")
        sys.exit(0)
    top, top_end = max_run(readings, limit_t)
    # collect the days above the threshold
    hot_list = []
    for k in range(len(readings)):
        if readings[k] > limit_t:
            hot_list.append(k + 1)
    chilly = 0
    for val in readings:
        if not val > limit_t:
            chilly = chilly + 1
    if top >= 3:
        tag = "heatwave"
    else:
        tag = "normal"
    if top == 0:
        print("no day above", limit_t)
    else:
        print("longest streak", top, "days, from day", top_end - top + 2, "to day", top_end + 1)
    print("hot days", hot_list, "cool days", chilly, tag)

run()
