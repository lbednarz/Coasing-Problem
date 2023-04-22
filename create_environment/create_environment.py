import os
import subprocess

def create_environment(environment_name, requirements_file):
    conda_env_create_command = f'conda create --name {environment_name} --file {requirements_file}'
    subprocess.run(conda_env_create_command.split(), check=True)

    with open(requirements_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                if line.startswith('conda'):
                    subprocess.run(line.split(), check=True)
                else:
                    subprocess.run([f'conda run -n {environment_name}', 'pip', 'install', line], check=True)

create_environment('my_conda_env', 'requirements.txt')

