# class ShoppingCart:
#     def __init__(self):
#         self.items = []
        
#     def add_items(self, item, price):
#         self.items.append((item, price))
#         print(f"{item} added to Shopping Cart and its price is {price}.")
        
#     def remove_items(self, item, price):
#         for i in range(len(self.items)):
#             name, p = self.items[i]
#             if name == item and p == price:
#                 self.items.pop(i)
#                 print(f"{item} removed from Shopping Cart.")
#                 return
#         print('Item not found!')
    
#     def show_cart(self):
#         print("Cart items:")
#         for product in self.items:
#             print(product)

        
# cart1 = ShoppingCart()
# cart1.add_items('Apple', 10)
# cart1.add_items('Banana', 5)
# cart1.add_items('Orange', 8)

# cart1.remove_items('Apple', 10)

# cart1.show_cart()

#########################################################

# Exercise 4: Library Class
# attributes : books=[]
# Methods

class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, title, price):
        self.books.append((title, price))
        print(f"Book: {title} with ${price} is added!")
        
    def remove_book(self, title, price):
        for i in range(len(self.books)):
            title, p = self.books[i]
            if title == title and p == price:
                self.books.pop(i)
                print(f"Book: {title} with ${price} is removed!")
                return
        print("Book Not Found!!")
    
    def total_price(self):
        total_price = 0
        for i in range(len(self.books)):
            _, p = self.books[i]
            total_price += p
        print(f"Total price: {total_price} $")
        
        # for book in self.books:
        #     total_price += book[1]
        # return total_price
            
        
    def show_books(self):
        print(f"Available books:")
        for i, book in enumerate(self.books):
            print(f"{i+1}. {book[0]}")


cart1 = Library()
cart1.add_book("Intro to DS", 5000)
cart1.add_book("Intro to ML", 5000)
cart1.add_book("Intro to AI", 5000)
cart1.add_book("Intro to NLP", 5000)

cart1.remove_book('Intro to DS', 5000)

cart1.show_books()

cart1.total_price()


###############################################################














