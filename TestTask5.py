from Task5 import book
from Task5 import member
from Task5 import staffmember
from Task5 import library
book1 =book("python", "omar hany", 12345, True)
book2 =book("flask", "zeyad elswah", 54321, False)
book3 =book("javascript", "ali abdo", 13654, True)

member1 =member("ziad", 1550)
member2 =member("amr", 1551)

staffmember1 =staffmember("omar ahmed", 1440, "z001")
staffmember2 =staffmember("said adel", 1441, "z002" )


print(book1.title)
Library = library()

new_book = book("Algorithms", "hany shaker", 67890, True)
staffmember.add_book(staffmember1, new_book, Library)