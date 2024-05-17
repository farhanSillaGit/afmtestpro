from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os
import subprocess
from django.conf import settings

BASE_DIR = settings.BASE_DIR
@shared_task
def transcode_to_mpd(video_file_path):
    # Define the output directory for MPD files
    output_directory = os.path.join(BASE_DIR, 'videos')
    # Ensure that the output directory exists, create it if necessary
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Construct the output MPD file path
    output_mpd_file = os.path.join(output_directory, 'output.mpd')

    # Use FFmpeg to transcode the video to MPD format

    ffmpeg_executable = 'ffmpeg'
    command = [ffmpeg_executable,'-i', video_file_path, '-c:v', 'libx264', '-preset', 'fast', '-c:a', 'aac', '-strict', 'experimental', '-f', 'dash', output_mpd_file]


    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("Error transcoding video:", e)
        return None

    return output_mpd_file
