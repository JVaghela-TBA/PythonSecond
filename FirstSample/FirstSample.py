import sys;
import Phone;

try:
    Phone.iphone();
    Phone.samsung();
except:
    print("Exception Found");
else:
    print("Finally Block Execute");