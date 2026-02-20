import numpy as np
import pandas as pd
import utile as utl
from acp.ACP import ACP
import Grafice as g
from sklearn.preprocessing import StandardScaler


tabel = pd.read_csv('dataIN/EconomicIndicators_EU.csv', index_col=0)
print(tabel)

obsNume = tabel.index.values
print(obsNume, type(obsNume))
varNume = tabel.columns.values
print(varNume, type(varNume))

n = len(obsNume)
print('Nr. observatii:', n)
m = len(varNume)
print('Nr. variabile observate:', m)

X = tabel.values
print(X, type(X), X.shape)

X = utl.inlocuireNAN(X)
X_df = pd.DataFrame(data=X, index=obsNume, columns=varNume)
X_df.to_csv('dataOUT/ACP_X.csv')

scaler = StandardScaler()
X_std = scaler.fit_transform(X)
X_std_df = pd.DataFrame(data=X_std, index=obsNume, columns=varNume)
X_std_df.to_csv('dataOUT/ACP_X_std.csv')

modelACP = ACP(X)

R = modelACP.getCorr()
R_df = pd.DataFrame(data=R, index=varNume, columns=varNume)
R_df.to_csv('dataOUT/ACP_Corelatie.csv')
print('Matricea de corelatie:')
print(R_df)

valProp = modelACP.getValProp()
print('Valori proprii:', valProp)

varExpl, varCum = utl.calcul_varianta_explicata(valProp)
print('Varianta explicata:', varExpl)
print('Varianta cumulata:', varCum)

valProp_df = utl.creare_dataframe_valori_proprii(valProp, varExpl, varCum)
valProp_df.to_csv('dataOUT/ACP_ValoriProprii.csv', index=False)
print(valProp_df)

nrCompKaiser = utl.numar_componente_kaiser(valProp)
print('Numar componente (criteriul Kaiser):', nrCompKaiser)

Rxc = modelACP.getRxc()
Rxc_df = pd.DataFrame(data=Rxc, index=varNume,
                      columns=['C'+str(i+1) for i in range(m)])
Rxc_df.to_csv('dataOUT/ACP_CorelatiFactoriale.csv')
print('Corelatii factoriale:')
print(Rxc_df)

scoruri = modelACP.getScoruri()
scoruri_df = pd.DataFrame(data=scoruri, index=obsNume,
                          columns=['C'+str(i+1) for i in range(m)])
scoruri_df.to_csv('dataOUT/ACP_Scoruri.csv')
print('Scoruri:')
print(scoruri_df)

comun = modelACP.getComun()
comun_df = pd.DataFrame(data=comun, index=varNume,
                        columns=['C'+str(i+1) for i in range(m)])
comun_df.to_csv('dataOUT/ACP_Comunalitati.csv')
print('Comunalitati:')
print(comun_df)

calObs = modelACP.getCalObs()
calObs_df = pd.DataFrame(data=calObs, index=obsNume,
                         columns=['C'+str(i+1) for i in range(m)])
calObs_df.to_csv('dataOUT/ACP_CalitateObs.csv')
print('Calitatea reprezentarii observatiilor:')
print(calObs_df)

betha = modelACP.getBetha()
betha_df = pd.DataFrame(data=betha, index=obsNume,
                        columns=['C'+str(i+1) for i in range(m)])
betha_df.to_csv('dataOUT/ACP_ContributiiObs.csv')
print('Contributia observatiilor:')
print(betha_df)

g.corelograma(R2=R_df, titlu='Corelograma - Indicatori Economici UE')
g.valori_proprii(valori=valProp, titlu='Valori proprii - ACP Economic')
g.plot_varianta_cumulata(varianta=varCum, titlu='Varianta cumulata - ACP Economic')
g.cercul_corelatiilor(R2=Rxc_df, V1=0, V2=1, titlu='Cercul corelatiilor')
g.plot_scoruri(scoruri_df=scoruri_df, titlu='Reprezentare tari UE in spatiul C1-C2')
g.plot_comunalitati(comunalitati_df=comun_df, titlu='Comunalitati variabile economice')
g.afisare()
