from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.template.defaultfilters import slugify
from .validators import validate_is_audio
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    # Resize images for thumbnail instances
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path) 

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Track(models.Model):
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    track = models.FileField(upload_to='tracks', validators=[validate_is_audio])
    artist_name = models.CharField( max_length=100)
    track_title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    cover_art = models.ImageField(default='default_cover_art.jpg', upload_to='cover_art')
    description = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(User, default=None, blank=True, related_name='track_post')
    like_count = models.BigIntegerField(default='0')
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.track_title)
        super(Track, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.artist_name} - {self.track_title}'

class Comment(models.Model):
    track = models.ForeignKey(Track, related_name='comments', on_delete=models.CASCADE)  
    author = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.track} - {self.author}'



  