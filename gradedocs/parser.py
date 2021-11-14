def parse(ws, first_criteria_col):
    ws_rows = iter(ws)
    title_row = next(ws_rows)
    criteria = extract_criteria(title_row, first_criteria_col)
    print(criteria)
    reference_row = next(ws_rows)
    reference_result = extract_result(reference_row, criteria)
    student_results = []
    for row in ws_rows:
        student_results.append(extract_result(row, criteria))
    return (reference_result, student_results)


def extract_criteria(title_row, from_col):
    criteria = {}
    for i, criterium in enumerate(title_row[from_col:]):
        criteria[i + from_col] = criterium.value
    return criteria


def extract_result(row, criteria):
    result = {}
    result['class'] = row[0].value
    result['first_name'] = row[1].value
    result['last_name'] = row[2].value
    for col_index, criterium, in criteria.items():
        result[criterium] = row[col_index].value
    return result
