class Xbox:
  def __init__(self, color, size, disk): # Giving the xbox different attributes
    self.color = color
    self.size = size
    self.disk = disk

  def __str__(self):
    return f"Your Xbox is {self.color}, the size is {self.size}, and is there a disk drive? {self.disk}"

  def turnOn(self):
    return "Your xbox is turning on..."

  def turnOff(self):
    return "Your xbox is turning off..."

class XboxController:
  def __init__(self, color): # Giving the xbox controller different attributes
    self.color = color

  def __str__(self):
    return f"You have a {self.color} Xbox controller"

  def turnOn(self):
    return "Your xbox controller is turning on..."

  def turnOff(self):
    return "Your controller is turning off..."


# Printing out the different Methods and Objects
xboxSeriesS = Xbox("white", "small", "no")
xboxController1 = XboxController("white")
print(xboxSeriesS)
print(xboxSeriesS.turnOn())
print(xboxController1)
print(xboxController1.turnOn())
print(xboxSeriesS.turnOff())
print(xboxController1.turnOff())

print("----------------------------------------------------------------------")

xboxSeriesX = Xbox("black", "huge", "yes")
xboxController2 = XboxController("blue")
print(xboxSeriesX)
print(xboxSeriesX.turnOn())
print(xboxController2)
print(xboxController2.turnOn())
print(xboxSeriesX.turnOff())
print(xboxController2.turnOff())
