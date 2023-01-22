import pandas as pd
from jinja2 import Template

# Read data from XLS file
data = pd.read_excel('config_data.xlsx')

# Open and read the template file
with open('ios_template.j2') as f:
    template_str = f.read()

# Compile the template
template = Template(template_str)

# Iterate through rows in dataframe
for index, row in data.iterrows():
    # Assign variables from XLS data
    hostname = row['hostname']
    ip_address = row['ip_address']
    subnet_mask = row['subnet_mask']
    default_gateway = row['default_gateway']

    # Use template to generate configuration
    config = template.render(hostname=hostname, ip_address=ip_address,
                             subnet_mask=subnet_mask, default_gateway=default_gateway)

    # Write configuration to file
    with open(f"{hostname}.cfg", "w") as f:
        f.write(config)
