from operator import itemgetter

'''Вариант Б.
1. «Книга» и «Глава» связаны соотношением один-ко-многим. 
Выведите список всех связанных глав и книг, отсортированный по главам, сортировка по книгам произвольная.
2. «Книга» и «Глава» связаны соотношением один-ко-многим. 
Выведите список книг с количеством глав в каждой книге, отсортированный по количеству глав.
3. «Книга» и «Глава» связаны соотношением многие-ко-многим. 
Выведите список всех глав, у которых названия закачиваются на "ми", и названия их книг.
'''


class book() :
    def __init__ (self, ID, name):
        self.id = ID # Номер книги
        self.name = name # Название книги


class chapter() :
    def __init__ (self, ID, chapter_name, chapter_page, book_ID):
        self.id = ID # Номер главы 
        self.name = chapter_name # Название главы 
        self.page = chapter_page # Номер страницы, где находится глава
        self.book_id = book_ID # Номер книги


class bookchapter() :
    def __init__ (self, book_ID, chapter_ID):
        self.book_id = book_ID # Номер книги
        self.chapter_id = chapter_ID # Номер главы


books = [
    book(1, 'Google Android. Программирование для мобильных устройств'),
    book(2, 'Java 2. Самоучитель'),
    book(3, '1С: предприятие 8.1. Конфигурирование и администрирование'),
    book(4, 'Думай и богатей'),
    book(5, 'Возрождение бренда. Шесть принципов. Вдохните в свой бренд новую жизнь вместе с McDonalds'),
    book(6, 'Горизонт событий'),
        ]

chapters = [
    chapter(1, 'Компоненты Android-приложения', 43,1),
    chapter(2, 'Управление деятельностями', 249,1),
    chapter(3, 'Ресурсы, активы и локализация приложений', 349,1),
    chapter(4, 'Все, что надо знать о программах', 14,2),
    chapter(5, 'Наследование', 203, 2),
    chapter(6, 'Объекты конфигурации', 80 ,3),
    chapter(7, 'Механизм Web-сервисов', 612, 3),
    chapter(8, 'Изумительная сила секрета доказывается фактами', 3,4),
    chapter(9, 'Шесть принципов возрождения бренда', 46,5),
    chapter(10, 'Принцип 2. Восстановление соответствия бренда запросам потребителей', 68,5),
    chapter(11, 'Альфа Цефея', 2048,6),
        ]

chapters_of_books = [
    bookchapter(1, 1),
    bookchapter(1, 2),
    bookchapter(1, 3),
    bookchapter(2, 4),
    bookchapter(2, 5),
    bookchapter(3, 6),
    bookchapter(3, 7),
    bookchapter(4, 8),
    bookchapter(5, 9),
    bookchapter(5, 10),
    bookchapter(6, 11)]


def task1(oneToMany):
    try:
        
        B1 = sorted(oneToMany, key = itemgetter(0))
        return B1    
    except(TypeError):
        raise TypeError("Выражение должно быть типа list[tuple[str, int, str]]")

def task2(oneToMany):
    
    B2 = []
    for i in range(6):
        count_chap = list(filter(lambda j: j[2] == books[i].name, oneToMany))
        B2.append((books[i].name, len(count_chap)))
    B2 = sorted(B2, key=itemgetter(1), reverse=True)
    return B2


def task3(manyToMany):
    
    B3 = []
    for i in manyToMany:
        if (i[0][-2:]=='ми'):
            B3.append(i)
    return B3


def main():
     # Соединение данных один-ко-многим
    oneToMany = [(chap.name, chap.page, book.name)
                    for book in books
                    for chap in chapters
                    if chap.book_id == book.id
                ]

    # Соединение данных многие-ко-многим
    manyToMany_temp = [ (book.name, chobs.book_id, chobs.chapter_id)
                        for book in books
                        for chobs in chapters_of_books
                        if book.id == chobs.book_id
                        ]   

    manyToMany =  [(chap.name, chap.page, book_name)
                    for book_name, book_id, chapter_id in manyToMany_temp
                    for chap in chapters if chap.id == chapter_id]


    
    print(task1(oneToMany))
    print(task2(oneToMany))
    print(task3(manyToMany))

    

if __name__ == "__main__":
    main()