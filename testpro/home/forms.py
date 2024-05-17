from django import forms
from .models import Video

class VideoForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['title', 'description', 'video_file']

    def clean_video_file(self):
        video_file = self.cleaned_data['video_file']
        # Add validation for file size if needed
        # For example, to restrict file size to 20GB:
        max_size = 20 * 1024 * 1024 * 1024  # 20 GB in bytes
        if video_file.size > max_size:
            raise forms.ValidationError("The file size exceeds the maximum allowed (20GB).")
        return video_file
