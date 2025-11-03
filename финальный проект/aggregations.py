from statistics import mean, median, stdev

"""среднее"""
def safe_mean(values):
    values = [v for v in values if v is not None]
    return mean(values) if values else None

"""медиана"""
def safe_median(values):
    values = [v for v in values if v is not None]
    return median(values) if values else None

"""отклонение"""
def safe_stdev(values):
    values = [v for v in values if v is not None]
    return stdev(values) if len(values) > 1 else None

"""Топ-N элементов"""
def top_n(data_dict, n=5):
    return sorted(data_dict.items(), key=lambda x: x[1], reverse=True)[:n]