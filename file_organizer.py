# Library importing
import os
import shutil

class FileOrganization():
	# Initialize
	def __init__(self, current_dir, destination_dir = '', ext):
		# Current directory that want to be organized
		self.current_dir = current_dir
		# Extension that want to be organized
		self.ext = ext
		# Destination directory to store the organized extension(s)
		if destination_dir != '' :
			self.destination_dir = destination_dir

	def organize(self):

		# Search for all file in the current directory
		for file in os.listdir(self.current_dir):
			# Get file name and file extension from each file in the current directory
			filename, file_ext = os.path.splitext(file)

			# Check if destination directory is exists
			if not os.path.exists(self.destination_dir):
				os.makedirs(self.destination_dir)

			# Move the file using shutil from current directory to destination directory
			if file_ext in (self.ext):
				shutil.move(
					os.path.join(self.current_dir, (filename + file_ext)),
					os.path.join(self.destination_dir,  (filename + file_ext))
				)					
