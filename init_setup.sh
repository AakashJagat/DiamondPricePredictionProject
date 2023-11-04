echo [$(date)]: "creating env  with python 3.8 version"
python -m venv env
echo [$(date)]: "activating the environment"
source env/Scripts/activate
echo [$(date)]: "installinng the requirements"
pip install -r requirements.txt
echo [$(date)]: "END"
