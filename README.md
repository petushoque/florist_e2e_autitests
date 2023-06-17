# Create virtual environments

python -m venv ./environment

# Activate environment

./environment/Scripts/activate

# Install packages

pip install -r requirements.txt

# Produce a list of the installed packages

pip freeze > requirements.txt

# Run tests

pytest