"""
This is a script for generating a menu HTML-file for RF (Realistforeningen). To run the script the 
file "Meny (RF).xlsx" must be present in the same directory as the script.

The output is the file "meny.html". This file can be converted by opening it in a web-browser and 
printing to PDF, or using a tool like Pandoc. Some categories will appear in a pre-defined order,
with the rest appearing in alphabetical order between these. If any of the pre-defiend categories 
have no entries, a warning will be printed to the terminal.

Maintainer:
Iver Oknes (iver@oknes.no)
"""
import pandas as pd

html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RF Meny</title>
    <style>
        html {
            font-family: arial, sans-serif;
        }

        .prod {
            width: 40%;
        }

        .size {
            width: 12%;
        }

        .abv {
            width: 12%;
        }

        .orig {
            width: 25%;
        }
        
        .price {
            width: 11%;
        }

        /*h1 {
            text-align: center;
        }*/

        table {
          border-collapse: collapse;
          width: 100%;
        }  
        
        td, th {
          border: 1px solid #dddddd;  
          text-align: left;
          padding: 8px;
        }  
        
        tr:nth-child(even) {
          background-color: #dddddd;  
        }  
    </style>
</head>
<body>
"""

try:
    menu = pd.read_excel("Meny (RF).xlsx", header=0)
except FileNotFoundError:
    print("File 'Meny (RF).xlsx' missing! Can't generate menu without this file!")
    exit()

in_stock = menu.loc[pd.notna(menu["Til salg"])]
name = "Vare"
category = "Kategori"
abv = "ABV"
volume = "Størrelse"
country = "Land"
price = "Eksternpris"

categories_list = list(set(in_stock[category]))

predefined_start = ["Fat", "Lager", "Pale Ale", "IPA", "Hveteøl"]

for idx, cat in enumerate(predefined_start):
    try:
        categories_list.insert(idx, categories_list.pop(categories_list.index(cat)))
    except ValueError:
        print(f"Ingen produkter av typen {cat} på menyen!")

predefined_end = ["Hvitvin", "Rødvin", "Cava", "Musserende vin", "Portvin", "Shot", "Alkoholfritt øl", "Mineralvann"]


for cat in predefined_end:
    try:
        categories_list.append(categories_list.pop(categories_list.index(cat)))
    except ValueError:
        print(f"Ingen produkter av typen {cat} på menyen!")

for cat in categories_list:
    html += f"<h1>{cat}</h1>\n"
    cat_prods = in_stock.loc[(in_stock[category] == cat)]

    html += "<table>\n<tr><th>Produkt</th><th>Størrelse</th><th>ABV</th><th>Opprinnelse</th><th>Pris</th></tr>\n"

    for i in cat_prods.index:
        prod = cat_prods.loc[i]

        p_name = prod[name]
        p_abv = f"{prod[abv] * 100:.1f}%" if pd.notna(prod[abv]) else ""
        p_volume = f"{prod[volume] * 100:.0f}cl" if pd.notna(prod[volume]) else ""
        p_price = f"kr {round(prod[price])},-" if pd.notna(prod[price]) else ""
        p_country = prod[country] if pd.notna(prod[country]) else ""

        html += f"<tr><td class='prod'>{p_name}</td><td class='size'>{p_volume}</td><td class='abv'>{p_abv}</td><td class='orig'>{p_country}</td><td class='price'>{p_price}</td></tr>\n"

    html += "</table>\n"

html += """</body>
</html>
"""

with open("meny.html", 'w') as outfile:
    outfile.write(html)
print("Meny skrevet til meny.html")
