import re
import sys

#### @@author: ahmedsharif
##### input values defined in assignment
data = ["Winterallee 3", 
        "Am Bächle 23",
        "Auf der Vogelwiese 23 b",
        '4, rue de la revolution', 
        "200 Broadway Av",
        'Calle Aduana, 29',
        'Calle 39 No 1540'
]


def extract_street_housenumber(data: []):
    result = []
    for item in data:
        res = {}

        #### regex to extract the house number and last character from string
        house_string = re.search(r"(\d+)+ +\w{0,1}$|(\d+)$|(^\d+)", item)
        
        #### regex to extract the street from string
        street_string = re.search(r"[A-Za-zäöüÄÖÜß\s]+", item)
        
        res['street'] = street_string.group(0) if street_string else None
        res['housenumber'] = house_string.group(0) if house_string else None

        result.append(res)

    return result

if __name__ == "__main__":
    print("pass user input or it will use predefined values of assignment")
    print("start reading data", "\n")
    print("user input is", sys.argv)

    if len(sys.argv) > 1:
        data = sys.argv[1:]
    
    final_result = extract_street_housenumber(data)
    print("output result is ", final_result)

