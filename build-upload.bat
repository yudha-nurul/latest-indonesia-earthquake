@echo off
pip -m build
py -m twine upload --repository pypi dist/*