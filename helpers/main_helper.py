import json


def js_code(setValue: str) -> str:
    """
    Функция для заполнения поля ввода (SQL запросом)

    :param setValue: Принимает SQL запрос типа str
    :return: вставляет sql-запрос в поле ввода
    """
    set_value_escaped = json.dumps(setValue)
    return f"""
    var editor = window.editor;
    if (editor) {{
        editor.setValue("");  // Удалить текущий текст
        editor.setValue({set_value_escaped});  // Ввести новый текст
    }}
    """
