"""создаёт список всех призов с атрибутами лауреата"""
def flatten_prizes(data):
    prizes = []
    for l in data:
        for p in l.get('prizes_relevant', []):
            prize_copy = p.copy()
            prize_copy['laureate_id'] = l.get('id')
            prize_copy['laureate_name'] = l.get('name')
            prize_copy['birth_year'] = l.get('birth_year')
            prizes.append(prize_copy)
    return prizes