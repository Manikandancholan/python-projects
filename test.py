def expand_string(s):
    result = ""
    i = 0
    
    while i < len(s):
        char = s[i]
        i += 1
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            print("num --- ", num)
            i += 1
            print("i --- ", i)
        
        result += char * int(num)
    
    return result

input = input("Enter an input: ")
output = expand_string(input)
print(output)
