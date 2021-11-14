#!/usr/bin/env python3

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
    print(reference)
    print(results)


if __name__ == '__main__':
    build_docs()
