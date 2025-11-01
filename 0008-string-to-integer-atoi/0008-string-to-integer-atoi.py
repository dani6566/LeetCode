class Solution:
    def myAtoi(self, s):
        k = s.strip()
        if k == "":
            return 0

        sign = 1
        if k[0] == "-":
            sign = -1
            k = k[1:]
        elif k[0] == "+": 
            k = k[1:]

        k = k.lstrip("0")  

        data =[k]
        rstr = ""
        for i in data:
            for j in i:
                if j.isdigit():
                    rstr += j
                else:
                    break
            break 

        if rstr == "":      
            return 0
            
        if (int(rstr) * sign) >= 2147483648:
            return 2147483647
        elif (int(rstr) * sign) <= -2147483648:
            return -2147483648

        return (int(rstr) * sign)