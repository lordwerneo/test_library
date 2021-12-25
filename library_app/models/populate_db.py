from library_app import db
from library_app.models import Book, Genre

def populate_genre():
    genre_list = [['fantasy', 'Fantasy is a genre of speculative fiction involving magical elements, typically set in a fictional universe and sometimes inspired by mythology and folklore.'],
                  ['technology', 'Genre to and explain tools, machines, techniques, crafts, systems, and methods used to solve a problem, achieve a goal, or perform a specific function. They are about the things we can create that help to make our lives easier and more efficient.'],
                  ['history', 'A genre that is defined by its cultural and historical usage, whose features and definition are formulated from the observation of preexisting literary knowledge. The opposite of a theoretical genre.'],
                  ['food & drink', 'Books in the food and drinks nonfiction genre are about the history of or the recipes to make certain foods and drinks. The food books in this genre are about the origins, types, preparations, families, and nutritional values of food.'],
                  ['science fiction', 'Science fiction is a genre of speculative fiction that typically deals with imaginative and futuristic concepts such as advanced science and technology, space exploration, time travel, parallel universes, and extraterrestrial life.']]

    for genre in genre_list[:2]:
        genre_to_input = Genre(name=genre[0], description=genre[1])
        db.session.add(genre_to_input)
        db.session.commit()


def pupulate_book():
    book_list = [['0-7475-3269-9', 'Harry Potter and the Philosopher\'s Stone', 'J. K. Rowling', 1997, 'Bloomsbury', 3, 1],
                 ['0-7475-3849-2', 'Harry Potter and the Chamber of Secrets', 'J. K. Rowling', 1998, 'Bloomsbury', 5, 1],
                 ['0-7475-4215-5', 'Harry Potter and the Prisoner of Azkaban', 'J. K. Rowling', 1999, 'Bloomsbury', 7, 1],
                 ['0-7475-4624-X', 'Harry Potter and the Goblet of Fire', 'J. K. Rowling', 2000, 'Bloomsbury', 6, 1],
                 ['0-7475-5100-6', 'Harry Potter and the Order of the Phoenix', 'J. K. Rowling', 2003, 'Bloomsbury', 4, 1],
                 ['0-7475-8108-8', 'Harry Potter and the Half-Blood Prince', 'J. K. Rowling', 2005, 'Bloomsbury', 5, 1],
                 ['0-545-01022-5', 'Harry Potter and the Deathly Hallows', 'J. K. Rowling', 2007, 'Bloomsbury', 4, 1],
                 ['0-00-224584-1', 'A Game of Thrones', 'George R. R. Martin', 1996, 'Voyager Books', 4, 1],
                 ['0-00-224585-X', 'A Clash of Kings', 'George R. R. Martin', 1999, 'Voyager Books', 5, 1],
                 ['0-00-224586-8', 'A Storm of Swords', 'George R. R. Martin', 2001, 'Voyager Books', 7, 1],
                 ['0-00-224743-7', 'A Feast for Crows', 'George R. R. Martin', 2005, 'Voyager Books', 5, 1],
                 ['978-0-00-745637-6', 'A Dance with Dragons', 'George R. R. Martin', 2012, 'Voyager Books', 2, 1],
                 ['1-54-605930-X', 'Big Tech Battle to Erase Trump Movement and Steal the Election', 'Allum Bokhari', 2020, 'Center Street', 1, 2],
                 ['978-1-59-463296-9', 'How We Got to Now: Six Innovations That Made the Modern World', 'Steven Johnson', 2020, 'Riverhead Book', 3, 2],
                 ['0-39-956382-2', 'Ten Emerging Technologies That\'ll Improve and Ruin Everything', 'Kelly Weinersmith', 2017, 'Penguin Press', 2, 2],
                 ['1-54-177375-6', 'How the Tech Titans\' Thinking Machines Could Warp Humanity', 'Amy Webb', 2019, 'PublicAffairs', 5, 2],
                 ['1-53-811584-0', 'Deviced!: Balancing Life and Technology in a Digital World', 'Doreen Dodgen-Magee', 2018, 'Rowman & Littlefield', 2, 2],
                 ['1-501-16-3809', 'The Money Guide You Need Now, Later, and Much Late', 'Ric Edelman', 2017, 'Simon & Schuster', 5, 2],
                 ['978-9-78-968273-7', 'Digital: The New Code of Wealth', 'Joshua J Omojuwa', 2019, 'A\'Lime Media Ltd', 3, 2],
                 ['1-544-35083-X', 'Digital Leadership: Changing Paradigms for Changing Times', 'Eric C. Sheninger', 2019, 'Corwin', 5, 2],
                 ['1-46-547359-9', 'How to Be Good at Science, Technology, and Engineering', 'DK', 2018, 'DK Children', 9, 2],
                 ['1-63-535760-8', 'The Technological Elixir', 'Ryan D Gable', 2017, 'Neely Worldwide', 1, 2],
                 ['0-76-538756-5', 'The Invisible Life of Addie LaRue', 'V.E. Schwab', 2020, 'Tor Books', 6, 1]]

    for book in book_list:
        book_to_input = Book(isbn=book[0], title=book[1], author=book[2],
                             year=book[3], publisher=book[4], copies=book[5],
                             genre_id=Genre.query.get(book[6]).id)
        db.session.add(book_to_input)
        db.session.commit()


populate_genre()
pupulate_book()
