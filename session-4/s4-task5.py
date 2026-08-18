product = ["mi-Band 5", "SAMSUNG-Galaxy", "realme-Book"]

for i in product:
    i = i.strip()
    replace_product =  i.replace("-", " ")
    title_product = replace_product.title()

    print(i)
    print(replace_product)
    print(title_product)