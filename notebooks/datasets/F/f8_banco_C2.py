# deposit money, invalid amounts are rejected
def add_money(funds, amt):
    if amt <= 0:
        return funds, "invalid amount"
    return funds + amt, "ok"

# withdraw money, never allow a negative balance
def take_money(funds, amt):
    if amt <= 0 or amt > funds:
        return funds, "denied"
    return funds - amt, "ok"

def failed(note):
    if note == "denied" or note == "invalid amount":
        return True
    else:
        return False

def run():
    count = int(input())
    funds = refused = 0
    history = []
    # process every command in order
    idx = 0
    while idx < count:
        words = input().split()
        action = words[0]
        if action == "deposit":
            funds, note = add_money(funds, int(words[1]))
        elif action == "withdraw":
            funds, note = take_money(funds, int(words[1]))
        elif action == "balance":
            note = "balance " + str(funds)
        else:
            note = "unknown command"
        if failed(note):
            refused = refused + 1
        history.append(note)
        idx = idx + 1
    # print the numbered log
    for pos in range(len(history)):
        print(pos + 1, history[pos])
    if refused > 2:
        state = "suspicious"
    else:
        state = "normal"
    if not history:
        print("no commands")
    print("final", funds, "failures", refused, state)

run()
