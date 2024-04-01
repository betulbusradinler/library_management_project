class Validation:
      def int_type_casting(value):
        try:
          is_int = int(value)
          return is_int
        except ValueError:
            print("Please enter a NUMERIC value.\n")


      def check_value_range(value):
        if value<1 :
          return False
        elif value>4 :
          return False
        else :
          return True


class Library:
      def __init__(self) :
        try:
          self.file = open("books.txt", "a+", encoding='utf-8')
        except FileNotFoundError:
            print("File was not found")


      def __del__(self):
        self.file.close()


      def list_books(self):
           with open('books.txt', 'r', encoding='utf-8') as file:
            books = file.read().splitlines()
            if books:
              print("Book List:")
              for book in books:
                  book_info = book.split(',')
                  print(book_info)
                  #print(book_info[0], book_info[1])
            else:
                print("No books found.")

      def add_book(self) :
          try:
            book_title = input("Enter the title of the book: ")
            book_author = input("Enter the author of the book: ")

            while True:
              release_year = input("Enter the release year of the book: ")
              is_int = Validation.int_type_casting(release_year)
              if type(is_int) is int :
                break
              else :
                 continue

            while True:
                number_of_pages = input("Enter the number of pages of the book: ")
                is_int = Validation.int_type_casting(number_of_pages)
                if type(is_int) is int :
                  break
                else :
                  continue

            new_add_book =  "Book Name: {}, Book Author: {}, Release Year: {}, Nummber Of Pages: {}".format(book_title,book_author,release_year,number_of_pages)
            self.file.write(new_add_book)
            self.file.write('\n')
            self.file.flush() # bu kodu kullanmadığım da son eklediğim eleman tam olarak eklenmiyordu.
            print("Book added successfully.")

          except FileNotFoundError :
            print("File was not found")


      def remove_book(self):
            word = input("Enter the book title: ").strip()  # Kullanıcı girişinden önce ve sonra boşlukları kaldır
            found = False
            updated_books = []  # Silinmemiş kitapları saklamak için bir liste

            with open("books.txt", "r", encoding='utf-8') as file:
              books = file.readlines()
            for book in books:
              # Kitap adını ve diğer bilgileri ayırma
              title = book.strip().split(",")[0].split(":")[1].strip()  # Kitap adının etrafındaki boşlukları temizle
              if word != title:
                updated_books.append(book)
              else:
                found = True
            
            # Eğer bir kitap silinmişse, dosyayı güncellenmiş listeye göre yeniden yaz
            if found:
               with open("books.txt", "w", encoding='utf-8') as file:
                 file.writelines(updated_books)
               print(f"'{word}' titled book has been successfully removed.")
            else:
               print(f"No book found with the title '{word}'.")


lib = Library()

while True:
        print( "***MENU***\n1) List Books\n2) Add Book\n3) Remove Book\n4) Quit")
        choice = input("Enter your choice: ")
        try:
            type_casting = Validation.int_type_casting(choice)
            if type(type_casting) is int  :

               range_value = Validation.check_value_range(type_casting)

               if range_value == False :
                  print("Please enter a value between 1 and 4 \n");

               else :
                  if type_casting == 1 :
                      lib.list_books()

                  elif type_casting == 2 :
                       lib.add_book()

                  elif type_casting == 3 :
                       lib.remove_book()

                  elif type_casting == 4:
                      del lib
                      break
                  else:
                      print("Invalid choice. Please enter a valid option.")
        except ValueError :
            print("Invalid choice. Please enter a valid option.")
