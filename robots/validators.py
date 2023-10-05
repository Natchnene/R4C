from datetime import datetime


def is_valid_date(date_time):
    try:
        datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S")
        return True
    except ValueError:
        return False


def is_valid_data_robot(model, version, created):
    if not model or not version or not created:
        raise ValueError('Missing field(s)')
    if len(model) > 2:
        raise ValueError('Model is not correct')
    if len(version) > 2:
        raise ValueError('Version is not correct')
    if is_valid_date(created) is False:
        raise ValueError('Field created is not correct')

