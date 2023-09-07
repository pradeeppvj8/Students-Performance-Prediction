# Project Name
* Students Performance Prediction

#### Project Status: [Completed]

## Project Intro/Objective
The purpose of this project is to predict student's performance [Math Score] based on attributes like gender, race, parents education level etc.

### Methods Used
* Linear Regression
* Data Visualization

### Technologies
* Python
* Pandas, jupyter
* Sklearn
* Flask
* Dockers
* AWS ECR, AWS EC2
* Github runners


## Project Description
* The purpose of this project is to predict student's performance [Math Score] based on attributes like gender, race, parents education level , lunch type, status of test preparation course, reading and writing scores.
* The data has been taken from https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977
* As part of EDA we have tried to figure out which variables are true indicators of students performance.
* After trying various learning algorithms, Linear Regression has been used to perform students performance prediction in this project.
* This project has been dockorized and the settings are present in 'Dockerfile'.
* AWS ECR Repository was created to store our docker image.
* AWS EC2 Instance was created and was connected to the ECR repository.
* Github workflow and Github runner has been configured using main.yaml file. 
* The purpose of Github runner is to create a docker image for every push to git hub repository.
* Github runner and AWS EC2 instance are connected and whenever the github runner runs, the docker image is moved to ECR repository.
* The application has been deployed into EC2 instance and can be accessed using 'http://107.23.243.251:8080/predict' .


## Getting Started

1. Raw Data is kept in [notebooks\data\stud.csv].

2. Data Ingestion scripts are kept in [src\components\data_ingestion.py]
    
3. Data transformation scripts are kept in [src\components\data_transformation.py]

4. Model training scripts are kept in [src\components\model_trainer.py]

5. Docker configuration is kept in [Dockerfile]

6. Github workflow & runner configuration is kept in [.github\workflows\main.yaml]

## Featured Notebooks/Analysis/Deliverables
* notebooks\Student_Performance_Prediction_EDA.ipynb contains the EDA performed on the dataset.
* notebooks\Student_Performance_Prediction_Model_Training.ipynb contains the model training steps.
* src\pipeline\predict_pipeline.py is the prediction pipeline that is responsible for performing model predictions.
* src\pipeline\train_pipeline.py is the training pipeline that is responsible for training the model.

## Contact
* Name :- Pradeep.P 
* Mobile :- 8197607412
* Email :- pradeep.pvj8@gmail.com
