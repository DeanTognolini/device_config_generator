# device_config_generator
Generates network device configurations using Jinja2 templates.

Input the variable information into the XLSX and run `rendered.py`.

# Requirements
See requirements.txt

# Usage

## PowerShell
```shell
git clone https://github.com/shamske/device_config_generator
cd device_config_generator
./pyenv/Scripts/activate.ps1
pip install -r requirements.txt
python renderer.py  
```

## Bash
```shell
git clone https://github.com/shamske/device_config_generator
cd device_config_generator
python -m venv device_config_generator
pip install -r requirements.txt
python renderer.py  
```
