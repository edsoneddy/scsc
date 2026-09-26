for i in range(int(input())):
    word = list(input())
    count = 0
    new_word = ""
    for _ in word:
        if (_ != " ") and (count % 2 == 0):
            letter = _.upper()
            new_word = new_word + letter
            count += 1
        elif (_ != " ") and (count % 2 != 0):
            letter = _.lower()
            new_word = new_word + letter
            count+=1
        else:
            new_word = new_word + _
    print(new_word)