# `Measuring Technologists`

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
  pytest.exe test_name.py

https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake.gif
