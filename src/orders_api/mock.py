from orders_api.db.models import Store, Product
from orders_api.db.session import create_session


stores = [
    {
        "name": "Venus",
        "city": "Karlsruhe",
        "country": "Germany",
        "zipcode": "76131",
        "street": "Europaplatz 2",
        "email": "kundenservice@venus.com",
        "phone": "0721 3526 345",
        "currency": "EUR",
        "domain": "https://online-store.venus.com",
    },
    {
        "name": "Media Bazar",
        "city": "Munich",
        "country": "Germany",
        "zipcode": "80337",
        "street": "Karl-Wilhelm-Strasse 5a-c",
        "email": "hello@media-bazar.de",
        "phone": "089 325 815",
        "currency": "EUR",
        "domain": "https://media-bazar.de",
    },
]

products = [
    {
        "name": "GameStation 6",
        "description": "Play the greatest games on this next-gen entertainment system.",
        "price": 349.49,
    },
    {
        "name": "Adventure Quest: Dark Shadows - for GameStation 6",
        "description": "Explore the wide lands of Left Earth and stop the rise of the Dark Empire.",
        "price": 59.99,
    },
    {
        "name": "6 inch Plastic Planters with Saucers",
        "description": "The Flower Plant Pots are designed with matte finishing exterior in soft, round shapes, bringing out a modern minimalistic styled ceramic like visual representation, with brief stripes making the planters special, fits for any home/office décor. And smooth glossy inner finish for easy cleaning. Great for replanting, and for flower plant lovers",
        "price": 17.49,
    },
    {
        "name": "GameStation 6",
        "description": "Play the greatest games on this next-gen entertainment system.",
        "price": 399.99,
    },
]


def insert_mock_data(session):
    store_rows = [Store(**store) for store in stores]
    session.add_all(store_rows)
    session.flush()
    product_rows = [Product(**product) for product in products]
    product_rows[0].store = store_rows[0]
    product_rows[1].store = store_rows[1]
    product_rows[2].store = store_rows[1]
    product_rows[3].store = store_rows[1]
    session.add_all(product_rows)
    session.commit()


if __name__ == "__main__":
    session = create_session()
    insert_mock_data(session)
