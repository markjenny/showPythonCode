# -*- coding = utf-8 -*-
#本题是为了生成200个验证码，长度默认为8
'a test module'

__author__ = 'Mark'

import random

def gengerate_code(number=200, length=8):
    char_set = "abcdefghijklmnopqrstuvwxyz0123456789"
    result = ""
    for i in range(number):
        temp = ""
        while(temp == ""):
            for j in range(length):
                temp = temp + char_set[random.randint(0,35)]
            #judge if the code is similiar with the previous
            if(result.find(temp) == -1):
                result = result + "%d" % (i+1) + temp
            else:
                temp = ""
        result = result + "\n";
    return result

def file_write():
    try:
        fs = open("result.txt", "w")
        fs.writelines(gengerate_code())
    finally:
        fs.close()


if __name__ == "__main__":
    file_write()
