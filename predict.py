"""A pipeline test for haggle's Hour Detective, not a starting point: it guesses the median hours of train.csv
for every project. haggle runs it with train.csv and test.csv next to it, and it writes predictions.csv."""

import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

guess = train["hours_spent"].median()
pd.DataFrame({"project_id": test["project_id"], "hours_spent": guess}).to_csv("predictions.csv", index=False)
