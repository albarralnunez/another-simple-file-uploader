from django import forms

from simple_file_uploader.files_uploads.models import FileUpload


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = FileUpload
        exclude = ['id', 'md5']

    def save(self, user, commit=True):
        self.instance.user = user
        instance = super().save(commit=True)
        return instance
