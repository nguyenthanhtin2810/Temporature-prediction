<p align="center">
 <h1 align="center">Temporature prediction</h1>
</p>

## Introduction
In this project, I employ time series analysis techniques to predict temperature values. By analyzing historical temperature data, I aim to create a model that can provide accurate temperature forecasts.

## Dataset
I use a dataset containing historical temperature records. You can find the dataset at file 'temperature.csv'.

<a name="sample"></a>

|Time|Temperature|   
|----|:---------:|
|2011-12-31T13:00:00Z|21.4|
|2011-12-31T13:30:00Z|21.05|
|2011-12-31T14:00:00Z|20.7|
|2011-12-31T14:30:00Z|20.55|
|2011-12-31T15:00:00Z|20.4|
|2011-12-31T15:30:00Z|20.25|
|2011-12-31T16:00:00Z|20.1|
|2011-12-31T16:30:00Z|19.6|
|2011-12-31T14:30:00Z|19.1|
|2011-12-31T15:00:00Z|18.95|

## Method

### Recursive Time Series Forecasting
In the Recursive Time Series Forecasting method, I use historical temperature data to predict future values one step at a time.

A recursive dataset with a window size of 5 from this dataset from [this dataset](#sample)

### Direct Time Series Forecasting
In the Direct Time Series Forecasting method, I utilize historical temperature data to directly predict multiple future values in a single step. (using multiple models)

## Requirements
* python
* pandas
* sklearn
* matplotlib
