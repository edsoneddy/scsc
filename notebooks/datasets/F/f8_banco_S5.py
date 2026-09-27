# deposit money, invalid amounts are rejected
def deposit(balance, amount):
    if amount <= 0:
        return balance, "invalid amount"
    return balance + amount, "ok"

# withdraw money, never allow a negative balance
def withdraw(balance, amount):
    if amount <= 0 or amount > balance:
        return balance, "denied"
    return balance - amount, "ok"

def is_failure(msg):
    return msg == "denied" or msg == "invalid amount"

def main():
    n = int(input())
    balance = 0
    denied = 0
    log = []
    # process every command in order
    for i in range(n):
        parts = input().split()
        cmd = parts[0]
        if cmd == "deposit":
            balance, msg = deposit(balance, int(parts[1]))
        else:
            if cmd == "withdraw":
                balance, msg = withdraw(balance, int(parts[1]))
            else:
                if cmd == "balance":
                    msg = "balance " + str(balance)
                else:
                    msg = "unknown command"
        if is_failure(msg):
            denied += 1
        log.append(msg)
    # print the numbered log
    for j in range(len(log)):
        print(j + 1, log[j])
    status = "suspicious" if denied > 2 else "normal"
    if not log:
        print("no commands")
    print("final", balance, "failures", denied, status)

main()
