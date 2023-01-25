international = ('XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL')
germany = (36, 38, 40, 42, 44, 46, 48, 50)
usa = (8, 10, 12, 14, 16, 18, 20, 22)
france = (38, 40, 42, 44, 46, 48, 50, 52)
great_britain = (24, 26, 28, 30, 32, 34, 36, 38)
countries = [germany, usa, france, great_britain]
countries_names = ['germany', 'usa','france', 'great_britain']

sizes_ratio = []
for i in countries:
    sizes_ratio.append(dict(zip(dict.fromkeys(international), i)))
sizes_full_dict = dict(zip(countries_names, sizes_ratio))


def exchange(sizes):
    x = []
    for key, val in sizes_full_dict.items():
        x.append(val.get(sizes))
    return dict(zip(countries_names, x))

print(exchange('L'))

