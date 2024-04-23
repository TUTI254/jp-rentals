few_shots = [
    {
        'Question' : "How many rental units do i have that are located in Tokyo? give me a full break down of what they offer from rent the style the size of the unit.",
        'SQLQuery' : "SELECT * FROM rental_units WHERE location_id = 1",
        'SQLResult' : "[(1, 1, '1R', 'furnished', Decimal('80000.00'), 'Tokyo Station', 'wifi, parking space, washing machine, air conditioner'), (4, 1, '1LDK', 'not furnished', Decimal('85000.00'), 'Tokyo Station', 'wifi, parking space, washing machine')]",
        'Answer' : "There are 2 rental units in Tokyo; the first is a 1R furnished unit going for ¥80000 per month, the second on is a 1LDK not furnished going for ¥85000 per month."
    },
    {
        'Question' : "I'm looking for a rental unit that has an air conditioner what options are available and which locations are they in?",
        'SQLQuery' : "SELECT `size`, `rent`, `location_id`, `amenities` FROM `rental_units` WHERE `amenities` LIKE '%air conditioner%'",
        'SQLResult' : "[('1R', Decimal('80000.00'), 1, 'wifi, parking space, washing machine, air conditioner'), ('1DK', Decimal('70000.00'), 3, 'wifi, washing machine, air conditioner'), ('2DK', Decimal('90000.00'),  5, 'wifi, parking space, air conditioner')]",
        'Answer' : "There are 3 rental units that have an air conditioner. They are located in Tokyo a 1R going for ¥80000.00 per month, Kyoto a 1DK going for ¥70000.00 per month and Yokohama a 2DK going for ¥90000.00 per month."
    },
    {
        'Question' : "What units are in Osaka that are furnished and what are the rates per month?",
        'SQLQuery' : "SELECT size, rent FROM rental_units WHERE location_id = 2 AND style = 'furnished'",
        'SQLResult' : "",
        'Answer' : "There is a 1K Unit going for ¥60000.00 per month"
    },
]