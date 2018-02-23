from django.apps import AppConfig


class FilesUploadsConfig(AppConfig):
    name = 'simple_file_uploader.files_uploads'
    verbose_name = "FilesUploads"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
