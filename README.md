# **База данных ЖД**
### Установка нужных компонентов и сред
1. Установить *Python* (Скачать можно [тут](https://www.python.org)). Версию *Python* лучше брать от 3.8.0 и выше;
2. Установить *PyCharm Community Edition* (Скачать можно [тут](https://www.jetbrains.com/pycharm/download/?section=windows));
3. *Установить *SQLite* (Скачать можно [тут](https://www.sqlite.org/download.html)) - для просмотра и удобного редактирования данных (в формате .db);
4. *Установить *Qt Designer* (Скачать можно [тут](https://build-system.fman.io/qt-designer-download)) - для создания, реактирования, просмотра форм (в формате .ui).
### Сборка БД
1. Сделать ```git clone https://github.com/AdminSokol/GrandMaket_SQL.git``` репозитория в папку среды IDE;
2. Установить нужные библиотеки для проекта через терминал в *Pycharm* с помощью команды ```pip install <фреймворк>```;
3. Установить *PyInstaller* через терминал в *Pycharm* с помощью команды ```pip install PyInstaller``` для того, чтобы собрать приложение;
   - После установки *PyInstaller* через терминал в *Pycharm* вводим команду: ```pyinstaller main.py --icon=train.ico --noconsole --path="<Путь до проекта>\venv\Lib\site-packages"```;
   - Почитать документацию про *PyInstaller* и его параметры сборки можно [тут](https://readthedocs.org/projects/pyinstaller/downloads/pdf/latest/).
4. После сборки в папке проекта появятся две папки - ***build*** и ***dist***. Нам нужна только папка ***dist*** в ней будет еще одна папка ***main***, зайдя в ***main*** будет папка ***_internal*** и исполнительный файл с расширением ***.exe***. После чего в ***_internal*** копируем и вставляем из нашего проекта файлы ***res_rc.py*** и ***res.qrc***. Теперь в папку ***main*** из проекта копируем и вставляем все файлы с расширением (***.db*** и ***.ui***), а также папку ***sql_maket***;
5. *Исполнительный файл лучше переименовать из ***main.exe*** в ***База данных ЖД.exe*** и папку из ***main*** в ***База данных ЖД***. Также если есть папки ***Backup***, ***Фотки ЗЧ***, ***Картинки локо***, то их закинуть тоже во внутрь сборочной папки.
#### Уточнение_1: После сборки с GitHub в приложение будет пустая учётка(это значит, что логин и пароль при авторизации нужно будет оставлять пустым) с максимальными правами доступа, в вкладке "Другое"->"Авторизация" надо будет изменить пустую учетку, чтобы вы не забыли логин и пароль от учетки и при необходимости для других - добавили учетные записи.
#### Уточнение_2: В данных с GitHub не указаны мастера, нет информации о тех.обслуживаниях и инвентаризации.
---
#### Приложение собрано, папку можете перемещать куда угодно! Теперь приложение можно запускать через ярлык или исполнительный файл!