from collections import defaultdict
"""подсчитывает количество пропусков для каждого поля"""
def count_missing(data, fields):
    missing = {}
    total = len(data)
    for field in fields:
        missing[field] = sum(1 for d in data if d.get(field) in (None, '', []))
    return missing

"""считает распределение по странам"""
def get_country_counts(data):
    country_counts = defaultdict(int)
    for l in data:
        country = l.get('country_birth') or 'Unknown'
        country_counts[country] += 1
    return country_counts

"""считает распределение по категориям"""
def get_category_counts(prizes):
    category_counts = defaultdict(int)
    for p in prizes:
        category = p.get('category_en', 'Unknown')
        category_counts[category] += 1
    return category_counts