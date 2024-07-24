# Импорт библиотек
import os # os необходим для работы с файловой системы
from collections import defaultdict # collections необходим для создания словаря, который автоматически создает списки для новых ключей
from pprint import pprint # pprint необходим для форматированного вывода сложных структур данных

def categorize_files_by_type(folder_path): # Функция для категоризации файлов по типу (расширению)
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path): # Проверка существования пути и его типа
        raise ValueError(f"Указанный путь '{folder_path}' не существует или не является каталогом.")
    
    file_dict = defaultdict(list) # Создаем словарь с ключами по умолчанию (пустые списки) для хранения файлов по типам
    system_files = {'.DS_Store'} # Набор системных файлов, которые нужно исключить из обработки
    
    for root, _, files in os.walk(folder_path): # Обход всех файлов и поддиректории в указанной директории
        for file in files:
            if file in system_files: # Пропускает системные файлы
                continue
            file_extension = os.path.splitext(file)[1] # Получает расширение файла
            file_path = os.path.join(root, file) # Формирует полный путь к файлу
            file_dict[file_extension].append(file_path) # Добавляет файл в словарь по соответствующему расширению
    
    return dict(file_dict) # Возвращает словарь

result = categorize_files_by_type("/path/to/root/folder") # Пример использования функции (введите свой путь к папке)
pprint(result) # Форматированный вывод результата с помощью pprint