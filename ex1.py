################declare the class##############
class FruitBox:

################init function#################
    def __init__(self,apples,oranges):
        self.apples = apples
        self.oranges = oranges
 
    def __add__(self,m):
        return self.apples+m.apples+self.oranges+m.oranges

    def __str__(self):
        return self.apples,self.oranges


################create some objects###########

apples=FruitBox(40,0)
oranges=FruitBox(0,50)
################create some conditions###########

if apples.apples==str(apples.apples) or oranges.oranges==str(oranges.oranges):
    print("Error, you don't have only int charaters")
elif apples.apples==int(apples.apples) or oranges.oranges==int(oranges.oranges):
    total=apples+oranges
    print("Good")
    
    if total >50:
        print ("Your sum is out of the limit")
    else:
        print(total)
