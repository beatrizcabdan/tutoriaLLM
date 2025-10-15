import os


def load_files_in_folder(folder):
	return [folder + f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]