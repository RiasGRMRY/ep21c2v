import kosar

vasarlas = {}

def feladat_1() -> list:

        try:
                filepath = open("kosar.txt", "r", encoding="UTF-8")
                adat = filepath.read()
                be = adat.splitlines()
                for sor in be:
                        if sor != "F":
                                vasarlas[sor] = vasarlas.get(sor, 0) + 1
                print("1. Feladat: Sikeres beolvasás!")
                #print(vasarlas)
                return be
        except FileNotFoundError:
                print("Hiba! Nem található a file!")
        pass
def feladat_2(lista:list):

        print("2. Feladat: Összesen", lista.count("F"), "db fizetés történt!")
        pass

def feladat_3(lista:list):

        sorszam = int(input("3. Feladat: Adjon meg egy vásárlás sorszámot:"))
        pass

def feladat_4(lista: list) -> None:

        arucikk = str(input("4. Feladat: Adja meg egy termék nevét:"))
        print("A(z)",arucikk  ,"termékből összesen: ",vasarlas[arucikk],"db-ot vásároltak")

        pass

def feladat_5(lista:list, osszeg=str):

        pass
