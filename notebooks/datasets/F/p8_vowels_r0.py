def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

text = input()
v, c = count_vowels_consonants(text)
print(v, c)
