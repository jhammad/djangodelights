class Car(object):
#blueprint for car
    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model
        def start():
            x = self.speed_limit
            print("started")
        def stop():
            print("stopped")
        def accelarate():
            print("accelarating...")
    #accelerator functionality here"
        def change_gear(gear_type):
            print("gear changed")
#gear related functionality here"
#Now that we have created the objects, let’s move on to create the individual cars in the game.
maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)
print(maruthi_suzuki.speed_limit * 2)