#!/usr/bin/env python3

import os
import re
import sys

import click
from openpyxl import load_workbook

from parser import parse
from renderer import render


@click.command()
@click.option('--sheet', help='Sheet in Workbook to be processed.')
@click.option('--outdir', default='.', help='Directory for output.')
@click.argument('workbook', type=click.File('rb'))
def build_docs(sheet, outdir, workbook):
    wb = load_workbook(workbook)
    ws = wb[sheet] if sheet else wb.active
    if not ws:
        raise ValueError(f'unable to open workbook {workbook}')

    if os.path.exists(outdir):
        if not os.path.isdir(outdir):
            raise ValueError(f'{outdir} is not a directory')
    else:
        os.mkdir(outdir)

    first_criteria_col = 5
    reference, results = parse(ws, first_criteria_col)

    for result in results:
        filename = os.path.join(outdir, to_filename(result))
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
