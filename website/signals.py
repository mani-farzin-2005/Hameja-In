# signals.py
import os
from moviepy import VideoFileClip
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WebInfo
from django.conf import settings

@receiver(post_save, sender=WebInfo)
def generate_thumbnail(sender, instance, created, **kwargs):
    if instance.video_file and not instance.thumbnail:
        try:
            video_path = instance.video_file.path
            thumbnail_name = os.path.splitext(os.path.basename(video_path))[0] + ".jpg"
            thumbnail_dir = os.path.join(settings.MEDIA_ROOT, 'thumbnails')
            os.makedirs(thumbnail_dir, exist_ok=True)
            thumbnail_path = os.path.join(thumbnail_dir, thumbnail_name)

            clip = VideoFileClip(video_path)
            clip.save_frame(thumbnail_path, t=0)  # capture at 5 seconds
            clip.close()

            instance.thumbnail = f'thumbnails/{thumbnail_name}'
            instance.save(update_fields=['thumbnail'])

        except Exception as e:
            print(f"Thumbnail generation failed: {e}")
