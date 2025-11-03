from json_dict_processing import create_processor
from prizes_configs import prize_processor

"""извлекает год из строки"""
def process_year(date_string):
    if date_string and len(date_string) >= 4:
        return int(date_string[:4])
    return None

"""конфиг для людей-лауреатов"""
CONFIG_PERSON = {
    'id': (['id'], int),
    'name': ['knownName', 'en'],
    'gender': ['gender'],
    'birth_year': (['birth', 'date'], process_year),
    'country_birth': ['birth', 'place', 'country', 'en'],
    'country_now': ['birth', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor)
}

"""конфиг для организаций-лауреатов"""
CONFIG_ORG = {
    'id': (['id'], int),
    'name': ['orgName', 'en'],
    'founded_year': (['founded', 'date'], process_year),
    'country_founded': ['founded', 'place', 'country', 'en'],
    'country_now': ['founded', 'place', 'countryNow', 'en'],
    'prizes_relevant': (['nobelPrizes'], prize_processor)
}

"""процессоры"""
def process_persons(data):
    processor = create_processor(CONFIG_PERSON, list_processor=False)
    return processor(data)

def process_orgs(data):
    processor = create_processor(CONFIG_ORG, list_processor=False)
    return processor(data)