# PythonSocketServer
server.py, client.py файлы с исходным кодом сервера и клиента соответсвтенно
Для запуска приложения требуется скачать дополнительно базу данных binlist-data.csv https://github.com/iannuttall/binlist-data и поместить ее в папку проекта.
Далее запускаем server.exe, затем client.exe  
Команды вводятся в окно клиента.  
Программа знает две команды: "EXIT" и "GET /cards/<номер карты>”. Номер карты должен быть от 16 до 20 включительно. 
Данные отправляются на сервер, обрабатываются и приходит ответ от сервера. Команды регистрозависимые.
# Идентификация ошибок
При неправильном вводе команды последует информация об ошибке "Error report - unknown command".  
При неправильно указаном номере карты - "500 Internal Server Error".  
Если указанного bin номера нет в базе - "No card with that number".
# Пример запроса
Правильный пример ввода команды: GET /cards/1800181231238768768  
Ответ:   
HTTP/1.1 200 OK  
180018 JCB CREDIT  JCB CO., LTD. JP JPN Japan 36.2048 138.253
