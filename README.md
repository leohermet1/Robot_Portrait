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
# Activate Python virtualenv
pipenv shell
pipenv install -r ./requirements.txt
# Extract image dataset
cd robot_portrait/
gzip -d celebA_10000.zip
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
cd robot_portrait/
gzip -d celebA_10000.zip (The datasets of pictures)
python3 main.py
```

### auto_encoder
If you want to re-train the model, you can run the auto_encoder.py with this code:
```
python3 auto_encoder.py
```
In this code you can modify the number of epochs at the line 129.


## Authors
Beugin Maëva, Dufeu Marion, Cho Chaeeun, Hermet Léo, Li Danlin, Jimenez Juan
