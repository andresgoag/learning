# We always should create our own exception with better names

# Must be inherited from a built in exception to be raised
class TooManyPagsReadError(ValueError):...

class Book:
    def __init__(self, name, page_count):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return(
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )

    def read(self, pages):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagsReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages.")
        self.pages_read += pages
        print(
            f"You have now read {self.pages_read} pages out of {self.page_count}.")




# Error classes with parameters
class MyCustomError(Exception):
    def __init__(self, message, code) -> None:
        self.code = code
        super().__init__(f'Error code {code}: {message}')




if __name__ == "__main__":

    python101 = Book("Python 101", 50)
    pages_to_read = 50

    try:
        if not pages_to_read:
            raise MyCustomError("An error happened", 500)

        python101.read(pages_to_read)

    except TooManyPagsReadError as e:
        print(e)

    except MyCustomError as e:
        print(e.code)