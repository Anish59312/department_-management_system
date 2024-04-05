from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = [
        ("prof", "Professor"),
        ("stud", "Student"),
        ("hod", "Head of Department"),
        ("clerk", "Clerk"),
    ]
    userType = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=USER_TYPE_CHOICES[1][1]) #default is student


class Student(models.Model):
    name = models.CharField(max_length=20) 
    batchId = models.IntegerField(null=True) #batchno(1,2) + semisternumber(1-8)
    # sem = models.IntegerField()
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class Marks(models.Model):
    cgp = models.FloatField(default=0)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True )

    def __str__(self):
        return f"CGP: {self.cgp}"


class Professor(models.Model):
    name = models.CharField(max_length=20)

class DailySchedule(models.Model):
    batch_no = models.IntegerField()
    timeslot = models.CharField(max_length=20)
    # timeslot = fromTime-toTime

    def __str__(self):
        return str(self.__dict__)


# class ForumPost(models.Model):
#     forumType = models.IntegerField() #convert this to choices
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     creator = models.ForeignKey(User.userName, on_delete=models.CASCADE, related_name='forum_posts')


# class Comment(models.Model):
#     content = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments')
#     commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')


class Forum(models.Model):
    header = models.CharField(max_length=200)
    content = models.TextField(default="")
    comments = models.JSONField(default = list)

    def __str__(self):
        return self.header
    
    def add_comment(self, new_comment):
        self.comments.append(new_comment)
        self.save()


# class Article(models.Model):
#     title = models.CharField(max_length = 100)

#     def __str__(self):
#         return self.title
    


class Complaints(models.Model):
    subject = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Subject: {self.subject}, Description: {self.description}" 
