#!/usr/bin/env python3
# You should be able to run this to mimic what VS code will do for you to create the venv

import os
import subprocess

def create_environment(environment_path, requirements_file):
    os.makedirs(environment_path, exist_ok=True)
    subprocess.run(['python', '-m', 'venv', environment_path], check=True)
    activate_script = os.path.join(environment_path, 'Scripts', 'activate.bat')
    with open(activate_script, 'r') as f:
        activate_contents = f.read()
    with open(activate_script, 'w') as f:
        f.write('#!/usr/bin/env bash\n')
        f.write(f'source {activate_contents}\n')
        f.write(f'python -m pip install -r {requirements_file}\n')

create_environment('.venv', 'requirements.txt')
