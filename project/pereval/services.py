def get_path_upload_photo(instance, file):
    return f'photos/pereval_{instance.pereval.id}/{file}'
