#Can you make your sum function work for a list of strings as well.

#>>> sum(["hello", "world"])
"helloworld"
#>>> sum(["aa", "bb", "cc"])
#"aabbcc"


def sum(list):
    str = "";
    for i in list[:]:
        str += i;

    return str;

print(sum(["hello", "world", "py"]))
