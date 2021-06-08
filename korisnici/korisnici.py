from korisnici.korisniciIO import ucitaj_korisnike
from knjige.racunIO import ucitaj_racun

# Tabela korisnika
def tabela_korisnika():
    print('korisnicko ime  |ime       |prezime     |tip korisnika')
    print('----------------|----------|------------|-------------')


# Prikaz korisnika
def prikaz_korisnika(lista_korisnika):
    for korisnik in lista_korisnika:
        print(korisnik['korisnicko_ime'].ljust(16) + '|' + korisnik['ime'].ljust(10) + '|' + korisnik['prezime'].ljust(12) + '|' + str(
            korisnik['tip_korisnika']))


def prijava():
    korisnici = ucitaj_korisnike()
    korisnicko_ime = input("korisnicko ime: ")
    lozinka = input("loznika: ")

    for korisnik in korisnici:
        if korisnik['korisnicko_ime'] == korisnicko_ime and korisnik['lozinka'] == lozinka:
            return korisnik
    return None


# Dodavanje novog korisnika
def dodaj_korisnika(korisnicko_ime, lozinka, ime, prezime, tip_korisnika):
    korisnik = {'korisnicko_ime': korisnicko_ime, 'lozinka': lozinka, 'ime': ime, 'prezime': prezime,
                "tip_korisnika": tip_korisnika}
    return korisnik


def da_li_postoji_korisnik(lista_korisnika, korisnicko_ime):
    for korisnik in lista_korisnika:
        if korisnicko_ime == korisnik['korisnicko_ime']:
            return korisnik
    return False


def registracija_korisnika(lista_korisnika, korisnik):
    if not da_li_postoji_korisnik(lista_korisnika, korisnik['korisnicko_ime']):
        lista_korisnika.append(korisnik)
        return True
    return False


# Sortiraj korisnike u tabeli
def sortiraj_korisnike(lista_korisnika):
    print("\n1. Sortiraj po imenu")
    print("2. Sortiraj po prezimenu")
    print("3. Sortiraj po tipu korisnika")

    stavka = int(input("Izaberi stavku: "))
    korisnici = []
    if stavka == 1:
        return sorted(lista_korisnika, key=lambda student: student['ime'])
    if stavka == 2:
        return sorted(lista_korisnika, key=lambda student: student['prezime'])
    if stavka == 3:
        return sorted(lista_korisnika, key=lambda student: student['tip_korisnika'])
    for korisnik in korisnici:
        print(korisnik)


def kreiraj_izvestaj():
    print("\n1. Ukupna prodaja knjiga")
    print("2. Ukupna prodaja akcija")
    print("3. Ukupna prodaja knjiga odredjenog autora")
    print("4. Ukupna prodaja knjiga odredjenog izdavaca")
    print("5. Ukupna prodaja knjiga odredjene kategorije")

    stavka = int(input("Izaberi stavku: "))
    if stavka == 1:
        racun = ucitaj_racun()
        duzina = len(racun)
        print("Ukupno prodatih knjiga: ", duzina)
    #elif stavka == 2:
    elif stavka == 3:
        racun = ucitaj_racun()
        autor = input("Unesite ime autora: ")
        for knjiga in racun:
            if knjiga['autor'] == autor:
                print(knjiga)
    elif stavka == 4:
        racun = ucitaj_racun()
        izdavac = input("Unesite izdavaca: ")
        for knjiga in racun:
            if knjiga['izdavac'] == izdavac:
                print(knjiga)
    elif stavka == 5:
        racun = ucitaj_racun()
        kategorija = input("Unesite kategoriju: ")
        for knjiga in racun:
            if knjiga['kategorija'] == kategorija:
                print(knjiga)
