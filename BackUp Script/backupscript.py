import shutil
import os, time

# Back Up Folder Source
back_up_folder = r"D:\docs\backup_source"

# Backing Up Location
save_folder = r"D:\docs\backup_dest"

# Current TimeStamp
current_time = time.strftime("%Y-%m-%d-%H-%M-%S")

# Create a new folder in the backup folder with the date and time stamp
current_backup_path = os.path.join(save_folder, current_time)
os.mkdir(current_backup_path)

# Copy all the files and subdirectories from the folder to be backed up
for root, dirs, files in os.walk(back_up_folder):
    for file in files:
        source_file_path = os.path.join(root, file)
        dest_file_path = os.path.join(current_backup_path, file)
        shutil.copy2(source_file_path, dest_file_path)
        
print("Backup done succesfully.")
