class Solution:
    def fractionAddition(self, expression: str) -> str:
        num,den=zip(*((int(i.group('num')),int(i.group('den'))) for i in re.finditer('(?P<num>[+-]{0,1}\d+)/(?P<den>\d+)',expression)))
        lcm=functools.reduce(operator.mul,set(den))//math.gcd(*den,1)
        NUM=0
        for i in range(len(num)):
            NUM+=num[i]*(lcm//den[i])
        
        GCD=math.gcd(NUM,lcm)
        return f'{NUM//GCD}/{lcm//GCD}'

        