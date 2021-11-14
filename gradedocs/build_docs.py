#!/usr/bin/env python3

import re
import sys

from openpyxl import load_workbook

from parser import parse
from renderer import render


def build_docs():
    if len(sys.argv) < 2:
        print(f'usage: {sys.argv[0]}: Grades.xlsx [SheetName]')
        sys.exit(1)
    grade_sheet_path = sys.argv[1]
    grade_sheet_name = sys.argv[2] if len(sys.argv) == 3 else None

    wb = load_workbook(grade_sheet_path)
    ws = wb[grade_sheet_name] if grade_sheet_name else wb.active
    if not ws:
        print('unable to open worksheet')
        sys.exit(1)

    first_criteria_col = 5
    reference, results = parse(ws, first_criteria_col)

    for result in results:
        filename = to_filename(result)
        with open(filename, 'w') as f:
            f.write(render(ws.title, result, reference))


def to_filename(result, suffix='md'):

    def normalize(s):
        return re.sub(r'\s', '-', s).lower()

    class_name = normalize(result['class_name'])
    first_name = normalize(result['first_name'])
    last_name = normalize(result['last_name'])

    return f'{class_name}_{last_name}_{first_name}.md'


if __name__ == '__main__':
    build_docs()
