# v.1.0 dzialajacej aplikacji

region = input("Podaj Region EUR / USA: ")
#sprawdzenie regionu:
if region.isdigit() == True:
    exit("Proszę podać region: EUR / USA ")
region=str(region)
if region==str("EUR"):
    print("Wybrano region: EUR")
elif region==str("USA"):
    print("Wybrano region: USA")
else:
    exit("Proszę podać poprawny region EUR / USA")
wiek = input("Podaj wiek uzytkownika: ")
#sprawdzenie czy wiek jest liczba całkowitą
if wiek.isdigit() == False:
    exit("wiek musi być liczbą całkowitą. Zamykam aplikację")
wiek=int(wiek)
if wiek>=18 and wiek<=40:
    print("Witamy w apce. Możesz u nas kupować alkohol")
elif wiek>40 and wiek<120:
    print("witamy w apce. Możesz u nas kupować alkohol")
    print("Proszę korzystaj z produktów z umiarem")
elif wiek>=120:
    print("Kup se trumna, a nie gorzoła czoeku")
else:
    exit("Jesteś za młody/a na alkohol. Zapraszamy na disney.com :)")
plec = input("Podaj swoją płeć: M/K ")
#sprawdzenie czy płeć jest literą:
if plec.isdigit() == True:
    exit("Proszę podać płeć: M / K ")
plec=str(plec)
if plec==str("M"):
    print("Wybrano płeć: M")
elif plec==str("K"):
    print("Wybrano płeć: K")
else:
    exit("Proszę podać poprawną formę: M / K")
    

if plec==str("K") and wiek>=30:
    print("Promocja! Odbierz gratis w postaci Aperol Spritz do swojego zamówienia!")