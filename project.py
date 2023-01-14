class book_database:
    def __init__(self , name , author , price , published_time):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_published = published_time
        
        
        
    def book_add(self):
        age = 2022 - int(self.book_published)
        print("Name of Book:" + self.book_name)
        print("Author of Book:" + self.book_author)
        print("Price of Book:" + str(self.book_price))
        print("Published in :" + str(self.book_published))
        print("Age of book:" + str(age))
        print("Book Added to Data Base")
        print("\n")
        
book1 = book_database("Atomic habit", "James Clear", 399, 2018)
book1.book_add()
book2 = book_database("Three Men in a Boat", "Jerome K.", 149, 1889,)
book2.book_add()
book3 = book_database("It Ends With Us", "Colleen Hoove", 499, 2016)
book3.book_add()
book4 = book_database("It Start With Us", "Colleen Hoove", 505, 2022)
book4.book_add()
book5 = book_database("Wuthering Heights", "Emily Brontë", 120, 1859)
book5.book_add()
book6 = book_database("Ikigai ", "Héctor García", 150, 	2017)
book6.book_add()
book6 = book_database("I Refused TO BRIBE", "Gireesh Sharma", 300, 	1988)
book6.book_add()
book7 = book_database("Ten Days", "Azharuddin", 175,2012)
book7.book_add()
