"""Create a function called `group_and_sum` that takes a list of tuples as input. Each tuple contains a key (a string) and a value
(a number). The function should group the values by their keys and calculate the sum of values for each key. The result should be a dictionary where
keys are the unique keys from the input, and values are the sums of values associated with each key.
Students should complete the missing part of the following template in the `group_and_sum` function to implement the `groupby` operation using the
`map` and `reduce` functions. This exercise will help them practice combining these functional programming concepts to perform data aggregation
operations."""

from functools import reduce

def group_and_sum(data):
    # Utilizzo reduce per aggregare i valori in base alle loro chiavi
    # 'pairs' è una lista di tuple dove ogni tupla contiene una chiave e un valore
    grouped = reduce(
        # La funzione lambda che elabora ogni (accumulatore, coppia attuale)
        lambda acc, pair: (
            # Aggiorna il dizionario accumulatore con la chiave e il valore della coppia attuale
            acc.update({pair[0]: acc.get(pair[0], 0) + pair[1]}) or acc
        ), 
        # La lista di input di tuple
        data, 
        # Inizializza l'accumulatore come un dizionario vuoto
        {}
    )
    
    # Restituisce i risultati aggregati sotto forma di dizionario
    return grouped

# Esempio di utilizzo:
pairs = [('apple', 10), ('banana', 5), ('apple', 15), ('orange', 7), ('banana', 3)]
result = group_and_sum(pairs)

# Stampa il risultato: i totali per ogni chiave
print(result)