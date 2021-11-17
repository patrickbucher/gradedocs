# GradeDocs

Turns Excel worksheets into grade/score documents.

## Example

Given such an Excel Worksheet (see `examples/example.xlsx`):

![Example Excel Worksheet](assets/example-xlsx.png)

The following commands converts each line (except for the title and reference
line) into a Markdown file:

    $ gradedocs/build_docs.py examples/example.xlsx

The scoring criteria can be abbreviated in the Excel sheet for better overview.
A (partial) criteria mapping YAML file can be defined to replace those by longer
names:

    $ gradedocs/build_docs.py examples/example.xlsx --catfile examples/categories.yaml

It is possible to reduce the points needed for the maximum grade using the
`--mercy` flag:

    $ gradedocs/build_docs.py examples/example.xlsx --mercy 5

### Worksheet Structure

The worksheet must meet the following **column** requirements:

- The first three column identify a student:
    1. Class
    2. Last Name
    3. First Name
- The next two columns contain the result:
    4. Points scored
    5. Grade achieved
- All the following columns contain the scores of the individual criteria.
    - Numeric values will be used to calculate the scores achieved—both for the individual criteria and for the total.
    - Non-numeric values will be read into a "miscellaneous" section to be displayed separately.

Note that the total score and grade, which are usually computed by a formula, will be ignored. The program will re-calculate them on its own.

The worksheet must meet the following **row** requirements:

1. The first row is the title row, defining the criteria.
2. The second row is the _reference_ row, which contains the maximum possible score per criterium.
3. All the following rows are _student_ rows, which are used to generate the actual documents.

In this example, two files will be generated:

    6a_huber_jasmin.md
    6b_meier_georg.md

Which can be converted to a PDF using the `examples/Makefile` (given that
`pandoc`, XeLaTeX, and a couple of fonts—Lato, Vollkorn, Fira Code—are
installed):

    $ make 6a_huber_jasmin.pdf

The result is a PDF that looks as follows:

![Example PDF Grading Sheet](assets/example-pdf.png)

Type `gradedocs/build_docs.py --help` for more information on the command line
parameters and arguments.
