str_ = "Hello *orld is mind"

mass_ = str_.split(" ")
print(mass_)
correct_word = []
for i in mass_:
    if i[0] != "*":
        correct_word.append(i)

print(correct_word)