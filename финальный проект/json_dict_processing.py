"""извлекаем значение"""
def extract_nested_value(obj, keys):
    current = obj
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return None
    return current

"""обрабатываем словарь"""
def process_dictionary_with_config(dictionary, config):
    result = {}
    for attribute, config_value in config.items():
        if isinstance(config_value, tuple):  # путь + функция обработки
            path, processor_func = config_value
            raw_value = extract_nested_value(dictionary, path)
            result[attribute] = processor_func(raw_value) if raw_value is not None else None
        else:  # только путь
            path = config_value
            raw_value = extract_nested_value(dictionary, path)
            result[attribute] = raw_value
    return result

"""обрабатываем список"""
def process_list_of_dicts_with_config(list_of_dicts, config):
    return [process_dictionary_with_config(item, config) for item in list_of_dicts]

"""создаём обработчик"""
def create_processor(config, list_processor=False):
    if list_processor:
        def processor(data):
            return process_list_of_dicts_with_config(data, config)
    else:
        def processor(data):
            return process_dictionary_with_config(data, config)
    return processor