class Solution:
    def reverse(self, x: int) -> int:
        a=0
        if x<=(2**31 - 1) and x>=-(2**31):
            if x>0:
                a=int(str(x)[::-1])
                if a<=(2**31 - 1) and a>=-(2**31):
                    return a
                else: 
                    return 0
            elif x<0:
                x=x*(-1)
                a=int(str(x)[::-1])*(-1)
                if a<=(2**31 - 1) and a>=-(2**31):
                    return a
                else:
                    return 0
        else:
            return 0
        return int(a)