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

        pass

    def termekek_lekerdezese(self) -> dict[str, int]:

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

        pass
