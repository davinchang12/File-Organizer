import os
import shutil

current_dir = "E:/Programming/Python/Playground"

for f in os.listdir(current_dir):
	filename, file_ext = os.path.splitext(f)
	print(filename+file_ext)
	try:
		if not file_ext:
			pass
		elif filename in ('test') and file_ext in ('.py'):
			print("Done")
			
			shutil.move(
				os.path.join(current_dir, (filename + file_ext)),
				os.path.join(current_dir, 'Test Files',  (filename + file_ext))
			)
			
	except (FileNotFoundError, PermissionError):
		pass