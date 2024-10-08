# PIPELINE, CONTARE 0-30 31-50 51-90 DAL FILE ANAGRAFICA_PERSONE.CSV E FARNE LA MEDIA
import csv

# Definisco contatori
count_0_30 = 0
count_31_50 = 0
count_51_90 = 0
somma_0_30 = 0
somma_31_50 = 0
somma_51_90 = 0

# Vado a leggere il file csv
with open('anagrafica_persone.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader) # Salta l'intestazione
    for row in reader:
        età = int(row[3])  # Dato che l'età si trova nella quarta colonna

        # Controllo l'età e aggiorno i contatori e le somme
        if 0 <= età <= 30:
            count_0_30 += 1
            somma_0_30 += età
        elif 31 <= età <= 50:
            count_31_50 += 1
            somma_31_50 += età
        elif 51 <= età <= 90:
            count_51_90 += 1
            somma_51_90 += età

# Calcolo le medie per ciascuna fascia
media_0_30 = somma_0_30 / count_0_30 if count_0_30 > 0 else 0
media_31_50 = somma_31_50 / count_31_50 if count_31_50 > 0 else 0
media_51_90 = somma_51_90 / count_51_90 if count_51_90 > 0 else 0


print(f"Persone con età tra 0-30: {count_0_30}, Media età: {media_0_30:.2f}")
print(f"Persone con età tra 31-50: {count_31_50}, Media età: {media_31_50:.2f}")
print(f"Persone con età tra 51-90: {count_51_90}, Media età: {media_51_90:.2f}")