# haggle test ship

A test of the ship pipeline for [haggle](https://haggle.hackclub.com)'s Week 1, Hour Detective. It is not a model to learn from: it guesses the same number (the median of `train.csv`) for every project, which scores about 0.97 RMSLE.

## Run it

1. Put `train.csv` from the Data tab next to `predict.py`.
2. Save a few rows of `train.csv` without `hours_spent`, `log_hours` and `hours_bucket` as `test.csv`.
3. `python predict.py` writes `predictions.csv` with `project_id,hours_spent`.

Needs Python 3 and pandas.
