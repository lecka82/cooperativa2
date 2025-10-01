import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

import django
django.setup()

from accounts.models import Profile

# Caminho local de uma imagem de teste
caminho_imagem = "C:/Users/TESOURARIA/Downloads/cooperativa/cooperativa/media/profiles/bart.jpg"

# Pegue um perfil qualquer
p = Profile.objects.last()

# Abra a imagem e atribua ao campo foto
with open(caminho_imagem, "rb") as f:
    p.foto.save("teste.jpg", f, save=True)

print("URL gerada:", p.foto.url)
