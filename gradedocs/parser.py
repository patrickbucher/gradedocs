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
    result['class'] = str(row[0].value)
    result['first_name'] = str(row[1].value)
    result['last_name'] = str(row[2].value)
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
