# `Measuring Technologists`

# Настройка службы.
  Поместите файл `tcp_server.service` в каталог  `*/etc/systemd/system/`

  Перед запуском программы внесите следующие изменения в `tcp_server.service` файл в каталоге  `*/etc/systemd/system/`:
  В секции `[Service]` измените следующие значения:
  1)	`User` – Укажите корректное имя пользователя, от которого будет выполнен запуск программы. 
  2)	`WorkingDirectory` – Укажите корректный адрес директории расположения файла server.py.
  3)	`ExecStart` – Укажите полный путь к интерпретатору и полный путь к файлу server.py (через пробел).
  4)	`RestartSec` – Укажите таймаут перезагрузки сервера (в секундах).


# Пример содержимого `tcp_server.service` файла:
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

