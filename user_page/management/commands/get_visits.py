from django.core.management.base import BaseCommand
from django.db.models import F, Count
from user_page.models import SenderURL


class Command(BaseCommand):
    help = 'Return number of visits from given url'

    def add_arguments(self, parser):
        parser.add_argument('--url', default=None, type=str, required=False)

    def handle(self, *args, **options):
        url = options['url']
        if not url:
            sender_urls = SenderURL.objects.all()\
                .annotate(current_count=Count(F('requests')))\
                .order_by('-current_count')[:10]
            for sender_url in sender_urls:
                print(f'url: {sender_url.url}, '
                      f'count: {sender_url.current_count}')
        else:
            try:
                sender_url = SenderURL.objects.get(url=url)
                print(f'url: {sender_url.url}, count: {sender_url.count()}')
            except SenderURL.DoesNotExist:
                print(f'url {url} not found')
