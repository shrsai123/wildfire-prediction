# Next-Day Wildfire Spread Prediction  
**Course Project – Predicting Wildfire Spread Using Machine Learning**

---

## Overview

This repository presents the implementation and analysis of multiple machine learning models for predicting next-day wildfire spread using remote-sensing data. Our work builds upon the open-source dataset and benchmark framework provided in the paper by Huot et al. [1], which introduces the "Next Day Wildfire Spread" dataset. We reproduce the Random Forest and Logistic Regression baselines from the paper and extend the study by adding recurrent models (RNN, LSTM) and a CNN-based Autoencoder.

##  Project Scope

This project aims to:

1. Reproduce the benchmark results from the original paper.

2. Evaluate the performance of classical and deep learning models.

3. Analyze model sensitivity to different learning rates and batch sizes.

### Model Implemented

1. Logistic Regression (baseline model using scikit-learn)

2. Random Forest (based on [1], with hyperparameter tuning)

3. Recurrent Neural Network (RNN)

4. Long Short-Term Memory (LSTM)

5. Convolutional Autoencoder (CNN-AE)

Our additions extend the original study by exploring temporal dependencies (RNN/LSTM) and spatial encoding (CNN-AE), as well as assessing how learning rate and batch size affect model behavior.

### Dataset (via Google Drive)

To keep this repository lightweight, the TFRecord dataset (~3GB) is hosted on Google Drive.

```bash
python download_data_from_drive.py
```
You can also manually download the data from : [LINK](https://drive.google.com/file/d/1XYxfgKdmDp-l9TDobaaeMP0D4oWPdtVa/view?usp=sharing)

> Original dataset was published by Huot et al. [1] and made available via [Kaggle](https://www.kaggle.com/datasets/fantineh/next-day-wildfire-spread/data).

##  Installation

```bash
git clone https://github.com/<your-org>/wildfire-spread-prediction.git
cd wildfire-spread-prediction
pip install -r requirements.txt
```



## References
[1] Huot, F., Abid, A., Elsen, E., Li, D., Jain, S., Ermon, S., & Pavone, M. (2021).
Next Day Wildfire Spread: A Machine Learning Data Set to Predict Wildfire Spreading from Remote-Sensing Data.
arXiv preprint arXiv:2112.02447.(https://arxiv.org/abs/2112.02447)

This work heavily references the data pipeline and baseline models provided by Huot et al. All extensions and evaluations are built upon the public dataset and code released by the authors.

## Team Members
Submitted as part of CS6140 Machine Learning, Northeastern University.
1. Rishabh Gupta (gupta.risha@northeastern.edu)
2. Shreyas Sai Raman (raman.shr@northeastern.edu)
3. Zhen Wang (wang.zhen3@northeastern.edu)

## Project Report
Read the full project report here: [Project_Report](Project_Report.pdf)