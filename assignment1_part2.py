
class Book:
    author = ''
    title = ''
    def __init__(self, author, title):
        self.author = author
        self.title = title

    def display(self):
        print(f'{self.title}, written by {self.author}')


if __name__ == "__main__":
    harry_potter = Book("J. K. Rowling", "Harry Potter and the Goblet of Fire")
    ivanhoe = Book("Walter Scott", "Ivanhoe: A Romance")

    harry_potter.display()
    ivanhoe.display()
