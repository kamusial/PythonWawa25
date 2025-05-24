## send to PyPi
hatch build
twine upload --repository testpypi dist/*

## generate .exe
pyinstaller -F .\invoice_generator\main.py --collect-data=invoice_generator
