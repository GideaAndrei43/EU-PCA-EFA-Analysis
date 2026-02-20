import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd


def corelograma(R2=None, dec=2, titlu='Corelograma', valMin=-1, valMax=1):
    plt.figure(num=titlu, figsize=(12, 8))
    plt.title(label=titlu, fontsize=12, verticalalignment='bottom', color='Blue')
    sb.heatmap(data=np.round(a=R2, decimals=dec), vmin=valMin, vmax=valMax,
               cmap='bwr', annot=True)


def intesitate_legaturi(matrice=None, dec=2, titlu='Intensitate legaturi', color='Oranges'):
    plt.figure(num=titlu, figsize=(12, 8))
    plt.title(label=titlu, fontsize=12, verticalalignment='bottom', color='Blue')
    sb.heatmap(data=np.round(a=matrice, decimals=dec), cmap=color, annot=True)


def cercul_corelatiilor(R2=None, V1=0, V2=1, dec=2, titlu='Cercul corelatiilor'):
    plt.figure(num=titlu, figsize=(10, 9))
    plt.title(label=titlu + ' intre ' + 'Componenta ' + str(V1+1) + ' si ' +
              'Componenta ' + str(V2+1), fontsize=12,
              verticalalignment='bottom', color='Green')
    theta = [t for t in np.arange(start=0, stop=2*np.pi, step=0.01)]
    x = [np.cos(t) for t in theta]
    y = [np.sin(t) for t in theta]
    plt.plot(x, y)
    plt.axhline(y=0, color='Green')
    plt.axvline(x=0, color='Green')

    if isinstance(R2, np.ndarray):
        plt.xlabel(xlabel='Componenta ' + str(V1+1), fontsize=10,
                  verticalalignment='top', color='Blue')
        plt.ylabel(ylabel='Componenta ' + str(V2+1), fontsize=10,
                   verticalalignment='top', color='Blue')
        plt.scatter(x=R2[:, V1], y=R2[:, V2], color='Red')
        for i in range(R2.shape[0]):
            plt.text(x=R2[i, V1], y=R2[i, V2], color='Black',
                s='(' + str(np.round(R2[i, V1], decimals=dec)) + ', ' +
                  str(np.round(R2[i, V2], decimals=dec)) + ')')
    elif isinstance(R2, pd.DataFrame):
        plt.xlabel(xlabel=R2.columns[V1], fontsize=10,
                  verticalalignment='top', color='Blue')
        plt.ylabel(ylabel=R2.columns[V2], fontsize=10,
                   verticalalignment='top', color='Blue')
        plt.scatter(x=R2.iloc[:, V1], y=R2.iloc[:, V2], color='Blue')
        for i in range(R2.index.size):
            plt.text(x=R2.iloc[i].iloc[V1], y=R2.iloc[i].iloc[V2], color='Black',
                        s=R2.index[i])
    else:
        raise Exception('R2 must be a pandas.DataFrame or numpy.ndarray')


def valori_proprii(valori, titlu='Valori proprii - varianta explicata'):
    plt.figure(num=titlu, figsize=(10, 6))
    plt.title(label=titlu, fontsize=12, verticalalignment='bottom', color='Blue')
    plt.xlabel(xlabel='Componente principale', fontsize=10,
               verticalalignment='top', color='Blue')
    plt.ylabel(ylabel='Valori proprii - varianta explicata', fontsize=10,
               verticalalignment='bottom', color='Blue')
    componente = ['C'+str(i+1) for i in range(valori.shape[0])]
    plt.plot(componente, valori, 'bo-')
    plt.axhline(y=1, color='Red')


def plot_varianta_cumulata(varianta, titlu='Varianta cumulata'):
    plt.figure(num=titlu, figsize=(10, 6))
    plt.title(label=titlu, fontsize=12, verticalalignment='bottom', color='Blue')
    plt.xlabel(xlabel='Componente principale', fontsize=10,
               verticalalignment='top', color='Blue')
    plt.ylabel(ylabel='Varianta cumulata (%)', fontsize=10,
               verticalalignment='bottom', color='Blue')
    componente = ['C'+str(i+1) for i in range(varianta.shape[0])]
    plt.bar(componente, varianta, color='SteelBlue', edgecolor='Navy')
    plt.axhline(y=80, color='Red', linestyle='--')


def plot_scoruri(scoruri_df, titlu='Scoruri observatii'):
    plt.figure(num=titlu, figsize=(12, 10))
    plt.title(label=titlu, fontsize=12, verticalalignment='bottom', color='Blue')
    plt.xlabel(xlabel='Componenta 1', fontsize=10, color='Blue')
    plt.ylabel(ylabel='Componenta 2', fontsize=10, color='Blue')
    plt.scatter(scoruri_df.iloc[:, 0], scoruri_df.iloc[:, 1], c='SteelBlue', s=80)
    for i in range(scoruri_df.shape[0]):
        plt.annotate(scoruri_df.index[i],
                    (scoruri_df.iloc[i, 0], scoruri_df.iloc[i, 1]),
                    xytext=(5, 5), textcoords='offset points', fontsize=8)
    plt.axhline(y=0, color='Gray', linestyle='--')
    plt.axvline(x=0, color='Gray', linestyle='--')


def plot_comunalitati(comunalitati_df, titlu='Comunalitati'):
    plt.figure(num=titlu, figsize=(12, 6))
    plt.title(label=titlu, fontsize=12, verticalalignment='bottom', color='Blue')
    plt.xlabel(xlabel='Variabile', fontsize=10, color='Blue')
    plt.ylabel(ylabel='Comunalitate', fontsize=10, color='Blue')
    variabile = comunalitati_df.index.tolist()
    valori = comunalitati_df.iloc[:, -1].values
    plt.bar(variabile, valori, color='Coral', edgecolor='DarkRed')
    plt.xticks(rotation=45, ha='right')
    plt.axhline(y=0.5, color='Red', linestyle='--')
    plt.tight_layout()


def afisare():
    plt.show()
