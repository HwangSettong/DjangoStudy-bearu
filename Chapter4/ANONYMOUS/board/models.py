from django.db import models
from user.models import User # import User class of user/models.py


# Post Table
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # use the PK of user model as a FK.
    # "on_delete = models.CASCADE" : If the user is deleted, the post is also deleted.
    # "on_delete = models.CASCADE, null=True" : if the user is deleted, the post will remain, and the author will be changed to Null.

    title = models.CharField(max_length = 100)           # add post title filed
    content = models.TextField()                         # add post content filed
    reg_date = models.DateTimeField(auto_now_add = True) # add post register date filed
    img_url = models.URLField(null = True)               # add img content filed

    class Meta:
        db_table = "post" # table name is "post"

# Comment Table
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # use the PK of Post model as a FK. If the Post is deleted, Comment is also deleted.
    content = models.TextField()                         # add comment content filed
    reg_date = models.DateTimeField(auto_now_add = True) # add comment register date filed
    class Meta:
        db_table = "comment" # table name is "comment"