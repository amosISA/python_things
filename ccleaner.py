# -*- coding: utf-8 *-* 
import os, shutil
import logging
import platform

mozilla_windows = '' #route for mozilla or chrome history to delete 
mozilla_linux = '' #route for mozilla or chrome history to delete 
LOG_FILE = 'C:\Users\ORDENADOR_1\Desktop\ccleaner_python\ccleaner_log.txt';
dir_text = 'Folder contents successfully deleted!'

logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

if platform.system() == 'Windows':
	if os.path.exists(mozilla_windows):
		try: 
			for the_file in os.listdir(mozilla_windows):
				file_path = os.path.join(mozilla_windows, the_file)
				try:
					if os.path.isfile(file_path):
						os.unlink(file_path)
					elif os.path.isdir(file_path): 
						shutil.rmtree(file_path)
				except Exception as err:
					logger.error(err)
			print dir_text.center(50, "=") 
		except Exception as err: 
			logger.error(err)
	else: 
		print 'The route for mozilla history is not correct!'
elif platform.system() == 'Linux': 
	if os.path.exists(mozilla_linux):
		try: 
			for the_file in os.listdir(mozilla_linux):
				file_path = os.path.join(mozilla_linux, the_file)
				try:
					if os.path.isfile(file_path):
						os.unlink(file_path)
					elif os.path.isdir(file_path): 
						shutil.rmtree(file_path)
				except Exception as err:
					logger.error(err)
			print dir_text.center(50, "=") 
		except Exception as err: 
			logger.error(err)
	else: 
		print 'The route for mozilla history is not correct!'
else: 
	pass 
