from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView

from simple_file_uploader.files_uploads.models import FileUpload
from .forms import UploadFileForm


class FileUploadedListView(LoginRequiredMixin, FormView, ListView):

    model = FileUpload
    template_name = 'pages/home.html'
    form_class = UploadFileForm
    success_url = reverse_lazy('files_uploads:file-list')

    def get_queryset(self):
        return self.model.objects.filter(
            user=self.request.user)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = form_class(request.POST, request.FILES)
        if not form.is_valid():
            return self.form_invalid(form)
        form.save(user=request.user, commit=True)
        return self.form_valid(form)
