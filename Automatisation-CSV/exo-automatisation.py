from pathlib import Path
from openpyxl import Workbook, load_workbook
import os


os.getcwd()

wb = load_workbook('/home/kamel/Bureau/Automatisation-CSV/exercice.xlsx')

sheet = wb['Tech IA']

tuple(sheet['A1'])