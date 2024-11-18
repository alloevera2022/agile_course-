# test_hello_world.py
import subprocess

def test_hello_world_output():
    # Запускаем hello_world.py и проверяем вывод
    result = subprocess.run(
        ["python", "hello_world.py"], capture_output=True, text=True
    )
    assert result.stdout.strip() == "Привет, мир!"
