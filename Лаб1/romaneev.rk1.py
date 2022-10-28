class Chapter:
    """Глава"""
    def __init__(self, id, name, pages, number, book_id):
        self.id = id
        self.name = name
        self.pages = pages
        self.number = number
        self.book_id = book_id

class Book:
    """Книга"""
    def __init__(self, id, name, author, year):
        self.id = id
        self.name = name
        self.author = author
        self.year = year

class BookChapter:
    """Главы книги для реализации связи многие-ко-многим"""
    def __init__(self, book_id, chapter_id):
        self.book_id = book_id
        self.chapter_id = chapter_id

# Книги
books = [
    Book(1, 'Книга Война и мир', 'Л.Н.Толстой', 1869),
    Book(2, 'Роман Отцы и дети', 'И.С.Тургенев', 1862),
    Book(3, 'Пьеса Чайка', 'А.Н.Островский', 1967),
    Book(4, 'Книга Двенадцать стульев', 'И.А.Бунин', 1928),

    Book(11, 'Капитанская дочка', 'А.С.Пушкин', 1836),
    Book(12, 'Евгений Онегин', 'А.С.Пушкин', 1833),
    Book(13, 'Руслан и Людмила', 'А.С.Пушкин', 1820),
]

# Главы
chapters = [
    Chapter(1, 'Война', 100, 1, 1),
    Chapter(2, 'Мир', 200, 2, 1),
    Chapter(3, 'Война и мир', 300, 3, 1),
    Chapter(4, 'Война и мир', 400, 4, 1),
    Chapter(5, 'Война и мир', 500, 5, 1),

    Chapter(6, 'Отец', 100, 1, 2),
    Chapter(7, 'Дети', 200, 2, 2),
    Chapter(8, 'Отцы и дети', 300, 3, 2),

    Chapter(9, 'Чайка', 100, 1, 3),
    Chapter(10, 'Чайка', 200, 2, 3),
    Chapter(11, 'Чайка', 300, 3, 3),

    Chapter(12, 'Двенадцать', 100, 1, 4),
    Chapter(13, 'Стульев', 200, 2, 4),
    Chapter(14, 'Двенадцать стульев', 300, 3, 4),

    Chapter(15, 'Капитанская', 100, 1, 11),
    Chapter(16, 'Дочка', 200, 2, 11),

    Chapter(17, 'Евгений', 100, 1, 12),
    Chapter(18, 'Онегин', 200, 2, 12),

    Chapter(19, 'Руслан', 100, 1, 13),
    Chapter(20, 'Людмила', 200, 2, 13),
]

# Главы книг
book_chapters = [
    BookChapter(1, 1),
    BookChapter(1, 2),
    BookChapter(1, 3),
    BookChapter(1, 4),
    BookChapter(1, 5),

    BookChapter(2, 6),
    BookChapter(2, 7),
    BookChapter(2, 8),

    BookChapter(3, 9),
    BookChapter(3, 10),
    BookChapter(3, 11),

    BookChapter(4, 12),
    BookChapter(4, 13),
    BookChapter(4, 14),

    BookChapter(11, 15),
    BookChapter(11, 16),

    BookChapter(12, 17),
    BookChapter(12, 18),

    BookChapter(13, 19),
    BookChapter(13, 20),
    # Случайные для многие-ко-многим
    BookChapter(1, 6),
    BookChapter(1, 7),
    BookChapter(1, 8),
]

def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(b.name, b.year, c.number, c.name, c.pages)
        for b in books 
        for c in chapters
        if c.book_id == b.id
    ]
    
    # Соединение данных многие-ко-многим
    many_to_many = [(b.name, b.author, b.year, c.name, c.pages)
        for b in books
        for c in chapters
        for bc in book_chapters
        if b.id == bc.book_id and c.id == bc.chapter_id
    ]
 
    print('Задание E1')
    res_11 = [b for b in books if b.name.startswith('Книга')]
    res_11 = {b.name: [(otm[2], otm[3]) for otm in one_to_many if otm[0] == b.name] for b in res_11}
    print(res_11)

    print('Задание E2')
    res_12 = [b.name for b in books]
    for i in range(len(res_12)):
        n_of_chapters = len([otm[2] for otm in one_to_many if otm[0] == res_12[i]])
        sum_of_pages = sum([otm[4] for otm in one_to_many if otm[0] == res_12[i]])
        res_12[i] = (res_12[i], round(sum_of_pages/n_of_chapters, 2))
    res_12 = sorted(res_12, key=lambda x: x[1], reverse=True)
    print(res_12)

    print('Задание E3')
    res_13 = {c.name: [
        mtm[0] for mtm in many_to_many if mtm[3] == c.name
    ] for c in chapters if c.name.startswith('Д')}
    print(res_13)
        
 
if __name__ == '__main__':
    main()