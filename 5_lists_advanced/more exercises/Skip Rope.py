string = input()

numbers = [string[i] for i in range(len(string)) if string[i].isdigit()]
letters = [string[i] for i in range(len(string)) if not string[i].isdigit()]
take_ = [int(numbers[i]) for i in range(len(numbers)) if i % 2 == 0]
skip_ = [int(numbers[i]) for i in range(len(numbers)) if i % 2 != 0]

final_letters = []
taken_text = []
for i in range(len(take_)):
    take = int(take_[i])
    skip = int(skip_[i])

    if take >= 0:
        taken_text += letters[:take]
        del letters[:take]

    if skip >= 0:
        for _ in range(skip):
            if len(letters) <= 0:
                break
            del letters[0]
print("".join(map(str, taken_text)))
