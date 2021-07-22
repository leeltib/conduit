# A008 teszteset tesztadatai

name = 'testuser03'
mail = 'tuser03@gmail.com'
passw = 'TestUser03'
name_cont = 'testuser01'
mail_cont = 'tuser01@gmail.com'
passw_cont = 'TestUser01'

# számok jelentése:
# első szám: a bejegyzés sorszáma (ahányadik a listán)
# második szám: a bejegyzéshez rendelt hozzászólás sorszáma
# A hozzászólások száma, a hozzájuk kapcsolt komment szabadon variálható, de megkötés, hogy
# a tesztben minden típusú hozzászólás legalább egyszer szerepeljen! (Kevesebb tesztszituáció esetén csökkenthető a hozzászólás típusok száma...)
com_list = [[1, 2], [2, 4], [5, 1], [10, 3]]
com_list_num = len(com_list)


comment_positive1 = """
Ez egy nagyon pozitív hozzászólás, amiben megdicsérem
a bejegyzés szerzőjét. Jelzem felé, hogy minden
általa leírt gondolat megérintett, és megköszönöm
neki, hogy megosztotta a világgal ezeket a remek
észrevételeket.
"""

comment_positive2 = """
Ez egy alapvetően pozitív hozzászólás, amiben megdicsérem
a bejegyzés szerzőjét, de jelzem felé, hogy van pár
megállapítás a bejegyzésében, ami szerintem nincs teljesen
rendben.
"""

comment_negative1 = """
Ez egy alapvetően kritikus hozzászólás, amiben felhívom
a bejegyzés szerzőjének figyelmét azokra a szerintem téves
megállapításokra amik a bejegyzésében olvashatók.
"""

comment_negative2 = """
Ez egy számomra felháborító, hazug, rosszindulatú és
ostoba bejegyzés. Ennek a véleményemnek kissé indulatosan
hangot is adok...
"""

# az elemek száma szabadon változtatható
comment_full = [comment_positive1, comment_positive2, comment_negative1, comment_negative2]
