from DividendClass.Dividend import Dividend

dividend = Dividend()
dividend.TotalSavings = 107839
dividend.Name = ["Peter", "Paul"]
dividend.Interest = 400000
dividend.IndividualSavings = [65000, 42839]

share = dividend.getShare(sf=0)
print(share)
dividend.getName()
