def set_einheit():
    while True:

        E = input("Welche Einheit möchtest du umrechnen?:\n[1:°Celsius->°Kelvin]\n[2:°Kelvin->°Celsius]\n")
        return E


def get_temp(E):
    while True:
        if E == "1":
            while True:
                C = input("Gib die Temperatur in Grad Celsius an: ")
                try:
                    C = float(C)
                    return C
                except ValueError:
                    print("Keine gültige Zahl")
        elif E == "2":
            while True:
                C = input("Gib die Temperatur in Grad Kelvin an: ")
                try:
                    C = float(C)
                    return C
                except ValueError:
                    print("Keine gültige Zahl")
        else:
            print("Nicht möglich")
            break



def connvert_tempC(C):
    K = C + 273.15
    return K

def connvert_tempK(C):
    K = C - 273.15
    return K

if __name__ == "__main__":
    while True:
        E = set_einheit()
        C = get_temp(E)
        if E == "1":
            print("Das sind " + str(connvert_tempC(C)) + " Grad Kelvin")

        if E == "2":
            print("Das sind " + str(connvert_tempK(C)) + " Grad Kelvin")