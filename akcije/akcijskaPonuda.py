import akcije
from akcije.akcijskaPonudaIO import ucitaj_akcije, sacuvaj_akcije
from knjige.knjiga import ucitaj_knjige
from datetime import date

akcije = ucitaj_akcije()
n = len(akcije)
knjige = ucitaj_knjige()
kljuc = ['sifra', 'naslov', 'autor', 'isbn', 'izdavac', 'godina', 'cena', 'kategorija', 'broj strana']


# Funkcija za prikazivanje akcija u tabelarnoj formi
def tabela_akcija(akcije, prikazi):
    # Zaglavlje koje ce biti vidljivo kao tabela
    zaglavlje = f"{'Sifra Akcije': <15}" \
                f"{'Naslov': <25}" \
                f"{'Autor': <20}" \
                f"{'Kategorija': <25}" \
                f"{'Datum': <10}"
    #Pritovanje zaglavlja
    print(zaglavlje)
    #Pritovanje - simbola u duzini zaglavlja
    print("-" * len(zaglavlje))
    #Pomocu for petlje prolazimo kroz akcije koje se nalaze u fajlu
    for i in range(0, len(akcije)):
        #Uslov za datum
        if akcije[i]["datum"] > str(date.today()) or prikazi == False:
            #Ugnjezdena for petlja koja ce prolaziti kroz knjige
            for j in range(0, len(akcije[i]['knjige'])):
                kreiraj = f"{akcije[i]['sifra']:<15}" \
                          f"{akcije[i]['knjige'][j]['naslov']:<25}" \
                          f"{akcije[i]['knjige'][j]['autor']:<19}" \
                          f"{akcije[i]['knjige'][j]['kategorija']:<20}" \
                          f"{akcije[i]['datum']:^20}"

                print(kreiraj)


# Funkcija za sortiranje akcija po jednakosti(sifri)
def pretraga_akcija_jednakost(kljuc, vrednost):
    filtriranje_akcije = []

    for akcija in akcije:
        if vrednost == akcija[kljuc]:
            filtriranje_akcije.append(akcija)

    return filtriranje_akcije


# Funkcija za sortiranje akcija po stringu(naslov, autor, kategorija)
def pretraga_akcija_string(kljuc, vrednost):
    filtrirane_akcije = []

    if kljuc == 'sifra':
        for akcija in akcije:
            if vrednost.lower() in akcija[kljuc].lower():
                filtrirane_akcije.append(akcija)
    else:
        for akcija in akcije:
            for a in akcija['knjige']:
                if a[kljuc].lower() == vrednost.lower():
                    filtrirane_akcije.append(akcija)
    return filtrirane_akcije


# Funkcija za pretrazivanje akcije po odredjenom parametru
def pretrazi_akcije():
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po kategoriji")
    print("4. Pretraga po autoru")

    stavka = int(input("Izaberite stavku: "))

    akcije = []
    if stavka == 1:
        sifra = int(input("Unesite sifru akcije: "))
        akcije = pretraga_akcija_jednakost("sifra", sifra)
    elif stavka == 2:
        naslov = input("Unesite naslov: ")
        akcije = pretraga_akcija_string("naslov", naslov)
    elif stavka == 3:
        kategorija = input("Unesite kategoriju: ")
        akcije = pretraga_akcija_string("kategorija", kategorija)
    elif stavka == 4:
        autor = input("Unesite autora: ")
        akcije = pretraga_akcija_string("autor", autor)
    tabela_akcija(akcije, prikazi=False)


# Sortiranje akcija, implementacija je ista kao i u funkciji sortiraj_knjige(kljuc)
def sortiraj_akcije(kljuc):
    for i in range(len(akcije)):
        for j in range(len(akcije)):
            if akcije[i][kljuc] < akcije[j][kljuc]:
                temp = akcije[i]
                akcije[i] = akcije[j]
                akcije[j] = temp

    return akcije


# Prikazivanje akcija po odredjenom parametru u vidu tabele
def prikazi_akcije():
    print("\n1. Sortiraj po sifri")
    print("2. Soritraj po datumu")

    stavka = int(input("Izaberite stavku: "))
    if stavka == 1:
        sortiraj_akcije('sifra')
    elif stavka == 2:
        sortiraj_akcije("datum")
    tabela_akcija(akcije, prikazi=False)


# Dodavanje nove akcije sa svim podacima
def dodaj_akciju():
    nova_akcija = {"sifra": 1,
                   "knjige": [],
                   "datum": "01.01.1111",
                   }
    sifra = akcije[-1]['sifra']
    nova_akcija['sifra'] = sifra + 1

    sifra = int(input("Unesite sifru:"))

    for knjiga in knjige:
        if knjiga['sifra'] == sifra:
            nova_cena = float(input("\nUnesite novu cenu: "))
            knjiga['nova cena'] = nova_cena
            nova_akcija['knjige'].append(knjiga)
    datum = input("Unesite datum do kada vazi akcija")
    nova_akcija['datum'] = datum
    akcije.append(nova_akcija)

    if len(nova_akcija['knjige']) > 0:
        sacuvaj_akcije(akcije)
        print('Nova akcijska ponuda je dodata!')