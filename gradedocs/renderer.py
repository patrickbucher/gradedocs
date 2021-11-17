from datetime import datetime

from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import select_autoescape

env = Environment(
    loader=PackageLoader('templates', package_path='.'),
    autoescape=select_autoescape()
)


def render(title, result, ref_result, prefix='', mercy=0):
    template = env.get_template('template-de.md.jinja2')

    title = f'{prefix} {title}' if prefix else title
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
    misc = result['misc']

    return template.render(
        title=title,
        full_name=full_name,
        class_name=class_name,
        today=today,
        scoring=scoring,
        total=total,
        maximum=maximum,
        mercy=mercy,
        grade=grade,
        misc=misc,
    )
