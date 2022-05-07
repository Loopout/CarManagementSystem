import socket

############ADRESS##############
serverip = '192.168.0.100'
port = 9000
buffsize = 4096

while True:
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.bind((serverip,port))
	server.listen(1)
	print('waiting client...')

	client, addr = server.accept()
	print('connected from:', addr)

	data = client.recv(buffsize).decode('utf-8')
	print('Data from client: ',data)
	# - บันทึกข้อมูลที่ได้รับจาก [2]
	# write to csv

	client.send('saved'.encode('utf-8'))
	client.close()


















'''
[1]-car-system-out.py
	- server.py
	(function)
		- บันทึกเวลาออก
		- คำนวณชั่วโมงจอด
		- คำนวณค่าจอด
		- บันทึกข้อมูลที่ได้รับจาก [2]
'''