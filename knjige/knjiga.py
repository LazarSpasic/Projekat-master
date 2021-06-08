from knjige.knjigeIO import ucitaj_knjige
from knjige.knjigeIO import sacuvaj_knjige
from knjige.racunIO import ucitaj_racun, sacuvaj_racun

knjige = ucitaj_knjige()


# knjige koje se iscitavaju direktno iz json fajla i predstavljene su pomocu tabele


def tabela_knjiga():
    print(
        'sifra    |naslov               |autor             |isbn          |izdavac     |godina   |cena     | kategorija')
    print(
        '---------|---------------------|------------------|--------------|------------|---------|---------|-----------')


def prikaz_knjiga(knjige):
    for knjiga in knjige:
        print(str(knjiga['sifra']).ljust(9) + '|' + knjiga['naslov'].ljust(21) + '|' + knjiga['autor'].ljust(18) + '|' +
              knjiga[
                  'isbn'].ljust(14) + '|' + knjiga['izdavac'].ljust(12) + '|' + str(knjiga['godina']).ljust(
            9) + '|' + str(knjiga['cena']).ljust(9) + '|' +
              knjiga['kategorija'].ljust(22))


# Pretrazivanje knjiga po sifri knjige
def pretraga_knjiga_po_sifri(sifra):
    # ucitavanje knjiga
    lista_knjiga = ucitaj_knjige()
    # prolazak kroz sve knjige iz json fajla pomocu for petlje
    for knjiga in lista_knjiga:
        # ako je uslov True, vraticec datu knjigu koja se poklapa sa sifrom
        if knjiga['sifra'] == sifra:
            return knjiga
    return None


# Pretrazivanje knjige po sifri akcije, logika je identicna kao u prethodnoj metodi
def pretraga_knjiga_po_sifriAkcije(lista_akcija, sifraAkcije):
    for akcija in lista_akcija:
        if akcija['sifra'] == sifraAkcije:
            return akcija
    return akcija


def pretraga_knjiga_string(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost.lower() in knjiga[kljuc].lower():
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretraga_knjiga_jednakost(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost == knjiga[kljuc]:
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige


def pretrazi_knjige():
    print("\n1. Pretraga po sifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po kategoriji")
    print("4. Pretraga po autoru")
    print("5. Pretraga po izdavacu")
    print("6. Pretraga po ceni")

    stavka = int(input("Izaberite stavku: "))
    if stavka == 1:
        sifra = int(input("Unesite sifru: "))
        knjige = pretraga_knjiga_jednakost("sifra", sifra)
        tabela_knjiga()
        prikaz_knjiga(knjige)
    elif stavka == 2:
        naslov = input("Unesite naslov: ")
        knjige = pretraga_knjiga_string("naslov", naslov)
        tabela_knjiga()
        prikaz_knjiga(knjige)
    elif stavka == 3:
        kategorija = input("Unesite kategoriju: ")
        knjige = pretraga_knjiga_string("kategorija", kategorija)
        tabela_knjiga()
        prikaz_knjiga(knjige)
    elif stavka == 4:
        autor = input("Unesite autora: ")
        knjige = pretraga_knjiga_string("autor", autor)
        tabela_knjiga()
        prikaz_knjiga(knjige)
    elif stavka == 5:
        izdavac = input("Unesite izdavaca: ")
        knjige = pretraga_knjiga_string("izdavac", izdavac)
        tabela_knjiga()
        prikaz_knjiga(knjige)
    elif stavka == 6:
        cena = float(input("Unesite cenu: "))
        knjige = pretraga_knjiga_jednakost("cena", cena)
        tabela_knjiga()
        prikaz_knjiga(knjige)


def sortiraj_knjige(kljuc):
    knjige = ucitaj_knjige()

    for i in range(len(knjige)):
        for j in range(len(knjige)):
            if knjige[i][kljuc] < knjige[j][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[j]
                knjige[j] = temp

    return knjige


def prikazi_knjige():
    print("\n1. Sortiraj po naslovu")
    print("2. Sortiraj po kategoriji")
    print("3. Sortiraj po autoru")
    print("4. Sortiraj po izdavacu")
    print("5. Sortiraj po ceni")

    stavka = int(input("Izaberite stavku: "))
    if stavka == 1:
        knjige = sortiraj_knjige("naslov")
        tabela_knjiga()
        prikaz_knjiga(knjige)
    elif stavka == 2:
        knjige = sortiraj_knjige("kategorija")
        tabela_knjiga()
        prikaz_knjiga(knjige)
    elif stavka == 3:
        knjige = sortiraj_knjige("autor")
        tabela_knjiga()
        prikaz_knjiga(knjige)
    elif stavka == 4:
        knjige = sortiraj_knjige("izdavac")
        tabela_knjiga()
        prikaz_knjiga(knjige)
    elif stavka == 5:
        knjige = sortiraj_knjige("cena")
        tabela_knjiga()
        prikaz_knjiga(knjige)


def prodaja_knjiga():
    korpa = []

    while True:
        print("\n1. Dodaj knjigu u korpu")
        print("\n2. Pregled korpe")
        print("3. Potvrdi kupovinu")
        print("4. Odustani od kupovine")

        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            sifra = int(input("sifra: "))
            knjiga = pretraga_knjiga_po_sifri(sifra)
            kolicina = int(input("kolicina: "))
            knjige = dodaj_u_korpu(knjiga, kolicina)
            korpa.append(knjige)
        elif stavka == 2:
            ukupna_cena = 0
            for k in korpa:
                ukupna_cena += k['cena'] * k['kolicina']
            tabela_knjiga()
            prikaz_knjiga(korpa)
            print("Kolicina: ", kolicina)
            print("Ukupna cena: ", ukupna_cena)
        elif stavka == 3:
            lista_korpe = sacuvaj_racun(korpa)
            print("Kupovina potvrdjena!")
            return lista_korpe
        elif stavka == 4:
            return


# Dodavanje kolicine koja se kupuje zajedno sa sifrom knjige
def dodaj_u_korpu(knjiga, kolicina):
    knjiga['kolicina'] = kolicina
    return knjiga


# Dodavanje nove knjige u fajl
def dodaj_knjigu(sifra, naslov, autor, isbn, izdavac, broj_strana, godina, cena, kategorija):
    knjiga = {'sifra': sifra, 'naslov': naslov, 'autor': autor, 'isbn': isbn, 'izdavac': izdavac,
              'broj_strana': broj_strana, 'godina': godina, 'cena': cena, 'kategorija': kategorija}
    return knjiga


# Metoda koja proverava da li knjiga vec postoji u fajlu
def da_li_postoji_sifra(lista_knjiga, sifra):
    for knjiga in lista_knjiga:
        if knjiga['sifra'] == sifra:
            return knjiga
    return False


# Registracija knjige u fajl(ako knjiga vec ne postoji)
def registracija_knjige(lista_knjiga, knjiga):
    if not da_li_postoji_sifra(lista_knjiga, knjiga['sifra']):
        lista_knjiga.append(knjiga)
        return True
    return False


# Izmena podataka postojece knjige
def izmeni_knjigu(knjiga, naslov, autor, isbn, izdavac, broj_strana, godina, cena, kategorija):
    knjiga['naslov'] = naslov
    knjiga['autor'] = autor
    knjiga['isbn'] = isbn
    knjiga['izdavac'] = izdavac
    knjiga['broj strana'] = broj_strana
    knjiga['godina'] = godina
    knjiga['cena'] = cena
    knjiga['kategorija'] = kategorija


# Brisanje knjige
def brisanje_knjiga(sifra):
    for knjiga in knjige:
        if knjiga['sifra'] == sifra:
            knjiga['obrisana'] = True
    sacuvaj_knjige(knjige)
