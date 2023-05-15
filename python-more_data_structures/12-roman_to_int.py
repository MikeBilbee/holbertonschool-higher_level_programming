#!/usr/bin/python3
def roman_to_int(roman_string):
    a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    iv = 0
    r = roman_string
    if type(r) != str or r is None:
        return 0
    for i in range(len(r)):
        if i > 0 and a[r[i]] > a[r[i-1]]:
            iV += a[r[i]] - \
                2 * a[r[i-1]]
        else:
            iv += a[r[i]]
    return iv
