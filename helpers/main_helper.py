import json


def js_code(setValue: str) -> str:
    set_value_escaped = json.dumps(setValue)
    return f"""
    var editor = window.editor;
    if (editor) {{
        editor.setValue("");  // Удалить текущий текст
        editor.setValue({set_value_escaped});  // Ввести новый текст
    }}
    """
