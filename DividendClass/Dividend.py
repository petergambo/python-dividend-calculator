class Dividend:
    def __init__(self, TotalSavings="", IndividualSavings="", Interest="", Name=""):
        self.TotalSavings = TotalSavings
        self.IndividualSavings = IndividualSavings
        self.Interest = Interest
        self.Name = Name

    def getShare(self, sf=""):
        if self.IndividualSavings =="" or self.TotalSavings == "":
            print("One or more Parameters Not Set. Kindly Set TotalSavings, IndividualSavings and Interest")
        else:
            for item in self.IndividualSavings:
                factor = item / self.TotalSavings
                dividend = self.Interest * factor

                if sf == "":
                    dividend = round(dividend)
                elif sf == 2:
                    dividend = round(dividend, 2)
                elif sf == 4:
                    dividend = round(dividend, 4) 
                else:
                    dividend = round(dividend) 

                return f"Dividend is: {dividend}"
            
    def getName(self):
        if self.Name == "":
            print("Oops! Name Parameter has not been sent!")
        else:
            for name in self.Name:
                print(name)