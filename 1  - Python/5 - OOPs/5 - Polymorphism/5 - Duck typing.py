

# Duck Typing

# in Python we follow a principle
# " if its walk like a duck and talk like a duck it must be a duck"

# which means python does't care about which class of object it is ,if its an object and required
# behaviour is present for that object then itwill work.
# the type of object is distinguished only runtime .this is called duck typing .

# Example


class duck:
    def __init__(self):
        pass

    def walk(self):
        print("Thppak thappak")


class hores:
    def __init__(self):
        pass

    def walk(self):
        print("hores walking ")
class cat:
    def sound(self):
        print("Meaw meaw")


d = duck()
h = hores()
c = cat()

def main(obj):
    obj.walk()

main(d)
main(h)
























