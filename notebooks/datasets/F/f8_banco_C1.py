# solution handed in for the weekly exercise
# NOTE: deposit money, invalid amounts are rejected
def deposit(balance, amount):
  if amount <= 0:
    return balance, "invalid amount"
  return balance + amount, "ok"


def withdraw(balance, amount):
  if amount <= 0 or amount > balance:
    return balance, "denied"
  return balance - amount, "ok"


def is_failure(msg):
  if msg == "denied" or msg == "invalid amount":
    return True
  else:
    return False


def main():
  n = int(input())
  balance = denied = 0
  log = []
  # process every command in order (helper)
  i = 0
  while i < n:
    parts = input().split()
    cmd = parts[0]
    if cmd == "deposit":
      balance, msg = deposit(balance, int(parts[1]))
    elif cmd == "withdraw":
      balance, msg = withdraw(balance, int(parts[1]))
    elif cmd == "balance":
      msg = "balance " + str(balance)
    else:
      msg = "unknown command"
    if is_failure(msg):
      denied = denied + 1
    log.append(msg)
    i = i + 1
  # print the numbered log (helper)
  for j in range(len(log)):
    print(j + 1, log[j])
  if denied > 2:
    status = "suspicious"
  else:
    status = "normal"
  if not log:
    print("no commands")
  print("final", balance, "failures", denied, status)


# start the program
main()
