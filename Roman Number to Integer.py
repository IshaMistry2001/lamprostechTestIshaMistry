class Main():
   def romanToInteger(self, s):     
      #defining dictionary containing all values
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      num = 0
      while i < len(s):
          #checking for 2 char values in dict
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]] #if value is found in dict adding to num 
            i+=2
         else:
            num+=roman[s[i]] #check for 1 char value
            i+=1
      return num
ob1 = Main()
print(ob1.romanToInteger("III"))
print(ob1.romanToInteger("LVIII"))
print(ob1.romanToInteger("MCMXCIV"))