"""                                     Технічне завдання до домашнього завдання №6.

Розробіть систему для управління адресною книгою.

                        Сутності(Класи):

- Field: Базовий клас для полів запису.
- Name: Клас для зберігання імені контакту. Обов'язкове поле.
- Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
- Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
- AddressBook: Клас для зберігання та управління записами.

                        Функціональність:

- AddressBook:Додавання записів.
- Пошук записів за іменем.
- Видалення записів за іменем.
- Record:Додавання телефонів.
- Видалення телефонів.
- Редагування телефонів. 
- Пошук телефону.

                        Рекомендації для виконання

    В якості старту візьміть наступний базовий код для реалізації цього домашнього завдання:

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    # реалізація класу
		pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
		pass

    Після реалізації ваш код має виконуватися наступним чином:
# Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
     
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

                        
                        Критерії оцінювання
                        
1. Клас AddressBook:
- Має наслідуватись від класу UserDict .
- Реалізовано метод add_record, який додає запис до self.data. Записи Record у AddressBook зберігаються як 
  значення у словнику. В якості ключів використовується значення Record.name.value.
- Реалізовано метод find, який знаходить запис за ім'ям. На вхід отримує один аргумент - рядок, якій 
  містить ім’я. Повертає об’єкт Record, або None, якщо запис не знайден.
- Реалізовано метод delete, який видаляє запис за ім'ям.
- Реалізовано магічний метод __str__ для красивого виводу об’єкту класу AddressBook .                        

2. Клас Record:
- Реалізовано зберігання об'єкта Name в атрибуті name.
- Реалізовано зберігання списку об'єктів Phone в атрибуті phones.
- Реалізовано метод для додавання - add_phone .На вхід подається рядок, який містить номер телефона.
- Реалізовано метод для видалення - remove_phone. На вхід подається рядок, який містить номер телефона.
- Реалізовано метод для редагування - edit_phone. На вхід подається два аргумента - рядки, які містять 
  старий номер телефона та новий. У разі некоректності вхідних даних метод має завершуватись помилкою 
  ValueError.
- Реалізовано метод для пошуку об'єктів Phone - find_phone. На вхід подається рядок, який містить номер 
  телефона. Метод має повертати або об’єкт Phone, або None .

3. Клас Phone:
- Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
- Наслідує клас Field. Значення зберігaється в полі value .
"""
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        super().__init__(value)
        

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)
        else:
            raise ValueError("Phone number not found.")

    def edit_phone(self, old_number, new_number):
        phone = self.find_phone(old_number)
        if phone:
            new_phone = Phone(new_number)
            index = self.phones.index(phone)
            self.phones[index] = new_phone
        else:
            raise ValueError("Old phone number not found.")

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise ValueError("Record not found.")

    def __str__(self):
        return '\n'.join(str(record) for record in self.data.values())


# Створення нової адресної книги
book = AddressBook()
# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
# Додавання запису John до адресної книги
book.add_record(john_record)
# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
     
print(book)
# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# Видалення запису Jane
book.delete("Jane")
# Перевірка видалення запису Jane з адресної книги
print(book)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
