'''This is the Product assignment,
by: Troy Center, troycenter1@gmail.com, Coding Dojo Python fundamentals, June 2017
'''

#pylint: disable=C0103

class Product(object):
    ''' This is the class for the Product assignment
    '''
    def __init__(self, price, name, weight, brand, cost, status="for sale"):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = status

    def sell(self):
        '''This function will set all items to "sold" status
        '''
        self.status = 'sold'
        return self

    def addTax(self, tax):
        '''This function will take a tax amount in as a param
           and return the price of the item including sales tax
        '''
        priceaftertax = format(self.price * ((tax*.01)+1), '.2f')
        print "Price after tax is", priceaftertax

    def returnitem(self, returnreason, openbox):
        '''This function takes reason for return as a parameter
           and changes status accordingly. If the item is being
           returned because its defective, change status to defective
           and change price to 0. If its being returned in its box
           mark it for sale, if the box has been opened mark it used
           and apply a 20% discount.
        '''
        # return reason
        #   defective = prioce 0 and status defective
        if returnreason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        if openbox is False:
            self.status = "for sale"
            return self
        elif openbox is True:
            self.status = "used"
            self.price = self.price * .8 # 20% discount
            return self
        #   likenew = mark for sale
        #   openbox = 20% discount and status used

    def displayInfo(self):
        '''This fucntion shows all the product details.
        '''
        print "====================================="
        print "== Price info for ", self.name, " =="
        print "====================================="
        print "Price: $", format(self.price, '.2f')
        print "Product: ", self.name
        print "Weight: ", self.weight
        print "Brand: ", self.brand
        print "Cost: $", format(self.cost, '.2f')
        print "Status: ", self.status
        return self

laptop = Product(2199.99, "EliteBook", "6lbs", "HP", 1400.00)
laptop.displayInfo()
laptop2 = Product(3199.99, "GameBook G4", "10lbs", "HP", 2400.00)
laptop2.displayInfo()
laptop3 = Product(499.99, "StudentModel", "5lbs", "Dell", 310.00)
laptop3.displayInfo()
dockingstation = Product(199.99, "EliteDock", "2lbs", "HP", 149.00)
dockingstation.displayInfo()
speaker = Product(199.99, "ProAudio5.1", "8lbs", "Klipsch", 159.00)
speaker.displayInfo()
monitor = Product(299.99, "HR24", "4lbs", "Dell", 210.00)
monitor.displayInfo()
cpu = Product(199.99, "i7-4400", "0lbs", "Intel", 180.00)
cpu.displayInfo()
memory = Product(39.99, "16GB DDR3", "0lbs", "Crucial", 19.00)
memory.displayInfo()
powersupply = Product(49.99, "Power420", "3lbs", "Corsair", 21.00)
powersupply.displayInfo()
vgacable = Product(19.99, "VGA Cable", "1lbs", "C2G", 10.00)
vgacable.displayInfo()
printercable = Product(19.99, "USB Printer Cable", "1lbs", "C2G", 10.00)
printercable.displayInfo()
powercable = Product(19.99, "Power Cable", "1lbs", "C2G", 10.00)
powercable.displayInfo()
smhdd = Product(199.99, "HDD120GB5400", "2lbs", "Seagate", 140.00)
smhdd.displayInfo()
lghdd = Product(299.99, "HDD240GB7200", "2lbs", "Seagate", 190.00)
lghdd.displayInfo()

laptop.sell()
laptop.displayInfo()

laptop.returnitem("didnt want", False)
laptop.displayInfo()

laptop2.returnitem("didnt like", True)
laptop2.displayInfo()

laptop3.returnitem("defective", False)
laptop3.displayInfo()

laptop2.addTax(.10)
