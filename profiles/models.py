from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture=models.ImageField("Imagen de perfil", upload_to="profile_pictures/",blank=True,null=True)
    bio=models.TextField("Biografia",max_length=500,blank=True)
    birth_date = models.DateField("Fecha de nacimiento", null=True, blank=True)
    followers=models.ManyToManyField("self",symmetrical=False,related_name="following",through="follow")


    class Meta:
        verbose_name="perfil"
        verbose_name_plural="perfiles"

    def __str__(self):
        return self.user.username 
    

    def follow(self,profile):
        Follow.objects.get_or_create(follower=self,following=profile)


    
class Follow(models.Model):
    follower=models.ForeignKey(UserProfile,verbose_name="¿Quien sigue?", on_delete=models.CASCADE, related_name="follower_set")
    following=models.ForeignKey(UserProfile,verbose_name="¿A quien sigue?",on_delete=models.CASCADE, related_name="following_set")
    created_at=models.DateTimeField(auto_now_add=True ,verbose_name="¿Desde cunado lo sigue")

    class Meta :
        unique_together= ("follower","following")

    def __str__(self):
        return f"{self.follower} follows {self.following}"
    
    class Meta:
        verbose_name="seguidor"
        verbose_name_plural="seguidores"