def oxford_comma(items):
    if not items:
        text = ""
    elif len(items) == 1:
        text = items[0]
    elif len(items) == 2:
        text = " and ".join(items)
    else:
        text = ", ".join(items[:-1]) + ", and " + items[-1]
    return text
