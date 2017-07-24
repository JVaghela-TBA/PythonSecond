import sys;
import logging;
import Phone;

#logging message in python
logger=logging.getLogger("Logger");
logger.setLevel(logging.DEBUG);

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

    no=10/0
    #Print Class Variables
    #print("Samsung.__doc__ :"+str(Phone.Samsung.__doc__));
    #print("Samsung.__name__ :"+str(Phone.Samsung.__name__));
    #print("Samsung.__module__ :"+str(Phone.Samsung.__module__));
    #print("Samsung.__bases__ :"+str(Phone.Samsung.__bases__));
    #print("Samsung.__dict__ :"+str(Phone.Samsung.__dict__));

    #using attribute method of python
    #print(hasattr(samsung,"price"));
    #setattr(samsung,"price",50000);
    #print(getattr(samsung,"price"));
    #delattr(samsung,"price");
    #print(getattr(samsung,"price"));

    print("-------------------------");
except Exception as e:
    #implement logger
    logger.error("Exception Found "+str(e));
    print("Exception Found"+str(e));
finally:
    
    del(phone5s);
    del(phone6s);
    del(samsung);
    print("All Variable Deleted");

