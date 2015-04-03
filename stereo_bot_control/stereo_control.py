#!/usr/bin/env python
# Insertar una licencia fantabulosa
# Referencias:
# https://python-gtk-3-tutorial.readthedocs.org/en/latest/index.html
import rospy
import numpy as np
import sys
import os
from std_msgs.msg import Float64
from gi.repository import Gtk

class StereoControl:
	"""Aplicacion para el control del robot estereo"""
	def __init__(self):
		

		self.builder = Gtk.Builder()
		self.builder.add_from_file('gui/stereo_bot.glade')
		self.window = self.builder.get_object('mainWindow')
		self.window.show()

		handlers = {
			"onDeleteWindow": Gtk.main_quit,
			"angleValueChanged": self.angleValueChanged
		}

		self.builder.connect_signals(handlers)

		try:
			robot_name = 'stereo_bot'
			topic_name = '/'+robot_name+'/neck_position_controller/command'
			self.pub = rospy.Publisher(topic_name, Float64, queue_size=10)
			rospy.init_node('stereo_bot_control', anonymous=True)
		except rospy.ROSInterruptException:
			pass

	def angleValueChanged(self, range, scroll, value):
		if not rospy.is_shutdown():
			value = np.clip(value, -90, 90)
			value = np.radians(value)
			rospy.loginfo(value)
			self.pub.publish(value)

if __name__ == '__main__':
	# Se configura el directorio de trabajo
	rDir = os.path.split(sys.argv[0])[0]
	os.chdir(rDir)
	
	gui = StereoControl()
	Gtk.main()
	