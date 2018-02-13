class Skateboard:
  name = ""
  brand = ""
  trucks = ""
  wheels = ""
  griptape = ""

  def announcer(self):
    announcer_template = "%s is riding a %s board with %s trucks, %s wheels, and %s griptape! Wish them luck!" % (self.name, self.brand, self.trucks, self.wheels, self.griptape)
    return announcer_template

# First skater
skater1 = Skateboard()
skater1.name = "Jerry"
skater1.brand = "Blind"
skater1.trucks = "Krux"
skater1.wheels = "Spitfire"
skater1.griptape = "Black Magic"

# Input any other skater

print(skater1.announcer())
