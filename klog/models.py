from django.db import models
# Create your models here.

class Blog(models.Model):
    Author = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Category = models.CharField(max_length=200)
    Image = models.ImageField(upload_to= 'uploads/', null=True, blank=True)
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
     return self.Title






class PostCategory(models.Model):
    Author = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    Category = models.CharField(max_length=200)
    # userPost= models.OneToOneField(CommentPost, null=True, on_delete=models.CASCADE)            
    Image = models.ImageField(upload_to= 'uploads/', null=True, blank=True)
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
     return self.Title

class CommentPost(models.Model):
    name=models.CharField(max_length=200)
    postCategory= models.ForeignKey(PostCategory, null=True, on_delete=models.CASCADE)
    Body = models.TextField()
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class BlogComment(models.Model):
    name=models.CharField(max_length=200)
    Blog= models.ForeignKey(Blog, null=True, on_delete=models.CASCADE)
    Body = models.TextField()
    Date_Created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return (self.name)