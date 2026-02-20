import numpy as np
import pandas as pd


def inlocuireNAN(X):
    medii_pe_coloane = np.nanmean(a=X, axis=0)
    pozitie = np.where(np.isnan(X))
    X[pozitie] = medii_pe_coloane[pozitie[1]]
    return X


def calcul_varianta_explicata(valori_proprii):
    varianta_totala = np.sum(valori_proprii)
    varianta_explicata = (valori_proprii / varianta_totala) * 100
    varianta_cumulata = np.cumsum(varianta_explicata)
    return varianta_explicata, varianta_cumulata


def numar_componente_kaiser(valori_proprii):
    return np.sum(valori_proprii >= 1)


def salvare_csv(df, cale):
    df.to_csv(cale)
    print('Salvat:', cale)


def creare_dataframe_valori_proprii(valori_proprii, varianta_explicata, varianta_cumulata):
    m = len(valori_proprii)
    df = pd.DataFrame({
        'Componenta': ['C' + str(i+1) for i in range(m)],
        'Valoare_proprie': valori_proprii,
        'Varianta_explicata': varianta_explicata,
        'Varianta_cumulata': varianta_cumulata
    })
    return df
