import numpy as np
import pandas as pd
import utile as utl
from aef.AEF import AEF
import factor_analyzer as fa
import Grafice as g
from sklearn.preprocessing import StandardScaler


tabel = pd.read_csv('dataIN/EducationIndicators_EU.csv', index_col=0)
print(tabel)

obsNume = tabel.index.values
print(obsNume, type(obsNume))
varNume = tabel.columns.values
print(varNume, type(varNume))

n = len(obsNume)
print('Nr. observatii:', n)
m = len(varNume)
print('Nr. variabile observate:', m)

X = tabel.values.astype(float)
print(X, type(X), X.shape)

X = utl.inlocuireNAN(X)
X_df = pd.DataFrame(data=X, index=obsNume, columns=varNume)
X_df.to_csv('dataOUT/AEF_X.csv')

scaler = StandardScaler()
X_std = scaler.fit_transform(X)
X_std_df = pd.DataFrame(data=X_std, index=obsNume, columns=varNume)
X_std_df.to_csv('dataOUT/AEF_X_std.csv')

sfericitate_Bartlett = fa.calculate_bartlett_sphericity(x=X_std)
print('Test Bartlett:', sfericitate_Bartlett)
if sfericitate_Bartlett[0] > sfericitate_Bartlett[1]:
    print('Exista cel putin un factor comun!')
else:
    print('Nu exista nici macar un factor comun!')

kmo = fa.calculate_kmo(x=X_std)
print('KMO:', kmo)
if kmo[1] > 0.5:
    print('Variabilele observate pot fi exprimate prin factori!')
else:
    print('Variabilele observate NU pot fi exprimate prin factori!')

kmo_individual = kmo[0]
kmo_df = pd.DataFrame(data=kmo_individual[:, np.newaxis], index=varNume, columns=['KMO'])
kmo_df.to_csv('dataOUT/AEF_KMO.csv')
print('Indici KMO individuali:')
print(kmo_df)

modelAEF = AEF(X)

R = modelAEF.getCorr()
R_df = pd.DataFrame(data=R, index=varNume, columns=varNume)
R_df.to_csv('dataOUT/AEF_Corelatie.csv')
print('Matricea de corelatie:')
print(R_df)

valProp = modelAEF.getValProp()
print('Valori proprii:', valProp)

varExpl, varCum = utl.calcul_varianta_explicata(valProp)
print('Varianta explicata:', varExpl)
print('Varianta cumulata:', varCum)

valProp_df = utl.creare_dataframe_valori_proprii(valProp, varExpl, varCum)
valProp_df.to_csv('dataOUT/AEF_ValoriProprii.csv', index=False)
print(valProp_df)

nrCompKaiser = utl.numar_componente_kaiser(valProp)
print('Numar factori (criteriul Kaiser):', nrCompKaiser)

Rxc = modelAEF.getRxc()
Rxc_df = pd.DataFrame(data=Rxc, index=varNume,
                      columns=['F'+str(i+1) for i in range(m)])
Rxc_df.to_csv('dataOUT/AEF_FactorLoadings.csv')
print('Factor Loadings:')
print(Rxc_df)

scoruri = modelAEF.getScoruri()
scoruri_df = pd.DataFrame(data=scoruri, index=obsNume,
                          columns=['F'+str(i+1) for i in range(m)])
scoruri_df.to_csv('dataOUT/AEF_Scoruri.csv')
print('Scoruri factoriale:')
print(scoruri_df)

comun = modelAEF.getComun()
comun_df = pd.DataFrame(data=comun, index=varNume,
                        columns=['F'+str(i+1) for i in range(m)])
comun_df.to_csv('dataOUT/AEF_Comunalitati.csv')
print('Comunalitati:')
print(comun_df)

calObs = modelAEF.getCalObs()
calObs_df = pd.DataFrame(data=calObs, index=obsNume,
                         columns=['F'+str(i+1) for i in range(m)])
calObs_df.to_csv('dataOUT/AEF_CalitateObs.csv')
print('Calitatea reprezentarii observatiilor:')
print(calObs_df)

nrFactori = nrCompKaiser
modelFA = fa.FactorAnalyzer(n_factors=nrFactori, rotation='varimax')
modelFA.fit(X_std)

loadings_rotite = modelFA.loadings_
loadings_rotite_df = pd.DataFrame(data=loadings_rotite, index=varNume,
                                   columns=['F'+str(i+1) for i in range(nrFactori)])
loadings_rotite_df.to_csv('dataOUT/AEF_LoadingsRotite.csv')
print('Factor Loadings dupa rotatie Varimax:')
print(loadings_rotite_df)

variance = modelFA.get_factor_variance()
variance_df = pd.DataFrame({
    'Factor': ['F'+str(i+1) for i in range(nrFactori)],
    'Varianta': variance[0],
    'Proportie': variance[1],
    'Cumulata': variance[2]
})
variance_df.to_csv('dataOUT/AEF_VariantaFactori.csv', index=False)
print('Varianta explicata de factori:')
print(variance_df)

comunalitati_fa = modelFA.get_communalities()
comunalitati_fa_df = pd.DataFrame(data=comunalitati_fa, index=varNume, columns=['Comunalitate'])
comunalitati_fa_df.to_csv('dataOUT/AEF_ComunalitatiFA.csv')
print('Comunalitati dupa rotatie:')
print(comunalitati_fa_df)

g.corelograma(R2=R_df, titlu='Corelograma - Indicatori Educationali UE')
g.intesitate_legaturi(matrice=kmo_df, titlu='Indici Kaiser-Meyer-Olkin')
g.valori_proprii(valori=valProp, titlu='Valori proprii - AEF Educational')
g.plot_varianta_cumulata(varianta=varCum, titlu='Varianta cumulata - AEF Educational')
g.cercul_corelatiilor(R2=Rxc_df, V1=0, V2=1, titlu='Cercul corelatiilor - Factori')
g.plot_scoruri(scoruri_df=scoruri_df, titlu='Reprezentare tari UE - Factori Educationali')
g.plot_comunalitati(comunalitati_df=comun_df, titlu='Comunalitati variabile educationale')
g.afisare()
