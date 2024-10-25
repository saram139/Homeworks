from pprint import pprint


def introspection_info(obj):
    info = {
        "Тип объекта": type(obj).__name__,
        "Атрибуты": [method for method in dir(obj) if not callable(getattr(obj, method))],
        "Методы": [method for method in dir(obj) if callable(getattr(obj, method))],
        "Модуль": getattr(obj, "__module__", __name__),
    }

    if isinstance(obj, str):
        info["Длина строки"] = len(obj)
    elif isinstance(obj, list):
        info["Длина списка"] = len(obj)
        info["Элементы"] = obj
    elif isinstance(obj, dict):
        info["Размер словаря"] = len(obj)
        info["Ключи"] = list(obj.keys())
        info["Значения"] = list(obj.values())
        
    return info


number_info = introspection_info(42)
pprint(number_info)
