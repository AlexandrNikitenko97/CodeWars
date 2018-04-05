"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:

accum("abcd")    # "A-Bb-Ccc-Dddd"
accum("RqaEzty") # "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt")    # "C-Ww-Aaa-Tttt"

The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(s):
    result = []                             # initiate an empty array for results
    for i in range(len(s)):
        result.append((s[i]*(i+1)).title()) # multiply letter in given string on index + 1 and make it title
    return '-'.join(result)                 # join '-' between samples
