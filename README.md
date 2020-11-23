# COVID-19 vs Influenza

This repository contains code and ML models used for distinguishing between COVID-19 and Influenza.

## Models

* Influenza vs COVID-19 Positive vs COVID-19 Negative
* COVID-19 Negative vs COVID-19 Positive
* Others vs Influenza
* Influenza vs COVID-19

## Data

The columns present in the dataset (in order) are:

* `sex_F` – 1 if Female, 0 if otherwise

* `race_White` – 1 if White, 0 otherwise

* `race_AA` – 1 if African American, 0 otherwise

* `race_Other` – 1 if neither White nor African American, 0 otherwise

* `ethnicity_Hispanic_YN` – 1 if Hispanic or Latino, 0 otherwise

* `Age` – Age in years (integer)

* `patient_class`

* `encounter_type`

* `reason_for_visit`

* `SBP` – Systolic BP

* `DBP` – Diastolic BP

* `Temp_C` – Temperature in ºC

* `HR` – Heart Rate

* `RR` – Respiratory Rate

* `SPO2` – Blood Oxygen (SpO_2)

* `BMI`

* `BSA`

* `Month` – Month (integer) 0 - 11

* `Class` – Ground Truth

## Instructions

To run the code, ensure you have Python installed. All our code was written in Python 3.8.0, but should be backwards-compatible to some earlier versions of Python 3. Follow the instructions below to get started.

### Clone or Download Repository

Clone the repository by running this command.

```bash
git clone https://github.com/ynaveena/COVID-19-vs-Influenza
```

You may also just download the repository from GitHub.

### Requirements

To install all requirements, simply run this in the Terminal.

```bash
pip install -r requirements.txt
```

Note: On some systems, you may have to use `pip3` instead.

### Jupyter Notebooks

Additionally, to run our notebooks, you need to have Jupyter Notebook installed. You can do this using the command below.

```bash
pip install jupyter
```

Note: On some systems, you may have to use `pip3` instead.

### Running the Code

To use the notebooks, simply start up a Jupyter server using the command below.

```bash
jupyter notebook
```

Our code is also available as Python scripts. To use them, follow the instructions below.

#### Sample Validation

Run the command given below from the root of the repository to validate the models on sample data.

```bash
python scripts/validation.py [MODELS]
# For help: python scripts/validation.py --help
```

`[MODELS]` can either be empty (this would mean all 4 models are validated) or a space-separated list of specific models to validate. The arguments can be specified as follows:

* `3Class` – Influenza vs COVID-19 Positive vs COVID-19 Negative

* `CPosvCNeg` – COVID-19 Negative vs COVID-19 Positive

* `FvOthers` – Others vs Influenza

* `FvC` – Influenza vs COVID-19

## Citation

If you use the code and models provided in this repository, please do cite us.

```
@misc{covid19vsinfluenza,
  title = {COVID 19 vs Influenza},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/ynaveena/COVID-19-vs-Influenza}}
}
```
