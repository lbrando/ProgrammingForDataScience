"""In this exercise, you will work with a list of sales data, where each item is represented as a dictionary
containing information about a sale. Your task is to calculate the total sales amount using the `map` and
`reduce` functions.
Write Python functions to perform the following tasks:
1. **Extract Sales Amounts:** Create a function called `extract_sales_amounts` that takes a list of sale
dictionaries as input and returns a list containing only the sales amounts.
2. **Calculate Total Sales:** Create a function called `calculate_total_sales` that takes a list of sales
amounts as input and uses the `reduce` function to calculate the total sales amount."""

from functools import reduce

def extract_sales_amounts(sales_data):
    """
    Estrae gli importi delle vendite da una lista di dizionari di vendita.

    Args:
    sales_data (list): Una lista di dizionari, ciascuno contenente informazioni sulla vendita.

    Returns:
    list: Una lista di importi delle vendite.
    """
    # Usa map per creare una nuova lista contenente solo gli importi delle vendite
    return list(map(lambda sale: sale['amount'], sales_data))

def calculate_total_sales(sales_amounts):
    """
    Calcola l'importo totale delle vendite da una lista di importi delle vendite.

    Args:
    sales_amounts (list): Una lista di importi delle vendite.

    Returns:
    float: L'importo totale delle vendite.
    """
    # Usa reduce per sommare tutti gli importi delle vendite, partendo da 0
    return reduce(lambda total, amount: total + amount, sales_amounts, 0)

# Esempio di dati di vendita
sales_data = [
    {'item': 'apple', 'amount': 10},
    {'item': 'banana', 'amount': 5},
    {'item': 'orange', 'amount': 7},
    {'item': 'grape', 'amount': 12},
]

# Estrai gli importi delle vendite
sales_amounts = extract_sales_amounts(sales_data)
print("Importi delle vendite:", sales_amounts)

# Calcola il totale delle vendite
total_sales = calculate_total_sales(sales_amounts)
print("Totale vendite:", total_sales)