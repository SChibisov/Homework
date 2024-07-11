def all_variants(text):
    for obj in range(len(text)):
        for j in range(len(text) - obj):
            yield text[j:j + obj + 1]


a = all_variants("abc")
for i in a:
    print(i)
