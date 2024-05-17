import os
from django.conf import settings
from django.shortcuts import render,redirect
from . forms import VideoForm
from .models import Video
from .utils import transcode_to_mpd
# Create your views here.
def index(request):
    return render(request,'index.html')
def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        # Save the uploaded video temporarily
        if form.is_valid():
            video = form.save(commit=False)
            video.save()



            video_file_path = os.path.join(settings.MEDIA_ROOT, str(video.video_file))
            mpd_file_path = transcode_to_mpd(video_file_path)

            video.mpd_file = mpd_file_path
            video.save()

            # Split the video into chunks
            #chunk_duration = 60  # Example: Split video into 60-second chunks
            #chunks_metadata = split_video_into_chunks(video_file_path, chunk_duration)

            return redirect('video_list')

        return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})


from .models import Video

def video_list(request):
    # Retrieve all videos from the database
    videos = Video.objects.all()


    return render(request, 'video_list.html', {'videos': videos})
#import ffmpeg

