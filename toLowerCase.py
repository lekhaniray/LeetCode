class Solution:
    str = "HelloLoser"
    def toLowerCase(str):
        result = ''
        for char in str:
            if(ord(char) >= 65 and ord(char)<=90):
                result += chr(ord(char) + 32)

            else:
                result += char
        return result

    ret = toLowerCase(str)
    print(ret)
