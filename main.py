from knjige.knjiga import prikazi_knjige, pretrazi_knjige, prodaja_knjiga, dodaj_knjigu, registracija_knjige, pretraga_knjiga_po_sifri, izmeni_knjigu, brisanje_knjiga, pretraga_knjiga_jednakost
from akcije.akcijskaPonuda import prikazi_akcije
from akcije.akcijskaPonuda import pretrazi_akcije
import korisnici.korisniciIO
from knjige.knjigeIO import ucitaj_knjige, sacuvaj_knjige
from knjige.knjiga import izmeni_knjigu
from knjige.knjiga import brisanje_knjiga
from korisnici.korisniciIO import ucitaj_korisnike, sacuvaj_korisnike
from korisnici.korisnici import prijava, sortiraj_korisnike, dodaj_korisnika, registracija_korisnika, tabela_korisnika, \
    prikaz_korisnika, kreiraj_izvestaj
from akcije.akcijskaPonuda import dodaj_akciju


# Uloguj se kao administrator
def meni_administrator():
    while True:
        print("\n1. Prikaz knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Registracija")
        print("6. Prikaz svih korisnika")
        print("7. Dodaj knjigu")
        print("8. Izmeni knjigu")
        print("9. Obrisi knjigu")
        print("10. Kraj")
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            prikazi_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            korisnicko_ime = input('korisnicko ime >> ')
            lozinka = input('lozinka >> ')
            ime = input('ime >> ')
            prezime = input('prezime >> ')
            tip_korisnika = input('tip korisnika >> ')
            korisnik = korisnici.korisnici.dodaj_korisnika(korisnicko_ime, lozinka, ime, prezime, tip_korisnika)
            lista_korisnika = korisnici.korisniciIO.ucitaj_korisnike()
            uspesno = korisnici.korisnici.registracija_korisnika(lista_korisnika, korisnik)
            if uspesno:
                korisnici.korisniciIO.sacuvaj_korisnike(lista_korisnika)
            else:
                print("Vec postoji korisnik sa tim korisnickim imenom")
        elif stavka == 6:
            lista_korisnika = ucitaj_korisnike()
            lista_korisnika = sortiraj_korisnike(lista_korisnika)
            tabela_korisnika()
            prikaz_korisnika(lista_korisnika)
        elif stavka == 7:
            sifra = int(input('sifra: '))
            naslov = input('naslov: ')
            autor = input('autor: ')
            isbn = input('isbn: ')
            izdavac = input('izdavac: ')
            broj_strana = int(input('broj strana: '))
            godina = int(input('godina: '))
            cena = int(input('cena: '))
            kategorija = input('kategorija: ')
            knjiga = dodaj_knjigu(sifra, naslov, autor, isbn, izdavac, broj_strana, godina, cena, kategorija)
            lista_knjiga = ucitaj_knjige()
            uspesno = registracija_knjige(lista_knjiga, knjiga)
            if uspesno:
                sacuvaj_knjige(lista_knjiga)
                print("Nova knjiga je dodata!")
            else:
                print("Vec postoji knjiga sa tom sifrom")
        elif stavka == 8:
            sifra = int(input('sifra: '))
            knjiga = pretraga_knjiga_po_sifri(sifra)
            if knjiga is None:
                print("Ne postoji knjiga sa sifrom: ", sifra)
            else:
                print(knjiga)
                knjiga['naslov'] = input('naslov: ')
                knjiga['autor'] = input('autor: ')
                knjiga['isbn'] = input('isbn: ')
                knjiga['izdavac'] = input('izdavac: ')
                knjiga['broj_strana'] = int(input('broj strana: '))
                knjiga['godina'] = int(input('godina: '))
                knjiga['cena'] = float(input('cena: '))
                knjiga['kategorija'] = input('kategorija: ')
                sacuvaj_knjige(knjiga)
        elif stavka == 9:
            sifra = int(input("Unesite sifru knjige: "))
            brisanje_knjiga(sifra)
            print("Knjiga je obrisana!")
        elif stavka == 10:
            return
        else:
            print("Pokusajte ponovo!")


# Uloguj se kao menadzer
def meni_menadzer():
    while True:
        print("\n1. Prikaz knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Registracija")
        print("6. Prikaz svih korisnika")
        print("7. Dodavanje akcijske ponude")
        print("8. Kreiranje izvestaja")
        print("10. Kraj")
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            prikazi_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            korisnicko_ime = input('korisnicko ime: ')
            lozinka = input('lozinka: ')
            ime = input('ime: ')
            prezime = input('prezime: ')
            tip_korisnika = input('tip korisnika: ')
            korisnik = dodaj_korisnika(korisnicko_ime, lozinka, ime, prezime, tip_korisnika)
            lista_korisnika = ucitaj_korisnike()
            uspesno = registracija_korisnika(lista_korisnika, korisnik)
            if uspesno:
                sacuvaj_korisnike(lista_korisnika)
            else:
                print("Vec postoji korisnik sa tim korisnickim imenom")
        elif stavka == 6:
            lista_korisnika = ucitaj_korisnike()
            lista_korisnika = sortiraj_korisnike(lista_korisnika)
            tabela_korisnika()
            prikaz_korisnika(lista_korisnika)
        elif stavka == 7:
            dodaj_akciju()
        elif stavka == 8:
            kreiraj_izvestaj()
        elif stavka == 10:
            return
        else:
            print("Pokusajte ponovo!")


# Uloguj se kao prodavac
def meni_prodavac():
    while True:
        print("\n1. Prikaz knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("5. Prodaja knjiga")
        print("7. Dodaj knjigu")
        print("8. Izmeni knjigu")
        print("9. Obrisi knjigu")
        print("10. Kraj")
        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 3:
            prikazi_akcije()
        elif stavka == 4:
            pretrazi_akcije()
        elif stavka == 5:
            prodaja_knjiga()
        elif stavka == 7:
            sifra = int(input('sifra: '))
            naslov = input('naslov: ')
            autor = input('autor: ')
            isbn = input('isbn: ')
            izdavac = input('izdavac: ')
            broj_strana = int(input('broj strana: '))
            godina = int(input('godina: '))
            cena = int(input('cena: '))
            kategorija = input('kategorija: ')
            knjiga = dodaj_knjigu(sifra, naslov, autor, isbn, izdavac, broj_strana, godina, cena, kategorija)
            lista_knjiga = ucitaj_knjige()
            uspesno = registracija_knjige(lista_knjiga, knjiga)
            if uspesno:
                sacuvaj_knjige(lista_knjiga)
            else:
                print("Vec postoji knjiga sa tom sifrom")
        elif stavka == 8:
            sifra = int(input('sifra: '))
            knjiga = pretraga_knjiga_po_sifri(sifra)
            if knjiga is None:
                print("Ne postoji knjiga sa sifrom: ", sifra)
            else:
                print(knjiga)
                knjiga['naslov'] = input('naslov: ')
                knjiga['autor'] = input('autor: ')
                knjiga['isbn'] = input('isbn: ')
                knjiga['izdavac'] = input('izdavac: ')
                knjiga['broj_strana'] = input('broj strana: ')
                knjiga['godina'] = int(input('godina: '))
                knjiga['cena'] = int(input('cena: '))
                knjiga['kategorija'] = input('kategorija: ')
                sacuvaj_knjige(knjiga)
        elif stavka == 9:
            sifra = int(input("Unesite sifru knjige: "))
            brisanje_knjiga(sifra)
            print("Knjiga je obrisana!")
        elif stavka == 10:
            return
        else:
            print("Pokusajte ponovo!")


def main():
    for x in range(3):
        ulogovani_korisnik = prijava()

        if ulogovani_korisnik is not None:
            if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
                meni_administrator()
                break
            elif ulogovani_korisnik['tip_korisnika'] == 'Menadzer':
                meni_menadzer()
                break
            elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
                meni_prodavac()
                break
            else:
                print("Greska! Nepostojeca uloga korisnika!")


main()
