# CHICKEN_INVADERS
# A simple game that we all used to play when we were a kid

![Demo](https://user-images.githubusercontent.com/74227710/160250383-0b7fc92e-b22a-43c7-a678-cddf23481968.mov)

# 1. Install pip, python

### If you already installed python(any versions), please ignore this step:
```
sudo apt-get install python3
```
* Then, verify Installation and check pip and python version:
```
python3 --version
pip3 -V

```
### Install virtual environtment
* Install virtualenv
```
sudo pip3 install virtualenv
```
* Create a directory to store env
```
mkdir environments
cd environments
```
* Create a virtual environment
```
virtualenv chicken
```
* Activate virtual environment
```
cd chicken
source bin/activate
```
* Then go back to the root
```
cd 
```
# 2. Clone the project
* Make sure you have git installed by checking its version:
```
git --version 
```
* You can view your default Git configuration options with the following command:
```
git config -h
```
* Clone the project:
```
git clone https://github.com/phuongngo2904/CHICKEN_INVADERS.git
```
* Navigate to this project 
```
cd CHICKEN_INVADERS
```
# 3.  Install requirements
```
pip3 install -r requirements.txt
```
# 4. Run the game
```
python3 main.py
```
