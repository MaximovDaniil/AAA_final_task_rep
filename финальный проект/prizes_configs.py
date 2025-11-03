from json_dict_processing import create_processor

"""извлекает год из строки"""
def process_year(date_string):
    if date_string and len(date_string) >= 4:
        return int(date_string[:4])
    return None

"""конфиг для призов"""
CONFIG_PRIZE = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], process_year), 
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus']
}

def prize_processor(data):
    processor = create_processor(CONFIG_PRIZE, list_processor=True)
    return processor(data)
