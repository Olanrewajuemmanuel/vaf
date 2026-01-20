from main import VectorIndex, Disk

if __name__ == "__main__":
    index = VectorIndex("l2", dim=10)
    records = [
        {
            "id": 1,
            "text": "Denim jeans were originally created as durable workwear for laborers.",
            "category": "fashion",
        },
        {
            "id": 2,
            "text": "The fabric denim comes from the French phrase 'serge de Nîmes.'",
            "category": "fashion",
        },
        {
            "id": 3,
            "text": "This textile was valued for its strength and resistance to wear.",
            "category": "fashion",
        },
        {
            "id": 4,
            "text": "Levi Strauss popularized jeans during the California Gold Rush.",
            "category": "fashion",
        },
        {
            "id": 5,
            "text": "Miners needed clothing that could survive harsh conditions.",
            "category": "fashion",
        },
        {
            "id": 6,
            "text": "Rivets were added to reinforce stress points on pockets.",
            "category": "fashion",
        },
        {
            "id": 7,
            "text": "These metal rivets dramatically increased garment lifespan.",
            "category": "fashion",
        },
        {
            "id": 8,
            "text": "Over time, jeans moved from workwear into everyday fashion.",
            "category": "fashion",
        },
        {
            "id": 9,
            "text": "Hollywood films helped make denim stylish and rebellious.",
            "category": "fashion",
        },
        {
            "id": 10,
            "text": "Jeans later became symbols of youth culture worldwide.",
            "category": "fashion",
        },
        {
            "id": 11,
            "text": "Today, denim appears in luxury fashion as well as streetwear.",
            "category": "fashion",
        },
        {
            "id": 12,
            "text": "The color black was once considered inappropriate for fashionable clothing.",
            "category": "fashion",
        },
        {
            "id": 13,
            "text": "In medieval Europe, black dyes were expensive and difficult to produce.",
            "category": "fashion",
        },
        {
            "id": 14,
            "text": "Only wealthy individuals could afford deep black garments.",
            "category": "fashion",
        },
        {
            "id": 15,
            "text": "This made black a symbol of power and authority.",
            "category": "fashion",
        },
        {
            "id": 16,
            "text": "Judges and royalty often wore black to show status.",
            "category": "fashion",
        },
        {
            "id": 17,
            "text": "In the nineteenth century, black became linked to formality.",
            "category": "fashion",
        },
        {
            "id": 18,
            "text": "Industrial dye production made black more accessible.",
            "category": "fashion",
        },
        {
            "id": 19,
            "text": "Coco Chanel later redefined black as elegant and modern.",
            "category": "fashion",
        },
        {
            "id": 20,
            "text": "Her little black dress changed women’s fashion permanently.",
            "category": "fashion",
        },
        {
            "id": 21,
            "text": "Black became associated with simplicity and sophistication.",
            "category": "fashion",
        },
        {
            "id": 22,
            "text": "It remains a dominant color in global fashion today.",
            "category": "fashion",
        },
        {
            "id": 23,
            "text": "The Great Pyramid of Giza was the tallest man-made structure for centuries.",
            "category": "architecture",
        },
        {
            "id": 24,
            "text": "It stood at about 146 meters when originally completed.",
            "category": "architecture",
        },
        {
            "id": 25,
            "text": "The pyramid was built over four thousand five hundred years ago.",
            "category": "architecture",
        },
        {
            "id": 26,
            "text": "Millions of limestone blocks were used in its construction.",
            "category": "architecture",
        },
        {
            "id": 27,
            "text": "Each block weighed several tons on average.",
            "category": "architecture",
        },
        {
            "id": 28,
            "text": "The builders achieved remarkable precision without modern tools.",
            "category": "architecture",
        },
        {
            "id": 29,
            "text": "The pyramid’s sides align closely with the cardinal directions.",
            "category": "architecture",
        },
        {
            "id": 30,
            "text": "This alignment reflects advanced ancient surveying knowledge.",
            "category": "architecture",
        },
        {
            "id": 31,
            "text": "Contrary to myth, enslaved people did not build the pyramid.",
            "category": "architecture",
        },
        {
            "id": 32,
            "text": "Skilled laborers and craftsmen carried out the work.",
            "category": "architecture",
        },
        {
            "id": 33,
            "text": "The structure remains an architectural marvel of human history.",
            "category": "architecture",
        },
    ]
    index.upsert_records(records)
    print(str(index))

    # Top-k search
    results = index.query("What is the Great Pyramid of Giza?", top_k=10)
    assert len(results) == 10

    results = index.query("What is the Great Pyramid of Giza?", top_k=10, filters={"category": "architecture"})

    # With disk
    index = VectorIndex("l2", dim=10, disk=Disk("/path/to/file"))
    print(str(index))
    results = index.query("What is the Great Pyramid of Giza?", top_k=10)
    assert len(results) == 10