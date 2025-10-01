import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ========= Segurança / Dev =========
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['coopsuzanapolis.onrender.com']

# ========= Apps =========
INSTALLED_APPS = [
    "jazzmin",  # Jazzmin antes do admin
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "accounts.apps.AccountsConfig",
    "coletores",
    "materiais",
    "caixa",
    "pagina",
    "app",
    "cloudinary",
    "cloudinary_storage",
]

# ========= Middleware =========
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    # WhiteNoise será inserido abaixo se DEBUG=False
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ========= URLs e WSGI =========
ROOT_URLCONF = "app.urls"
WSGI_APPLICATION = "app.wsgi.application"

# ========= Templates =========
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "app" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ========= Banco de Dados =========
DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}

# ========= Validação de Senhas =========
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ========= i18n / tz =========
LANGUAGE_CODE = "pt-br"
TIME_ZONE = "America/Sao_Paulo"
USE_I18N = True
USE_TZ = True

# ========= Static / Media =========
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "app" / "static",
]
STATIC_ROOT = BASE_DIR / "staticfiles"

#MEDIA_URL = "/media/"
#MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ========= Login redirects =========
LOGIN_URL = "/login/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/"

# ========= Jazzmin =========
JAZZMIN_SETTINGS = {
    "site_title": "Cooperativa Suzanápolis",
    "site_header": "Admin • Cooperativa",
    "site_brand": "Cooperativa Suzanápolis",
    "welcome_sign": "Bem-vindo à área administrativa",
    "copyright": "Cooperativa de Reciclagem • Suzanápolis/SP",
    "site_logo": "img/logo_suzanapolis.png",
    "site_logo_classes": "img-fluid",
    "login_logo": "img/logo_suzanapolis.png",
    "login_logo_dark": None,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "custom_css": "css/jazzmin_custom.css",
    "topmenu_links": [
        {"name": "Admin", "url": "admin:index"},
        {"name": "Dashboard do Site", "url": "dashboard", "icon": "fas fa-home"},
        {"name": "Sair", "url": "admin_logout", "icon": "fas fa-sign-out-alt"},
    ],
    "usermenu_links": [
        {"name": "Alterar senha", "url": "admin:password_change", "icon": "fas fa-key"},
        {"name": "Sair", "url": "admin_logout", "icon": "fas fa-sign-out-alt"},
    ],
    "icons": {
        "coletores.Coletor": "fas fa-user-friends",
        "materiais.Material": "fas fa-recycle",
        "caixa.LancamentoCaixa": "fas fa-cash-register",
        "auth.User": "fas fa-user",
        "auth.Group": "fas fa-users-cog",
        "accounts.Profile": "fas fa-id-badge",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-angle-right",
    "related_modal_active": True,
    "order_with_respect_to": ["coletores", "materiais", "caixa", "accounts"],
    "changeform_format": "collapsible",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "accounts.profile": "collapsible",
    },
}

JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",
    "dark_mode_theme": "slate",
    "navbar": "navbar-dark",
    "brand_colour": "navbar-primary",
    "accent": "accent-warning",
    "no_navbar_border": True,
    "sidebar": "sidebar-dark-success",
    "sidebar_fixed": True,
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_flat_style": True,
    "footer_fixed": False,
    "body_small_text": False,
    "footer_small_text": True,
}

# ========= Produção =========
if not DEBUG:
    MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True


# ========= Cloudinary =========

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}
# ========= Fim das Configurações =========