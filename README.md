# device_config_generator
Generates network device configurations using Jinja2 templates.

Input the variable information into the XLSX and run `rendered.py`.

# Requirements
See requirements.txt

# Usage
1.  Clone the repository:

```bash
git clone https://github.com/DeanTognolini/device_config_generator
```

2.  Change the directory to the cloned repository:

```bash
cd device_config_generator
```
3.  Create a virtual environment:

For PowerShell:
```powershell
python -m venv venv .\venv\Scripts\Activate.ps1
```

For Bash:

```bash
python -m venv venv
source venv/bin/activate
```

4.  Install the required packages:
`pip install -r requirements.txt`

5.  Input the variable information into a new file named `config_data.xlsx` in the same folder as `renderer.py`. The `config_data.xlsx` file should have the following columns: `hostname`, `ip_address`, `subnet_mask`, and `default_gateway`.
    
6.  Run the `renderer.py` script to generate the device configurations:

`python renderer.py`

After running the script, you will find the generated configuration files in the same directory, with filenames in the format `<hostname>.cfg`.
