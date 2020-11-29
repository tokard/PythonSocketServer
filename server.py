import csv
import socket


def csv_reader(file, num):
    bin_num = num[0:6]
    reader = csv.reader(file)
    for row in reader:
        if row[0] == bin_num:
            return ' '.join(row)
    return 'No card with that number'


def csv_connection(num):
    csv_path = "binlist-data.csv"
    with open(csv_path, "r", encoding='utf-8') as f:
        return csv_reader(f, num)


def check_num(num):
    if 16 <= len(num) <= 20 and num.isdigit():
        return 1
    else:
        return 0


def check_request(request, conn):
    if "GET /cards/" in request:
        num = request.split('/')[2]
        if check_num(num):
            answer = 'HTTP/1.1 200 OK\n' + csv_connection(num)
            conn.send(answer.encode('utf-8'))
        else:
            conn.send('500 Internal Server Error'.encode('utf-8'))
    elif "EXIT" == request:
        conn.send('EXIT'.encode('utf-8'))
    else:
        conn.send('Error report - unknown command'.encode('utf-8'))


def start():
    sock = socket.socket()
    sock.bind(('', 8080))
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        check_request(data, conn)
    sock.close()

start()