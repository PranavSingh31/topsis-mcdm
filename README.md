## Topsis_Pranav_102003432

# TOPSIS

Submitted By: **Pranav Singh - 102003432**.

Type: **Package**.

Title: **TOPSIS method for multiple-criteria decision making (MCDM)**.

Version: **1.0.0**.

Date: **2022-01-22**.

Author: **Pranav Singh**.

Maintainer: **Pranav Singh <psingh2_be20@thapar.edu>**.

Description: **Evaluation of alternatives based on multiple criteria using TOPSIS method.**.

---

live link : https://pypi.org/project/Topsis-Pranav-102003432/

---

## What is TOPSIS?

**T**echnique for **O**rder **P**reference by **S**imilarity to **I**deal **S**olution
(TOPSIS) originated in the 1980s as a multi-criteria decision making method.
TOPSIS chooses the alternative of shortest Euclidean distance from the ideal solution,
and greatest distance from the negative-ideal solution.

<br>

## How to install this package:

```
>> pip install Topsis-Pranav-102003432
```

### In Command Prompt

```
>> topsis data.csv "1,1,1,1,1" "+,+,-,+,-" result.csv
```

## Input file (data.csv)

The decision matrix should be constructed with each row representing a Model alternative, and each column representing a criterion like Accuracy, R<sup>2</sup>, Root Mean Squared Error, Correlation, and many more.

| Model |     P1      | P2 | P3 | P4 | P5 |
| ----- | ----------- | ------------- | ---- | -------- | ---- |
| M1    | 0.7       | 0.5        | 7 | 37    | 11.3 |
| M2    | 0.8        | 0.6          | 7 | 46    | 13.4 |
| M3    | 0.7       | 0.5          | 7 | 48    | 14 |
| M4    | 0.9        | 0.8          | 7 | 44    | 13.2 |
| M5    | 0.9        | 0.9          | 5  | 37    | 11.1 |
| M6    | 0.9        | 0.6          | 3  | 67    | 18 |
| M7    | 0.9        | 0.5          | 7  | 39    | 11.8 |
| M8    | 0.9        | 0.9          | 5  | 46    | 13.2 |

Weights (`weights`) is not already normalised will be normalised later in the code.

Information of benefit positive(+) or negative(-) impact criteria should be provided in `impacts`.

<br>

## Output file (result.csv)

| Model |     P1      | P2 | P3 | P4 | P5 | Topsis Score | Rank |
| ----- | ----------- | ------------- | ---- | -------- | ---- |-----| ----|
| M1    | 0.7       | 0.5        | 7 | 37    | 11.3 | 0.28016 | 5 |
| M2    | 0.8        | 0.6          | 7 | 46    | 13.4 | 0.8292 | 1 |
| M3    | 0.7       | 0.5          | 7 | 48    | 14 | 0.17536 | 8 |
| M4    | 0.9        | 0.8          | 7 | 44    | 13.2 | 0.25 | 7 |
| M5    | 0.9        | 0.9          | 5  | 37    | 11.1 | 0.56483 | 3 |
| M6    | 0.9        | 0.6          | 3  | 67    | 18 | 0.27313 | 6 |
| M7    | 0.9        | 0.5          | 7  | 39    | 11.8 | 0.55075 | 4 |
| M8    | 0.9        | 0.9          | 5  | 46    | 13.2 | 0.65029 | 2 |

<br>
The output file contains columns of input file along with two additional columns having `Topsis_score` and `Rank`.
