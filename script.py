from accounts.models import Profile

for p in Profile.objects.all():
    if p.foto and "media/" in str(p.foto):
        p.foto = None
        p.save()
