from datetime import datetime
from re import S

from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import select_autoescape

env = Environment(
    loader=PackageLoader('templates', package_path='.'),
    autoescape=select_autoescape()
)


def render(title, result, ref_result):
    template = env.get_template('template-de.md.jinja2')

    first_name = result['first_name']
    last_name = result['last_name']
    class_name = result['class_name']
    full_name = f'{first_name} {last_name}'
    today = datetime.utcnow().strftime('%d.%m.%Y')

    scoring = {}
    student_scores = result['scores']
    ref_scores = ref_result['scores']
    for category, score in student_scores.items():
        scoring[category] = (score, ref_scores[category])

    total = result['total_points']
    maximum = result['max_points']
    grade = result['grade']

    return template.render(
        title=title,
        full_name=full_name,
        class_name=class_name,
        today=today,
        scoring=scoring,
        total=total,
        maximum=maximum,
        grade=grade,
    )
