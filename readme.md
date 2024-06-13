# Workshop Repository

## Overview
Welcome to the Workshop Repository! This collection of Jupyter notebooks and scripts is designed to showcase how to develop and deploy a machine learning system, in a few hours. It follows the general pattern of the FTI pipelines (feature,training,inference)

## Repository Structure
- **busyness_model/**: Houses the model registry and related scripts for business analytics.
- **functions/**: Contains utility functions and scripts to enhance model functionality.
- **Main Notebooks**:
  - **`1- Feature Pipeline - Foot Traffic Data and Feature Store.ipynb`**: Feature engineering with foot traffic data from bestTime.
  - **`2- Training Pipeline - Bar Busyness Model.ipynb`**: Trains machine learning models.
  - **`3- Inference Pipeline - Inference and Function Calling.ipynb`**: Inference and function calling mechanisms.

## What you will learn
- **Feature Engineering**: State-of-the-art usage of the feature store for manipulating data as dataframe.
- **Model Training**: Easily train, evaluate, and optimize machine learning model.
- **Embeddings**: A bit of LLMs
- **Inference Pipelines**: Integrate model inference
- **real-time stuff** A real-time ML System.

## Prerequisites
- A free [Hopsworks account](https://app.hopsworks.ai)
- A free [BestTime account](https://besttime.app/)

## Requirements
To get started, clone the repository and install the necessary dependencies:
```bash
pip install -r requirements.txt
```

## Main Dependencies
```bash
langchain-community==0.0.38
langchain-core==0.1.52
xgboost==2.0.3
transformers==4.38.2
protobuf==3.20.0
langchain==0.1.10
streamlit==1.31.1
sentencepiece==0.2.0
gradio==4.21.0
torch==2.3.1
pandas==2.1.4
hopsworks==3.7.0
seaborn==0.13.2
```

## Usage
Clone the repository :) 
