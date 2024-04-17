class Card:
    def __init__(self,id,imageUrl,deviceType,price,rating):
        self.id=id
        self.imageUrl=imageUrl
        self.deviceType=deviceType
        self.price=price
        self.rating=rating
    
    def printall(self):
        print("Product -",self.id)
        print("imageUrl:",self.imageUrl)
        print("deviceType:",self.deviceType)
        print("price:",self.price)
        print("rating:",self.rating)
        print( )

Product1=Card("1 :","Dummy-url 1","Mobile",56000,4.5)
Product1.printall()
product2=Card("2 :","Dummy-url 2","Laptop",94000,4.8)
product2.printall()
product3=Card("3 :","Dummy-url 3","Smart-watch",18000,3.5)
product3.printall()
