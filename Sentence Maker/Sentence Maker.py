def sentence_maker(phrase):
    intoregetives = ("how", "what", "why")
    capitalised = phrase.capitalize()

    if phrase.startswith(intoregetives):
        return "{}?".format(capitalised)
    else: 
        return "{}.".format(capitalised)


print(sentence_maker("How Are You?"))

results = []
while True:
    user_input = input("Say something:")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))

