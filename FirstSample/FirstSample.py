import sys;
import Phone;

try:
    print("IPhone");
    phone5s=Phone.IPhone("IPhone 5S",21000)
    phone5s.print();
    phone6s=Phone.IPhone("IPhone 6S",42000)
    phone6s.print();

    print("-------------------------");
    print("Samsung");
    samsung=Phone.Samsung("Galaxy S",47000);
    samsung.print();

    #using attribute method of python
    #print(hasattr(samsung,"price"));
    #setattr(samsung,"price",50000);
    #print(getattr(samsung,"price"));
    #delattr(samsung,"price");
    #print(getattr(samsung,"price"));

    print("-------------------------");
except Exception as e:
    print("Exception Found"+str(e));
finally:
    del(phone5s);
    del(phone6s);
    del(samsung);
    print("All Variable Deleted");

