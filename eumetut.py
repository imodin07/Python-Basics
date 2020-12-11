# Enumerate Function

# Enumerate means mentioning one by one.

''' If we go to Nana Peth with the list to buy spare part for motorcycle and upon reaching there
your mecanich calls you and tells you don't bring second item from list then what will we do? '''

parts = ["Clutch cable", "Sprocket", "Mirrors", "Accelerator cable"]

i = 1
for item in parts:
    if i%2 != 0:
        print(f"Don't buy {item}")
    i += 1

# So this will be out normal program but instead of this we can do the following.

for index, item in enumerate(parts):
    if index%2 == 2:
        print(f"Don't buy {item}")