
import requests
import json
import pprint
################declare the class##############

class Money:

################init function#################

    def __init__(self,value,currency):
        self.value=value
        self.currency=currency
    
    def __str__(self):
        return "["+str(self.value)+self.currency+"]"

    def __sub__(self,m):
        #HW1: check the currency
        return Money(self.value - m.value, self.currency)

    def __add__(self,m):
        #HW1: check the currency
        return Money(self.value+m.value, self.currency)
    
    # NU PREA AM STIUT CUM SA FOLOSESC METODA RESPCTIVA 
    
    # def __floordiv__(self,m):
    #     return Money(self.value//m.value)
    
    def __eq__(self,m):
        return self.currency==m.currency
       

        


################create some objects###########

jun_salary  =Money(1000,"EUR")
travel_cost =Money(int(input("How much jun's travel costs?")),str(input("what's the travel cost currency?")))
jun_bonus   =Money(150,"EUR")




if jun_salary==travel_cost:
    print("The same currency")
    rest        =jun_salary+jun_bonus-travel_cost
    print("Jun salary is:",jun_salary)
    print("The travel cost:",travel_cost)
    print("Jun's remaining rest is:",rest)

else:
    pp=pprint.PrettyPrinter(indent=2, width=10)

    API_key="6fa58852246440c5b7b635f8cdbd8f86"
    currency=travel_cost.currency
    

    res=requests.get("http://data.fixer.io/api/latest?access_key="+API_key+"&symbols=",currency)
    data=json.loads(res.text)
    data1=data['rates'][str(currency)]

    cost=float(travel_cost.value)/data1
    
    
    print ("There is difference between currencies")
    print ("1 EUR=",data1,travel_cost.currency)
    print("The travel cost:",cost/data1,"EUR")

    rest        =jun_salary.value+jun_bonus.value-cost
    print ("Jun's remaining rest is:",rest,"EUR")

    









