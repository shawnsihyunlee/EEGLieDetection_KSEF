# EEGLieDetection_KSEF
This is a project for KSEF which involves lie detection using deep learning and EEG data.

By: Shawn Lee, Youngjin Cho


## Prerequisites
The necessary libraries for this project are:

* Tensorflow (https://www.tensorflow.org/)
* Keras (which comes with Tensorflow)
* Matplotlib
* Numpy
* Pandas


## Data
The data is organized into two folders: data/alldata and data/subjectdata. The former holds all the data for all subjects, whereas the latter holds the data for each subject.

For each subject, there is a truth folder and a lie folder, each of which contains a truth.csv or lie.csv file with the entirety of the raw EEG data, and a times.txt file which holds the times when the subject was answering the question.

### Data collection
Each subject was asked a set of 10 questions twice, and was asked to tell the truth once and lie once. Each of these trials are in the truth and lie folder for each subject respectively.


## Deep learning model
The model is in the Final EEG Model iPython Notebook, and is documented with comments.
The model is an LSTM network with a Dense layer afterwards.

