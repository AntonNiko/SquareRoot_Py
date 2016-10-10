
class SquareRoot:
    __slots__ = "value","result"
    def __init__(self,value):
        self.value = value
        self.result = 0

    def calculate(self):
        if self.value<0:
            raise ValueError("Value can only have real square roots")

        trialVal,difference = 0,1
        trialRes = 0
        upperHit,lowerHit = False,False

        while True:
            previousVal = trialRes
            trialRes = trialVal**2
            if trialRes > self.value:
                trialVal-=difference
                upperHit = True
            elif trialRes < self.value:
                trialVal+=difference
                lowerHit = True
            else:
                break
            print(trialRes)

            if previousVal==trialRes and trialVal!=1:
                break
            if upperHit and lowerHit:
                difference/=2
                upperHit,lowerHit = False,False

        self.result = trialVal
        
    def getSquareRoot(self):
        return self.result

def main():
    sq = SquareRoot(float(input("Value: ")))
    sq.calculate()
    return sq.getSquareRoot()

if __name__ == "__main__":
    print(main())
