class IPhone:
    def __init__(self, model,price):
        self.model=model;
        self.price=price;
    def print(self): 
        print("\tModel : "+self.model);
        print("\tPrice : "+str(self.price));


        