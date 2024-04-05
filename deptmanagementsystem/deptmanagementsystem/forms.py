from django import forms
from .models import Forum, Marks, Student, User

class LoginForm(forms.Form):
    usrname = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20)

#use this to add topic of forum
class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['header', 'content',]
    
#further IDEA
# show only titles on display
# when clicked go to its details page where person is allowed to add comments


class MarksForm(forms.ModelForm):
    class Meta: 
        model = Marks
        fields = ['cgp']

class CommentForm(forms.Form):
    new_comment = forms.CharField(label='New Comment', max_length=200, required=False)


class StudentForm(forms.Form):

    name = forms.CharField(max_length=20)
    description = forms.CharField(max_length=100)


class UserForm(forms.ModelForm):
    class Meta:
        model = User  # Use your custom User model if needed
        fields = ['username', 'email', 'password', 'userType']