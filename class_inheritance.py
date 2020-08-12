class Items:
    for_sale = "Yes"
    taxable = "Yes"

    def line(self):
        print(f'Country of origin of {self.brand} is {self.COO}')


class Beer(Items):
    minimum_alcohol_percentage = 5
    minimum_aging_period = 30

    def __init__(self, brand, company, kind, alcohol_percentage, coo):
        self.brand = brand
        self.company = company
        self. kind = kind
        self.alcohol_percentage = alcohol_percentage
        self.COO = coo

    def company_motto(self):
        print(f'{self.brand} is a good beer!')


shiner = Beer("Shiner Bock", "Shiner Brewery", "Dark Ale", 6, "USA")
sierra = Beer("Sierra Nevada", "Colorado Brewery", "IPA", 8, "Mexico")

sierra.line()
print(shiner.for_sale)


