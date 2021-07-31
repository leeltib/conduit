# Test data of test case A008

name = 'testuser03'
mail = 'tuser03@gmail.com'
passw = 'TestUser03'
name_cont = 'testuser01'
mail_cont = 'tuser01@gmail.com'
passw_cont = 'TestUser01'

# Input numbers:
# first number: number of the post (by list position) 
# second number: number of the comment 
# Number of posts and comments can be set arbitrary, however
# each type of comments have to be set at least once during the test.
# In case of less test cases comment types can be narrowed down.
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

# number of elements can vary
comment_full = [comment_positive1, comment_positive2, comment_negative1, comment_negative2]
