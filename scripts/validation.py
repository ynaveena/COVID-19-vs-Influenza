import sys
import pickle
import pandas as pd
import sklearn.metrics as skm

models = ['3Class', 'CPosvCNeg', 'FvOthers', 'FvC']
if len(sys.argv) > 1:
  if sys.argv[1] == '--help':
    help = '''Usage: python scripts/validation.py [MODELS]

    [MODELS] can be empty or a space-separated list containing:
      * 3Class    : Influenza vs COVID-19 Positive vs COVID-19 Negative
      * CPosvCNeg : COVID-19 Negative vs COVID-19 Positive
      * FvOthers  : Others vs Influenza
      * FvC       : Influenza vs COVID-19
    '''
    print(help)
    sys.exit(0)
  models = list(sys.argv)

print('Validating models...\n')

for model in models:
  title = f"{model} Validation"
  title += '\n' + '-' * len(title)
  print(title)
  data = pd.read_csv(f"data/{model}_Sample_Validation.csv")
  model = pickle.load(open(f"models/{model}.pkl", 'rb'))
  print(skm.classification_report(
      data['Class'], model.predict(data.drop('Class', axis=1))))
