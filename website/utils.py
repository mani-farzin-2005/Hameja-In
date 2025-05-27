from django.urls import get_resolver, reverse
from blog.models import Post
from tour.models import *
from hotel.models import *

def get_named_url_choices():
    urlconf = get_resolver()
    choices = []
    for pattern in urlconf.url_patterns:
        if hasattr(pattern, 'name') and pattern.name:
            choices.append((pattern.name, pattern.name.replace(":", " → ").title()))
        # Check for included URLs
        if hasattr(pattern, 'url_patterns'):
            for sub_pattern in pattern.url_patterns:
                if hasattr(sub_pattern, 'name') and sub_pattern.name:
                    full_name = f"{pattern.namespace}:{sub_pattern.name}" if pattern.namespace else sub_pattern.name
                    choices.append((full_name, full_name.replace(":", " → ").title()))
    for post in Post.objects.filter(status=True):
        choices.append((f'("website:post",{post.id})', f'Blog → {post.title}'))

    for hotelll in Hotel.objects.all():
        choices.append((f'("hotels:single",{hotelll.id})', f'Hotel → {hotelll.name}'))

    for tourr in Tour.objects.all():
        choices.append((f'("tour:tour",{tourr.id})', f'Tour → {tourr.name}'))

    for tour_group in TourGroup.objects.all():
        choices.append((f'("tour:package",{tour_group.id})', f'Tour Group → {tour_group}'))

    return sorted(choices)
