# Obesity Weight-Class Prediction – ML Model + Flask API

Ett komplett maskininlärningsflöde: dataanalys i Jupyter, modellträning (flera metoder), 
och till slut ett REST API byggt med Flask.

## Projektmål
Förutsäga en persons **viktklass** (t.ex. Normal_Weight, Overweight_Level_I, Obesity_Type_I, etc.)

## Dataset
`ObesityDataSet_raw_and_data_sinthetic.csv`  
syntetiskt dataset med 17 variabler relaterade till livsstil, hälsa och kost.

Målvariabel: `NObeyesdad` med 7 klasser:  
`Insufficient_Weight`, `Normal_Weight`, `Overweight_Level_I`, `Overweight_Level_II`,  
`Obesity_Type_I`, `Obesity_Type_II`, `Obesity_Type_III`.

## Modellval och metod
Flera modeller jämfördes:
- Logistic Regression  
- Random Forest  
- Gradient Boosting  
- **XGBoost (bäst resultat)**  

Preprocessing via `ColumnTransformer`:  
- StandardScaler på numeriska kolumner  
- OneHotEncoder på kategoriska kolumner  
- LabelEncoder på målvariabeln  

## Utvärdering (exempelresultat)
| Modell | Accuracy | Precision | Recall | F1 |  
|---------|-----------|-----------|--------|----|  
| Logistic Regression | 0.875 | 0.872 | 0.875 | 0.873 |  
| Random Forest | 0.936 | 0.935 | 0.936 | 0.935 |  
| Gradient Boosting | 0.950 | 0.949 | 0.950 | 0.950 |  
| **XGBoost** | **0.960** | **0.959** | **0.960** | **0.959** |

Vald slutmodell: `XGBoost` (sparad som `models/basta_pipeline.pkl`).  
Klassnamn sparas i `models/klasser.pkl`.

## Projektstruktur

