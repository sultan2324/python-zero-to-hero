word = "day noon sun moon"
print(word)

choice = input("To win the Lottery,Choose the any character from above word :").lower()


if choice == word[1] or choice == word[5] or choice == word[-6] or choice == word[15]:
    print("Congratulations ! You won the Lottery Price.")
else:
    print("Sorry you did not win the price.")
