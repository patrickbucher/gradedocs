from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import select_autoescape

env = Environment(
    loader=PackageLoader('templates', package_path='.'),
    autoescape=select_autoescape()
)


def render():
    template = env.get_template('template-de.md.jinja2')
    print(template.render(
        title='Titel',
        student='Student',
        today='01.01.2022',
        scores={
            'Stil': (4, 5),
            'Qualität': (7, 10),
        },
        total=11,
        maximumTotal=15,
        grade=4.67,
    ))
