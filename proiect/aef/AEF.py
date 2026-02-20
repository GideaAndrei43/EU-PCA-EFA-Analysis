import numpy as np
from acp.ACP import ACP
import scipy.stats as sts


class AEF:

    def __init__(self, matrice):
        self.X = matrice

        acpModel = ACP(self.X)
        self.Xstd = acpModel.getXstd()
        self.Corr = acpModel.getCorr()
        self.ValProp = acpModel.getValProp()
        self.Scoruri = acpModel.getScoruri()
        self.CalObs = acpModel.CalObs
        self.Rxc = acpModel.getRxc()
        self.Comun = acpModel.getComun()

    def getXstd(self):
        return self.Xstd

    def getCorr(self):
        return self.Corr

    def getValProp(self):
        return self.ValProp

    def getRxc(self):
        return self.Rxc

    def getScoruri(self):
        return self.Scoruri

    def getCalObs(self):
        return self.CalObs

    def getComun(self):
        return self.Comun

    def calculTestBartlett(self, loadings, epsilon):
        n = self.X.shape[0]
        m, q = np.shape(loadings)
        V = self.Corr
        psi = np.diag(epsilon)
        Vestim = loadings @ np.transpose(loadings) + psi
        Iestim = np.linalg.inv(Vestim) @ V
        detIestim = np.linalg.det(Iestim)
        if detIestim > 0:
            traceIestim = np.trace(Iestim)
            chi2Calc = (n - 1 - (2*m - 4*q - 5) / 6) * \
                       (traceIestim - np.log(detIestim) - m)
            numarGradeLibertate = ((m - q)**2 - m - q) / 2
            chi2Tab = 1 - sts.chi2.cdf(chi2Calc, numarGradeLibertate)
        else:
            chi2Calc, chi2Tab = np.nan, np.nan

        return chi2Calc, chi2Tab
