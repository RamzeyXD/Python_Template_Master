import os
import sys
import json
import subprocess
import time
import data_message


class Template():
    # JSON template object 

    def __init__(self):
        with open(os.path.join(sys.path[0], 'data.json'), 'r') as f:
            self.templates = json.load(f)

    def get_templates(self):
        return self.templates


def _save(data):
    # Save data to template

    with open(os.path.join(sys.path[0], 'data.json'), 'w') as f:
        json.dump(data, f)


def remove():
    # Remove template from data 

    template_name = input("Choose template name: ")

    templates = Template().get_templates()
    temp_template = templates

    for i in templates['templates']:
        if template_name == i:
            del temp_template['templates'][i]

            _save(temp_template)

            print(i, 'was removed')


def create():
    name = input("Choose template name: ")

    templates = Template().get_templates()
    _create_env()

    for i in templates['templates'][name]['packages']:
        _install(i)


def add():
    template_name = input("Add template name: ")

    temp = input("Add packages (split by ,): ")
    packages = temp.split(',')

    templates = Template().get_templates()

    templates['templates'][template_name] = {
        'packages': packages
    }
    
    _save(templates)


def edit():
    # Constructor func for edit template. Add new changes here

    template_name = input("Choose template name: ")
    print(data_message.edit_message)

    act = input("What you want to edit?: ")

    if act is 'N':
        _edit_name(template_name)
    elif act is 'P':
        _edit_packages(template_name)
    else:
        print("Action error")
        edit()


def _edit_name(template_name):
    templates = Template().get_templates()
    new_name = input("New name: ")

    temp_data = templates['templates'][template_name]['packages']
    del templates['templates'][template_name]

    templates['templates'][new_name] = temp_data

    _save(templates)

    print(f"Name was changed to {new_name}")


def _edit_packages(template_name):
    templates = Template().get_templates()

    temp_data = input("Add packages (split by ,): ")
    new_packages = temp_data.split(',')

    templates['templates'][template_name]['packages'] = new_packages

    _save(templates)

    print(f"Packages was changed to {temp_data}")





def _create_env():
    # Create a new virtual enviroment for future use

    os.system("virtualenv --python=python3 venv")           #create env and choose python3
    time.sleep(3)
    os.system(". venv/bin/activate")


def _install(package):
    # Private package install func.

    current_dir = os.getcwd()           # get real path to execute folder
    subprocess.check_call([str(current_dir) + "/venv/bin/python3", "-m", "pip", "install", package])
