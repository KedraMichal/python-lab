from lab5.shape_classes import *


class Paint:
    possible_actions = ["set_background_color", "set_border_color", "rotate", "move", "scale"]
    figures = {"triangle": Triangle, "rectangle": Rectangle, "square": Square, "circle": Circle}

    def __init__(self):
        self.names = {}

    def add(self, figure, name, *size):
        if figure in Paint.figures.keys():
            if name not in self.names.keys():
                try:
                    self.names[name] = Paint.figures[figure](name, *size)
                except: # nie piszemy except bez typu
                    print("Wrong size!")
            else:
                print("Name already taken")
        else:
                print("Unknown figure type")

    def remove(self, name):
        if name in self.names.keys():
            del self.names[name]
        else:
            print("Unknown name")

    def command_line(self): # warto tę funkcję zdekomponować
        while True:
            command = input("Enter a command: ")
            command = command.lower()

            if command == "quit":
                for figure in self.names.values():
                    print(figure)
                break

            command = command.split()
            if len(command) >= 4 and command[0] == "add":
                self.add(command[1], command[2], *command[3:])
            elif len(command) == 4 and command[0] == "move":
                if command[1] in self.names.keys():
                    try:
                        self.names[command[1]].move(float(command[2]), float(command[3]))
                    except:
                        print("Vector cant be a string")
                else:
                    print("Unknown name")
            elif len(command) == 3 and command[0] in Paint.possible_actions:
                if command[1] in self.names.keys():
                    if command[0] == "set_border_color":
                        self.names[command[1]].set_border_color(command[2])
                    elif command[0] == "set_background_color":
                        self.names[command[1]].set_background_color(command[2])
                    elif command[0] == "scale":
                        try:
                            self.names[command[1]].scale(float(command[2]))
                        except:
                            print("Ratio must be a float")
                    elif command[0] == "rotate":
                        try:
                            self.names[command[1]].rotate(float(command[2]))
                        except:
                            print("Angle must be a float")

                else:
                    print("Unknown name")

            elif len(command) == 2 and command[0] == "remove":
                self.remove(command[1])

            elif len(command) == 1 and command[0] == "help":
                print("""Polecenia:
                    add <figure> <name> <size>
                    remove <name>
                    move <name> <vector>
                    scale <name> <ratio>
                    rotate <name> <angle>
                    set_border_color <name> <color>
                    set_background_color <name> <color>
                    help
                    quit


                <figure> to jedno z: circle, square, rectangle, triangle
                <name> - dowolny unikatowy identyfikator mogący zawierać litery, cyfry i podkreślniki, nie zaczynający się od cyfry
                <ratio> - dowolna liczba rzeczywista, różna od 0
                <angle> - dowolny kąt w stopniach
                <color> to jedno z: black, white, red, green, blue, cyan, magenta, yellow
                Każda figura po dodaniu ma środek w punkcie (0, 0).""")

            else:
                print("Unknown command")


if __name__ == "__main__":
    c1 = Paint()
    c1.command_line()
# da się stworzyć prostokąt z ujemnym bokiem
