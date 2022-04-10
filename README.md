# Robot_Portrait

## Description
This software helps you to identify a person with his face characteristics using the dataset celebA.

## Version
1.0.0

## Installation
Before trying to run this software ;
```
git clone https://github.com/leohermet1/Robot_Portrait.git
```
### To use Python Virtual Environment
```
cd Robot_Portrait/
#install Python virtualenv
pip3 install pipenv
# Activate Python virtualenv
pipenv shell
pipenv install -r ./requirements.txt
# Run 
python3 main.py
```

### If you don't want to use a Python Virtual Environment, make sure that you have all the following packages on your computer:
DEPENDENCIES:
+ `pip3 install tkinter`
+ `pip3 install Pillow`
+ `pip3 install keras`
+ `pip3 install tensorflow`
+ `pip3 install numpy`
+ `pip3 install sklearn.model_selection`
+ `pip3 install math`
+ `pip3 install base64`
+ `pip3 install pickle`
+ `pip3 install random`

#### Run
```
python3 main.py
```

## auto_encoder
In order to train the model proposed here we used : 
  - 10000 pictures from the celebA dataset https://mmlab.ie.cuhk.edu.hk/projects/CelebA.html 
  - 50 epochs

*For your information it took 2 hours to compute on a casual laptop (2022).*

You can modify the auto_encoder.py file in order to use another data set (line 35) or modify the number of epochs (line 129).
Then you can retrain the model by running :
```
python3 auto_encoder.py
```
It will automatically save your model and use it next time you run the main.py

## Documentations
To find all our documentation, you can either read directly the docstrings in the code of go to
```
Robot_Portrait/robot_portrait/docs/build/html
```
in your files and then click on the file 
```
index.htlm. 
```
It should open your web browser directly on the first of the documentation. You then just have to navigate inside to discover everything you need!

## Authors
Beugin Maëva, Dufeu Marion, Cho Chaeeun, Li Danlin, Jimenez Juan, Hermet Léo
