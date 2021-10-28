SECRET_KEY = 'django-insecure-yixoh#_ki#9zo^k$-)j=51te4$7#8p18u=79b$b73-bteh^+gq'
DEBUG = True
CORS_ORIGIN_ALLOW_ALL=True
INSTALLED_APPS = [
  'corsheaders'    
]
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]
ROOT_URLCONF = 'django_project.urls'