class Date:
    def __init__(self,day,month,year):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return f"{self.month}/{self.day}/{self.year}"
    
    def is_leap_year(self):
        if self.year % 4==0:
            if self.year % 100==0:
                return self.year % 400 ==0
            else:
                return True
        return False
    
    def validate_date(self):
        if not 1<=self.month<=12:
            return False
        if self.month in [1,3,5,7,8,10,12]:
            return 1<=self.day <= 31
        elif self.month in [4,6,9,11]:
            return 1<= self.day <= 30
        elif self.month == 2:
            if self.is_leap_year():
                return 1<=self.day <= 29
            else:
                return 1<=self.day <=28
        return False
        
date1 = Date(16,7,2023)
print(date1)
date2 = Date(29,2,2024)
print(date2)
date3 = Date(30,2,2023)
print(date3.validate_date())