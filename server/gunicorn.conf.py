import multiprocessing

# привязка к локальному хосту нашего сервера
# nginx

bind = 'http://127.0.0.1:5000'
workers = multiprocessing.cpu_count() + 1
user = 'ildar'
timeout = 120

