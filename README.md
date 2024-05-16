0. download/unzip content of this repo into some working directory, or clone it using git 

git clone https://github.com/qwiglydee/otree-experiments/
cd otree-experiments

1. create and activate virtualenv in working directory

python -m venv .venv
cd .venv
cd scripts
activate

2. install requirements 
cd..
cd..
pip install --upgrade pip
pip install -r requirements.txt

3. run the development server
otree devserver
