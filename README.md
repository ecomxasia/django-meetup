# django-meetup

ecomx01/settings.py 파일의 다음 부분을 수정해주어야 함.

DATABASES = {
    'default': {
        # Postgresql
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': '{{YOUR HOST ENDPOINT}}',
        'PORT': '{{YOURE HOST PORT}}',

        # Common
        'NAME': '{{YOUR DATABASE NAME}}',
        'USER': '{{YOUR USER NAME}}',
        'PASSWORD': '{{YOUR PASSWORD}}',
    }
}
