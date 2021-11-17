def parse(ws, first_criteria_col, mercy=0):
    ws_rows = iter(ws)
    title_row = next(ws_rows)
    criteria = extract_criteria(title_row, first_criteria_col)

    reference_row = next(ws_rows)
    reference_result = extract_result(reference_row, criteria)
    ref_points, max_grade = compute_grade(reference_result)
    reference_result['max_points'] = ref_points
    reference_result['total_points'] = ref_points
    reference_result['grade'] = max_grade

    student_results = []
    for row in ws_rows:
        student_result = extract_result(row, criteria)
        points, grade = compute_grade(student_result, ref_points-mercy)
        student_result['max_points'] = ref_points
        student_result['total_points'] = points
        student_result['grade'] = grade
        student_results.append(student_result)

    return (reference_result, student_results)


def round_to(x, granularity=0.01):
    return round(x * 1/granularity) * granularity


def compute_grade(result, max_points=None):
    got_points = sum(result['scores'].values())
    if not max_points:
        max_points = got_points
    return got_points, min(round_to(got_points / max_points * 5 + 1), 6)


def extract_result(row, criteria):
    result = {}
    result['class_name'] = str(row[0].value)
    result['last_name'] = str(row[1].value)
    result['first_name'] = str(row[2].value)
    result['scores'] = {}
    result['misc'] = {}
    for col_index, criterium, in criteria.items():
        value = row[col_index].value
        try:
            score = float(value)
            result['scores'][criterium] = score
        except:
            result['misc'][criterium] = value
    return result


def extract_criteria(title_row, from_col):
    criteria = {}
    for i, criterium in enumerate(title_row[from_col:]):
        criteria[i + from_col] = criterium.value
    return criteria
