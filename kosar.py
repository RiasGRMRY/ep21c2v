import bolt

class Kosar:
    """
    Egyetlen vásárlás adatait kezelő osztály.

    Az osztály attribútumai:
        - a kosárban lévő árucikkek (név-mennyiség párok)
        - a vásárlás összege
    """

    def __init__(self, termekek: dict[str, int], osszeg: int) -> None:
        self.termekek = termekek
        self.osszeg = osszeg
        pass

    def osszeg_lekerdezese(self) -> int:

        osszeg = 0

        for i in self.termekek:
            if self.termekek[i] > 3:
                osszeg += 1000 + 900 + ((self.termekek[i] - 2) * 800)
            elif self.termekek[i] == 2:
                osszeg += 1900
            else:
                osszeg += 1000
        return osszeg
        pass

    def termekek_lekerdezese(self) -> dict[str, int]:

        vasarlasok = {}
        for i in self.termekek:
            vasarlasok[i] = self.termekek[i]
        return vasarlasok

        pass

    def termekek_szamanak_lekerdezese(self) -> int:

        ossz = 0
        for i in self.termekek:
            ossz += self.termekek[i]
        return ossz

        pass

    def arucikk_mennyisegenek_lekerdezese(self, arucikk: str) -> int:

        for i in self.termekek:
            if arucikk not in self.termekek:
                return 0
            else:
                return self.termekek[arucikk]

        pass

    def kosar_tartalmanak_kiiratasa(self) -> None:

        print("A kosárnak a tartalma:")
        for i in self.termekek:
            print(f"\t{self.termekek[i]} {i}")
        pass
