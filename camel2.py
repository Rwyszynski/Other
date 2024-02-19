def solution(s):
    newList = ""
    for i in s:
        if i.isupper():
            newList += " "
        newList += i
    return newList





print(solution("breakCamelCase"))
