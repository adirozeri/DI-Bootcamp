#e1
user_word = input("enter a word:")

letter_indexes = {}

for index, letter in enumerate(user_word):
    if letter not in letter_indexes:
        letter_indexes[letter] = []
    letter_indexes[letter].append(index)

print(letter_indexes)


#e2
def affordable_items(items, wallet):
    wallet_amount = float(wallet.replace("$", "").replace(",", ""))
    
    affordable = []
    for item, price in items.items():
        price_amount = float(price.replace("$", "").replace(",", ""))
        if price_amount <= wallet_amount:
            affordable.append(item)
    
    affordable.sort()
    
    return affordable if affordable else "Nothing"

