import os
import shutil

current_dir = "E:/Programming/Python/Playground/"

destination_folder = 'Testing/'

for f in os.listdir(current_dir):
	filename, file_ext = os.path.splitext(f)

	if not os.path.exists((current_dir + destination_folder)):
		print("Oke")
		os.makedirs((current_dir + destination_folder))

	if not file_ext:
		pass
	elif filename in ('test') and file_ext in ('.py'):
		print("Done")
		
		shutil.move(
			os.path.join(current_dir, (filename + file_ext)),
			os.path.join(current_dir, destination_folder,  (filename + file_ext))
		)
			
