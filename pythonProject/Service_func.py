import pickle


def init_dict_object(file_path):
    """ Инициализация словаря в служебном файле"""
    with open(file_path, 'wb') as service_file:
        pickle.dump({}, service_file)


def get_dict_objects(file_path):
    """ Получение словаря объектов из служебного файла """

    ''' 
    Доступ к объекту осуществляется по его имени в словаре
    dict[name_object] -> object
    
    FileNotFoundError, если служебный файл не существует или пуст
    '''

    with open(file_path, 'rb') as service_file:
        dict_objects = pickle.load(service_file)
    return dict_objects


def get_object(file_path, name_object):
    """ Получение нужного объекта из служебного файла по имени """

    dict_objects = get_dict_objects(file_path)
    return dict_objects[name_object]


def save_object(name_object, obj, file_path):
    """ Сохранение объекта в служебный файл"""

    dict_objects = get_dict_objects(file_path)
    dict_objects[name_object] = obj
    with open(file_path, 'wb') as service_file:
        pickle.dump(dict_objects, service_file)