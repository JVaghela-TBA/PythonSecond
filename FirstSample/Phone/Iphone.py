class IPhone:
    def __init__(self, model,price):
        self.model=model;
        self.price=price;
    def __del__(self):
            class_name=self.__class__.__name__;
            print("Destroyed Object : "+class_name);
    def print(self): 
        print("\tModel : "+self.model);
        print("\tPrice : "+str(self.price));


        