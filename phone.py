class Phone:
    def __init__(self, number):
        self.number = number
        
    def turn_on(self):
        return f"mobile phone {self.number} is turned on"
        
    def turn_off(self):
        return f"mobile phone is turned off"
        
    def call(self):
        return f"calling {self.number}"
        
phone1 = Phone('786898878')
phone2 = Phone('511053789')

print(phone1.turn_on())
print(phone1.turn_off())
print(phone1.call())

