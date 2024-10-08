"""Group the indexes of the elements with the same value as the following example using map and reduce:
input: L = [12, 34, 35, 12, 99, 34, 34, 12, 34, 12]
output: G = {12: [0,3,7,9], 34: [1,5,6,8], 99:[4], 35:[2]}"""

from functools import reduce

def group_indexes(L):
    """
    Raggruppa gli indici degli elementi con lo stesso valore in un dizionario.

    Args:
    L (list): Una lista di valori.

    Returns:
    dict: Un dizionario con i valori come chiavi e le liste degli indici come valori.
    """
    # Usa reduce per creare un dizionario di indici
    return reduce(
        lambda acc, idx: acc.setdefault(L[idx], []).append(idx) or acc,
        range(len(L)),
        {}
    )

# Esempio di input
L = [12, 34, 35, 12, 99, 34, 34, 12, 34, 12]

# Raggruppa gli indici
G = group_indexes(L)

print("Output:", G)