# `Measuring Technologists`
# Общее описание программы
  Данная программа представляет собой TCP-сервер, который запускается в качестве службы и предназначен для выполнения задач на больших объемах данных. Она использует библиотеку Dask для эффективной работы с параллельными вычислениями.
  
  Сервер принимает задачи в виде набора Parquet данных и набора python функций для исполнения как объект Dask. После получения задачи, сервер выполняет функции на наборе данных из Parquet-файла при помощи Dask-библиотеки и возвращает результат клиенту.
  
  Класс TCP содержит методы для прослушивания соединений, обработки запросов и отправки ответов клиенту. 
  Класс Loader отвечает за загрузку и сохранение файлов.
  Класс Service предоставляет информацию о текущем состоянии сервера и процессов.
  Класс Math отвечает за выполнение математических операций. Метод math_work загружает данные из файла, используя метод get_file класса Loader, выполняет необходимые операции при помощи библиотеки Dask и сохраняет результат в файл при помощи метода out_file класса Loader.
  Класс Manager наследует методы классов Service и Math и отвечает за управление задачами. Метод task_manager обрабатывает запросы клиента и передает их на выполнение в метод math_work. 
  Класс Handler наследует методы классов Manager и TCP и отвечает за обработку запросов от клиентов. Метод handle_client принимает запрос от клиента, передает его на обработку в метод task_manager и отправляет ответ клиенту при помощи метода socket_response.
  Класс Server наследует методы класса Handler и представляет собой основной класс программы. Метод start запускает сервер и ожидает подключения клиентов..

# Настройка службы:
  Поместите файл `tcp_server.service` в каталог  `*/etc/systemd/system/`

  Перед запуском программы внесите следующие изменения в `tcp_server.service` файл в каталоге  `*/etc/systemd/system/`:
  В секции `[Service]` измените следующие значения:
  1)	`User` – Укажите корректное имя пользователя, от которого будет выполнен запуск программы. 
  2)	`WorkingDirectory` – Укажите корректный адрес директории расположения файла server.py.
  3)	`ExecStart` – Укажите полный путь к интерпретатору и полный путь к файлу server.py (через пробел).
  4)	`RestartSec` – Укажите таймаут перезагрузки сервера (в секундах).


# Пример:
    [Unit]
    Description=TCP SERVER
    After=syslog.target
    After=network.target
    
    [Service]
    Type=forking
    User=username
    WorkingDirectory=/username/tcpserver
    ExecStart=/usr/bin/python3 /username/tcpserver/server.py
    RestartSec=10
    Restart=always
    
    [Install]
    WantedBy=multi-user.target

# Запуск:
    sudo systemctl enable tcp_server.service # Добавить службу в автозагрузку ОС:
    sudo systemctl start tcp_server.service # Запустить службу
    sudo systemctl status tcp_server.service # Проверить состояние
  
  После перезапуска ОС, запуск программы будет обеспечен средствами ОС.

# Остановка:
    sudo systemctl stop tcp_server.service – Остановить службу
    sudo systemctl disable tcp_server.service – Удалить службу из автозагрузки ОС

# Примеры TCP запросов:

  # Статус сервера.
    {"Header":"Info",   
    "Request":"Status"} 
  # Запущено Dask процессов.
    {"Header":"Info",
    "Request":"Dask process"}
  # Запущено всего процессов.
    {"Header":"Info",
    "Request":"All process"}
  # Вся статистика.
    {"Header":"Info",
    "Request":"All statistic"}


# Dask:
    {"Header":"Dask",
    "Request":{"Directory":"C:/your_folder/",  # Путь к рабочей папке
               "Base":"time_series.parquet",   # Parquet файл с входными данными
               "File":"work.py"}}              # Python файл с формулами


# Запуск тестов:
  pytest.exe t_config.py
  pytest.exe t_service.py
  pytest.exe t_math.py

