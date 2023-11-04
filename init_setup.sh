echo [$(date)]: "START"
echo [$(date)]: "creating env with python 3.8 version"
python -m venv env 
echo [$(date)]: "activating the eneviornment"
source env/Scripts/activate
echo [$(date)]: "installing the dev requirements"
pip install -r requirements.txt
echo [$(date)]: "END"