import dropbox

# Initialize Dropbox client
dbx = dropbox.Dropbox('YOUR_ACCESS_TOKEN')

# Define the folder path
folder_path = '/path/to/your/folder'

def download_folder(folder_path):
    for entry in dbx.files_list_folder(folder_path).entries:
        if isinstance(entry, dropbox.files.FileMetadata):
            with open(entry.name, 'wb') as f:
                metadata, res = dbx.files_download(entry.path_lower)
                f.write(res.content)

download_folder(folder_path)
