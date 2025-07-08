from azure.storage.filedatalake import DataLakeServiceClient
import os

def upload_file_to_adls(local_path, remote_path, file_system_name, connection_string):
    service_client = DataLakeServiceClient.from_connection_string(connection_string)
    file_system_client = service_client.get_file_system_client(file_system=file_system_name)
    directory_path = os.path.dirname(remote_path)
    file_name = os.path.basename(remote_path)

    directory_client = file_system_client.get_directory_client(directory_path)
    file_client = directory_client.create_file(file_name)

    with open(local_path, 'rb') as data:
        file_client.append_data(data, offset=0, length=os.path.getsize(local_path))
        file_client.flush_data(os.path.getsize(local_path))

    print(f"Uploaded {local_path} to ADLS as {remote_path}")

