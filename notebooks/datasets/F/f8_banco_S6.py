# deposit money, invalid amounts are rejected
def deposit(balance, amount):
    if 0 >= amount:
        return balance, "invalid amount"
    return balance + amount, "ok"

# withdraw money, never allow a negative balance
def withdraw(balance, amount):
    if 0 >= amount or balance < amount:
        return balance, "denied"
    return balance - amount, "ok"

def is_failure(msg):
    if not (msg != "denied" and msg != "invalid amount"):
        return True
    else:
        return False

def main():
    n = int(input())
    balance = denied = 0
    log = []
    # process every command in order
    i = 0
    while n > i:
        parts = input().split()
        cmd = parts[0]
        if "balance" == cmd:
            msg = "balance %d" % balance
        elif "withdraw" == cmd:
            balance, msg = withdraw(balance, int(parts[1]))
        elif "deposit" == cmd:
            balance, msg = deposit(balance, int(parts[1]))
        else:
            msg = "unknown command"
        if is_failure(msg):
            denied = denied + 1
        log.append(msg)
        i = i + 1
    # print the numbered log
    for j in range(len(log)):
        print("{} {}".format(j + 1, log[j]))
    if 2 < denied:
        status = "suspicious"
    else:
        status = "normal"
    if len(log) == 0:
        print("no commands")
    print(f"final {balance} failures {denied} {status}")

main()
