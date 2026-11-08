
# Library system has books and magazines, allowing students to borrow items, display item information and check items availability stock.

from abc import ABC, abstractmethod

# Parent abstract class
class LibraryItem(ABC):

    # Constructor
    def __init__(self, title, item_id):
        self.title = title
        self.__item_id = item_id # private attribute
        self.__is_available = True # private attribute

    # Encapsulation: getter
    @property
    def available(self):
        return self.__is_available

    def borrow_item(self):
        if self.__is_available:
            self.__is_available = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is currently not available.")

    def return_item(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")

    @abstractmethod
    def display_info(self):
        pass

    def __str__(self):
        return f"Title: {self.title}, ID: {self.__item_id}"

# child class 1
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_info(self):
        availability = "Available" if self.available else "Not Available"
        print(f"Book: {self.title}, Author: {self.author}, ID: {self._LibraryItem__item_id}")

# child class 2
class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display_info(self):
        availability = "Available" if self.available else "Not Available"
        print(f"Magazine: {self.title}, Issue: {self.issue_number}, ID: {self._LibraryItem__item_id}")

class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

library=Library()

b1=Book("Basic Python", 100, "Jhon")
m1=Magazine("Python Magazine", 200, "Issue 1")

library.add_item(b1)
library.add_item(m1)

print(f"Total items in library: {len(library)}")

for item in library.items:
    item.display_info()

print("\nBorrowing items:")
b1.borrow_item()

print("\nReturning items:")
b1.return_item()

b2= Book("Advanced Python", 101, "Alice")
library.add_item(b2)

print("\n Updated library items:")
print("Avalaibility of items:", b1.available, b2.available)