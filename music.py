class Album:
    def __init__(self, title, artist, genre, price):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.artist} | Genre: {self.genre} | ₹{self.price}"


class MusicStore:
    def __init__(self):
        self.catalog = []
        self.cart = []

    def add_album(self, album):
        self.catalog.append(album)

    def show_catalog(self):
        print("\n🎶 Available Albums:")
        for idx, album in enumerate(self.catalog, start=1):
            print(f"{idx}. {album}")

    def search_album(self, keyword):
        print(f"\n🔍 Search results for '{keyword}':")
        results = [album for album in self.catalog if keyword.lower() in album.title.lower() or keyword.lower() in album.artist.lower()]
        if results:
            for album in results:
                print(f"- {album}")
        else:
            print("No albums found.")

    def add_to_cart(self, index):
        if 0 <= index < len(self.catalog):
            self.cart.append(self.catalog[index])
            print(f"✅ Added '{self.catalog[index].title}' to cart.")
        else:
            print("❌ Invalid album number.")

    def view_cart(self):
        print("\n🛒 Your Cart:")
        if not self.cart:
            print("Cart is empty.")
            return
        total = 0
        for album in self.cart:
            print(f"- {album}")
            total += album.price
        print(f"Total: ₹{total}")

    def checkout(self):
        if not self.cart:
            print("🛒 Your cart is empty. Add some albums first!")
            return
        self.view_cart()
        print("💳 Thank you for your purchase!")
        self.cart.clear()


# Sample usage
def run_store():
    store = MusicStore()

    # Add some albums
    store.add_album(Album("Midnight Memories", "One Direction", "Pop", 499))
    store.add_album(Album("Random Access Memories", "Daft Punk", "Electronic", 699))
    store.add_album(Album("Abbey Road", "The Beatles", "Rock", 599))
    store.add_album(Album("Thriller", "Michael Jackson", "Pop", 649))

    while True:
        print("\n🎧 Welcome to the Music Store!")
        print("1. View Catalog")
        print("2. Search Album")
        print("3. Add to Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            store.show_catalog()
        elif choice == '2':
            keyword = input("Enter album title or artist: ")
            store.search_album(keyword)
        elif choice == '3':
            store.show_catalog()
            try:
                index = int(input("Enter album number to add to cart: ")) - 1
                store.add_to_cart(index)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == '4':
            store.view_cart()
        elif choice == '5':
            store.checkout()
        elif choice == '6':
            print("👋 Thanks for visiting the Music Store!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# Run the app
run_store()




