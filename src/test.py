import pymorphy3

mf = pymorphy3.MorphAnalyzer()


def manager_name_gent(word) -> str:  # Функция склоняет ФИО в родительном падеже

    if not word:
        return ""
    split_name = word.split()
    res = []
    for word in split_name:
        parse = mf.parse(word)[0]
        print(parse.word)
        if parse.word[-1] == "о":
            res.append(parse.word.capitalize())

        else:
            inflected = parse.inflect({"gent"})

            res.append(inflected.word.capitalize() if inflected else word)

    return " ".join(res)


print(manager_name_gent("Харченко Дмитрий Владимирович"))
