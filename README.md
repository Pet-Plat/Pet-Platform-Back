# Pet-Projects-Platform

#### Установка через консоль
```bash
git clone https://github.com/Pet-Plat/Pet-Platform-Back.git
cd Pet-Platform-Back/
poetry install
poetry shell
```
UNIX:
```bash
cat .env.example > .env
```
Windows:
```powershell
copy .env.example .env
```

#### Запуск тестов
```bash
(pet-plat-py3.12) poetry run pytest
```
##### или
```bash
(pet-plat-py3.12) python -m pytest
```

#### Установка через PyCharm
1. Открываем PyCharm
2. File -> Project From Version Control
3. ![input_url](https://github.com/Pet-Plat/Pet-Platform-Back/blob/master/docs/setup/pycharm/input_url.png)
4. Paste URL (https://github.com/Pet-Plat/Pet-Platform-Back) -> Clone -> Trust Project
5. Редактор может попытаться вас определить, как поставить окружение poetry. Если не уверены, следуйте подпунктам 5 (нажав Cancel)
 ![setup_poetry_auto](https://github.com/Pet-Plat/Pet-Platform-Back/blob/master/docs/setup/pycharm/setup_poetry_auto.png) (если получилась ошибка, то):

5.1. File -> Settings

5.2. Project: Pet-Platform-Back -> Python Interpreter

5.3. Add interpreter -> Add local interpreter

5.4. ![add_poetry_interpreter](https://github.com/Pet-Plat/Pet-Platform-Back/blob/master/docs/setup/pycharm/add_poetry_interpreter.png)

Важно поставить версию Python от минимум 3.11

5.5. Ок -> Apply

6. В корне директории (Pet-Platform-Back) создайте файл .env
7. Скопируйте в него все, что есть в .env.example
8. (опционально). Чтобы редактор кода лучше понимал относительные импорты внутри src, пометьте src как ресурсную:

8.1. ЛКМ по src -> Mark directory as -> Sourcec Root

