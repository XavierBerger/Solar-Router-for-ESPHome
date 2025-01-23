#!/bin/env python3
"""
Convert configuration using remote to local conf
"""

import os

import yaml


# Manage !secret key ---------------------------------------------------------------------------------------------------
class SecretTag:
    """class dedicated to add !secret"""

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"SecretTag(value={self.value!r})"


def secret_constructor(_, node):
    """Manage !secret key"""
    return SecretTag(node.value)


def secret_representer(dumper, data):
    """Sérialiser les instances de SecretTag avec la balise !secret"""
    return dumper.represent_scalar("!secret", data.value)


yaml.add_constructor("!secret", secret_constructor)
yaml.add_representer(SecretTag, secret_representer)


# Manage !include key --------------------------------------------------------------------------------------------------
class IncludeTag:
    """class dedicated to add !include"""

    def __init__(self, filename, vars_values=None):
        self.file = filename
        self.vars = vars_values

    def __repr__(self):
        return f"{self.__class__.__name__}(file={self.file!r}, vars={self.vars!r})"


def include_constructor(loader, node):
    """Manage !include key"""
    data = loader.construct_mapping(node)
    return IncludeTag(**data)  # Return as IncludeTag for proper dumping


def include_representer(dumper, data):
    # Construire un mapping contenant uniquement les champs non vides
    mapping = {"file": data.file}
    if data.vars:  # Ajouter `vars` uniquement s'il n'est pas vide
        mapping["vars"] = data.vars
    node = dumper.represent_mapping("!include", mapping)
    return node


yaml.add_constructor("!include", include_constructor)
yaml.add_representer(IncludeTag, include_representer)


# ----------------------------------------------------------------------------------------------------------------------
def load_yaml_with_custom_constructors(file_path):
    """Use custom loader"""
    with open(file_path, "r", encoding="UTF-8") as file:
        data = yaml.load(file, Loader=yaml.Loader)  # Utilise le loader personnalisé
    return data


def get_package_name(filepath):
    """Extract package name from filename"""
    filename = os.path.basename(filepath)
    name, _ = os.path.splitext(filename)
    return name


def process_yaml_file(yaml_file):
    """Convert yaml file"""
    config = load_yaml_with_custom_constructors(yaml_file)
    if "solar_router" in config["packages"]:
        if "files" in config["packages"]["solar_router"]:
            for item in config["packages"]["solar_router"]["files"]:
                package_name = get_package_name(item["name"])
                config["packages"][package_name] = IncludeTag(filename=item["name"])
                if "vars" in item:
                    config["packages"][package_name].vars = item["vars"]
        del config["packages"]["solar_router"]
    dumped_yaml = yaml.dump(config, sort_keys=False, default_flow_style=False)
    with open(yaml_file, "w", encoding="UTF-8") as f:
        f.write(dumped_yaml)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    files = os.listdir(".")
    for file in files:
        if file.endswith(".yaml"):
            if file == "secrets.yaml":
                continue
            print(f"converting {file:36} ", end="")
            try:
                process_yaml_file(file)
                print("done")
            except TypeError:
                print(" ignored")
