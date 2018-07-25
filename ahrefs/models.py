from django.db import models

# Create your models here.
class UrlSearch(models.Model):
    url = models.URLField(max_length=200)
    session_id = models.IntegerField(default=0)

    def __str__(self):
        return self.url

    class Meta:
        verbose_name_plural = 'Paginas Buscadas'


class Backlinks(models.Model):
    LENGUAGE_CHOICES = (
        ('es', 'Español'),
        ('en', 'Ingles'),
        ('it', 'Italiano'),
        ('ru', 'Ruso'),
        ('ja', 'Japones'),
        ('ru', 'Rumano'),
        ('nl', 'Holandés'),
        ('ar', 'Armenio'),
        ('fr', 'Francés'),
        ('de', 'Aleman'),
        ('pl', 'Polaco'),
        ('tw', 'Taiwanes'),
        ('kr', 'Koreano'),
    )

    SITE_LINK_CHOICES = (
        ('Comentario', 'Comentario'),
        ('Articulo', 'Articulo'),
        ('Foro', 'Foro')
    )

    url_from = models.URLField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    url_to = models.URLField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200, choices=LENGUAGE_CHOICES, blank=True, null=True)
    anchor = models.CharField(max_length=200, blank=True, null=True)
    nofollow = models.BooleanField(blank=True)
    site_link = models.CharField(max_length=200, choices=SITE_LINK_CHOICES, blank=True, null=True)
    foro = models.BooleanField(blank=True, default=False)
    session_id = models.IntegerField(default=0)


    def __str__(self):
        return self.url_from

    class Meta:
        verbose_name_plural = 'Backlinks del sitio'


## Google Section
class GoogleSearch(models.Model):
    keyword = models.CharField(max_length=200, blank=True, null=True)
    cant = models.IntegerField(blank=True, null=True)
    session_id = models.IntegerField(default=0)

    def __str__(self):
        return self.keyword

    class Meta:
        verbose_name_plural = 'Keywords para Google'


class GoogleBD(models.Model):
    keyword = models.ForeignKey(GoogleSearch, on_delete=models.CASCADE, blank=True, null=True)
    url = models.URLField(max_length=200, blank=True, null=True)
    domain = models.URLField(max_length=200, blank=True, null=True)
    session_id = models.IntegerField(default=0)

    def __str__(self):
        return self.domain

    class Meta:
        verbose_name_plural = 'Resultados'


class Google_bk_single(models.Model):
    LENGUAGE_CHOICES = (
        ('es', 'Español'),
        ('en', 'Ingles'),
        ('it', 'Italiano'),
        ('ru', 'Ruso'),
        ('ja', 'Japones'),
        ('ru', 'Rumano'),
        ('nl', 'Holandés'),
        ('ar', 'Armenio'),
        ('fr', 'Francés'),
        ('de', 'Aleman'),
        ('pl', 'Polaco'),
        ('tw', 'Taiwanes'),
        ('kr', 'Koreano'),
    )

    SITE_LINK_CHOICES = (
        ('Comentario', 'Comentario'),
        ('Articulo', 'Articulo'),
        ('Foro', 'Foro')
    )

    url_from = models.URLField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    url_to = models.URLField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200, choices=LENGUAGE_CHOICES, blank=True, null=True)
    anchor = models.CharField(max_length=200, blank=True, null=True)
    nofollow = models.BooleanField(blank=True)
    site_link = models.CharField(max_length=200, choices=SITE_LINK_CHOICES, blank=True, null=True)
    session_id = models.IntegerField(default=0)


    def __str__(self):
        return self.url_from

    class Meta:
        verbose_name_plural = 'Backlinks del sitio'


class CSV_import(models.Model):
    LENGUAGE_CHOICES = (
        ('es', 'Español'),
        ('en', 'Ingles'),
        ('it', 'Italiano'),
        ('ru', 'Ruso'),
        ('ja', 'Japones'),
        ('ru', 'Rumano'),
        ('nl', 'Holandés'),
        ('ar', 'Armenio'),
        ('fr', 'Francés'),
        ('de', 'Aleman'),
        ('pl', 'Polaco'),
        ('tw', 'Taiwanes'),
        ('kr', 'Koreano'),
        ('pt', 'Portugues'),
    )

    SITE_LINK_CHOICES = (
        ('Comentario', 'Comentario'),
        ('Articulo', 'Articulo'),
        ('Foro', 'Foro')
    )

    document = models.CharField(max_length=200, blank=True, null=True)
    domain = models.URLField(max_length=200, blank=True, null=True)
    backlink = models.URLField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200, choices=LENGUAGE_CHOICES, blank=True, null=True)
    url_to = models.URLField(max_length=200, blank=True, null=True)
    site_link = models.CharField(max_length=200, choices=SITE_LINK_CHOICES, blank=True, null=True)
    foro = models.BooleanField(blank=True, default=False)
    nofollow = models.BooleanField(blank=True, default=False)
    session_id = models.IntegerField(default=0)

    def __str__(self):
        return self.domain


class ScrapperTest(models.Model):
    url = models.URLField(max_length=200, blank=True, null=True)
    foro = models.BooleanField(blank=True, default=False)
    comentario = models.BooleanField(blank=True, default=False)
    session_id = models.IntegerField(default=0)

    def __str__(self):
        return self.url


## Single URL apiv
class SingleAhref(models.Model):
    url = models.URLField(max_length=200, blank=True, null=True)
    session_id = models.IntegerField(default=0)

    def __str__(self):
        return self.url


class SingleBacklinks(models.Model):
    LENGUAGE_CHOICES = (
        ('es', 'Español'),
        ('en', 'Ingles'),
        ('it', 'Italiano'),
        ('ru', 'Ruso'),
        ('ja', 'Japones'),
        ('ru', 'Rumano'),
        ('nl', 'Holandés'),
        ('ar', 'Armenio'),
        ('fr', 'Francés'),
        ('de', 'Aleman'),
        ('pl', 'Polaco'),
        ('tw', 'Taiwanes'),
        ('kr', 'Koreano'),
    )

    SITE_LINK_CHOICES = (
        ('Comentario', 'Comentario'),
        ('Articulo', 'Articulo'),
        ('Foro', 'Foro')
    )

    url_from = models.URLField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    url_to = models.URLField(max_length=200, blank=True, null=True)
    language = models.CharField(max_length=200, choices=LENGUAGE_CHOICES, blank=True, null=True)
    anchor = models.CharField(max_length=200, blank=True, null=True)
    nofollow = models.BooleanField(blank=True)
    site_link = models.CharField(max_length=200, choices=SITE_LINK_CHOICES, blank=True, null=True)
    foro = models.BooleanField(blank=True, default=False)
    session_id = models.IntegerField(default=0)


    def __str__(self):
        return self.url_from

    class Meta:
        verbose_name_plural = 'Backlinks del sitio'


class TokenAhref(models.Model):
    token = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return 'Token: {}'.format(self.token)

    class Meta:
        verbose_name_plural = 'Token'
