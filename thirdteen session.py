# object-oriented programing
# class has def named __init__
# self mean to connect to attribute(name address)
class Game:
    has_license = True
    def __init__(self, name , console_type , game_type , characters , voice_actors , category):

        self.name = name
        self.address = console_type
        self.city = game_type
        self.phone_number = characters
        self.voice_actors = voice_actors
        self.category = category
    # function in function is method
    def __str__(self):
        return f"{self.name} - {self.address} - {self.city} - {self.phone_number} - {self.category}"
    # custom method
    def pre_order(self,game_name, console_brand):
        return f"{game_name} in {console_brand} pre-ordered"

game_1 = Game("nfs","pc/ps4",
            "open world","cars","exhust","sport")


game_2 = Game("spiderman","sony entertainment",
            "open world","spider-man & villan","andrew garfield","action")

print(game_1)
print(game_2)

print(game_1.has_license)