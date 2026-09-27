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
    return msg == "denied" or msg == "invalid amount"

def main():
    n = int(input())
    balance = denied = 0
    log = []
    # process every command in order
    for i in range(n):
        parts = input().split()
        cmd = parts[0]
        if "deposit" == cmd:
            balance, msg = deposit(balance, int(parts[1]))
        elif "withdraw" == cmd:
            balance, msg = withdraw(balance, int(parts[1]))
        elif "balance" == cmd:
            msg = "balance " + str(balance)
        else:
            msg = "unknown command"
        if is_failure(msg):
            denied += 1
        log.append(msg)
    # print the numbered log
    for j in range(len(log)):
        print(j + 1, log[j])
    status = "suspicious" if 2 < denied else "normal"
    if len(log) == 0:
        print("no commands")
    print("final %d failures %d %s" % (balance, denied, status))

main()
