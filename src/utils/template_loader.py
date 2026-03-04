from pathlib import Path


def load_template(template_name):

    template_path = Path("src/templates") / template_name

    with open(template_path, "r", encoding="utf-8") as file:
        return file.read()