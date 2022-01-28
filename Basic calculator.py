def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y
    
def dzielenie(x, y):
    return x / y
    
print("Jaką operacje chcesz wykonać?")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("")

dzialanie = input("Podaj numer operacji: ")

if dzialanie in ('1', '2', '3', '4'):

    x  = int(input("Podaj pierwszą liczbę: "))
    y = int(input("Podaj drugą liczbę: "))
    print("")
    
    if dzialanie == '1': 
        print(x, "+", y, "=", dodawanie(x, y))
        
    elif dzialanie == '2':
        print(x, "-", y, "=", odejmowanie(x,y))
        
    elif dzialanie == '3':
        print(x, "*", y, "=", mnozenie(x,y))
        
    elif dzialanie == '4':
        if x < y:
            print(x, "/", y, "=", dzielenie(x, y))
        elif x == 0:
            print("Nie można dzielić przez zero")
        elif y == 0:
            print("Nie można dzielić przez zero")
else:
    
    print("BŁĄD!!! Podaj poprawny operator działania.")



