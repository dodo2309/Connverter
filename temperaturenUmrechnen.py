def get_temp():
    while True:
        C = input("Gib die Temperatur in Grad Celsius an: ")
        try:
            C = float(C)
            return C
        except ValueError:
            print("Keine gültige Zahl")

def connvert_temp(C):
    K = C + 273.15
    return K

if __name__ == "__main__":
    C = get_temp()
    print("Das sind " + str(connvert_temp(C)) + " Kelvin")