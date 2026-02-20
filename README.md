# EU PCA & EFA Socio-Economic Analysis

## 📊 Project Overview

This project applies multivariate statistical methods to analyze the economic and educational performance of European Union Member States.

Using:
- **Principal Component Analysis (PCA)** for economic indicators
- **Exploratory Factor Analysis (EFA)** for educational indicators

The project aims to identify latent dimensions, reduce data dimensionality, and evaluate structural strengths and vulnerabilities across EU countries.

---

## 🎯 Objectives

- Identify latent dimensions that characterize EU economies
- Reduce dimensionality for clearer interpretation
- Classify EU countries based on economic and educational performance
- Validate the adequacy of data for multivariate analysis
- Provide a structured perspective on EU resilience in a geopolitical context

---

## 📂 Data Sources

All data were obtained from **Eurostat**, the statistical office of the European Union:

1. Macroeconomic Imbalance Procedure (MIP) Scoreboard  
2. Education and Training Database  

Reference period: 2022–2024  
Coverage: 27 EU Member States

---

## 📈 Methodology

### 1️⃣ Principal Component Analysis (PCA)

Applied to 10 economic indicators, including:
- GDP per capita
- Unemployment rate
- Inflation rate
- Public debt
- Current account balance
- FDI inflows
- R&D expenditure
- Labor productivity
- Export and import growth

Steps:
- Data standardization (z-score)
- Correlation matrix computation
- Eigenvalue decomposition
- Kaiser criterion for component selection
- Factor loadings and score interpretation

Results:
- 4 principal components retained
- 88% of total variance explained
- Identified dimensions:
  - General economic development
  - Macroeconomic stability
  - Investment attractiveness
  - Trade dynamics

---

### 2️⃣ Exploratory Factor Analysis (EFA)

Applied to 12 educational indicators, including:
- Early school leaving
- Tertiary education attainment
- NEET rate
- Graduate employment rate
- Early childhood education participation
- Adult learning participation
- Public education expenditure
- PISA low performance indicators

Adequacy tests:
- Bartlett’s Test of Sphericity (significant)
- KMO = 0.695 (acceptable sampling adequacy)

Results (after Varimax rotation):
- 4 latent factors identified:
  - Educational performance
  - Investment in education
  - Educational participation
  - Transition to labor market

---

## 🔎 Key Findings

- Economically advanced countries tend to display strong educational performance and higher resilience.
- Structural economic and educational weaknesses may indicate vulnerability to external shocks.
- Multivariate analysis provides a clearer understanding of underlying patterns than individual indicators alone.

---

## 🛠 Technologies Used

- Python
- pandas
- numpy
- scikit-learn
- factor_analyzer
- matplotlib
- seaborn

---

## 📚 References

- Hair, J. F. et al. (2019). *Multivariate Data Analysis*. Cengage Learning.
- Tabachnick, B. G. & Fidell, L. (2018). *Using Multivariate Statistics*. Pearson.
- Eurostat Databases

---

## 👥 Authors

Grigoras  
Gidea  

Academic Year: 2024–2025  
Group: 1086

---

## 📌 License

This project is developed for academic purposes.
