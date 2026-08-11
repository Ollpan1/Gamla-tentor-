def base3(n): ##Exercise A1
    if n < 3:
        return ''
    elif n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return  base3(n//3) +  str(n%3) 
def divisible9(x): ##Exercise A2
    def digit_sum(x):
        """ Computes and returns the sum of the digits
        """
        if x < 10:
            return x
        else:
            result  = 0
            y = str(x)
            for i in y:
                result += int(i)
            return result

    if x == 9 or x == 0:
        return True
    elif x> 9:
        return divisible9(digit_sum(x))
    else:
        return False

class TowerHanoi: ##Exercise B1
    def bricklek(self):
        def _bricklek(k, start=0, goal=2, help=1):
            if k == 0:
                return []
            else:
                return _bricklek(k-1, start, help, goal) +\
                [(start, goal)] +\
                _bricklek(k-1,help, goal, start)
        return _bricklek(self.n)
    def __init__(self,n):
        self.n = n
        self.ListofList = [list(range(n)),[],[]]
        self._time = 0
        self.instructions = self.bricklek()

    def step(self):
        current = self.instructions[self._time]
        out = current[0]
        In = current[1]
        element = self.ListofList[out][0]
        self.ListofList[out] = self.ListofList[out][1:]
        self.ListofList[In].insert(0, element)
        self._time += 1
        
    def __str__(self):
        stacks = ['start', 'help', 'goal']
        repr = "Step" + str(self._time)+"\n"
        for s,l in zip(stacks, self.ListofList):
           repr += s + ":"+"\n"
           for n in l:
               repr += "*"*(n+1)+"\n"
        return repr
                  

def main():
    print("Test A1:")
    for x in [3,6,20,27,28,52]:
        print(base3(x), end=" ")
    print("")
    print("Test A2:")
    for x in [9,18,9000, 25689, 24606]:
        print(divisible9(x))
    print("")
    print("Test B1:")
    TH = TowerHanoi(3)
    for _ in range(5):
        TH.step()
        print(TH)

if __name__ == '__main__':
    main()