def asterisk_triangle(n):
    string = ""
    for i in range(1, n + 1):
        if i == n:
            string += f"{(n - i) * ' ' + i * '*'}"
        else:
            string += f"{(n - i) * ' ' + i * '*'}\n"
    return string


print(asterisk_triangle(6))