from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Rewards(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=2)
    # activity = models.TextField()

    def __str__(self) -> str:
        return f"{self.user.username} - {self.points}"


class TreeShop(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Tree(models.Model):
    shop = models.ForeignKey(TreeShop, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='trees')
    date_uploaded = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class TreeOrder(models.Model):
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    location = models.PointField()
    date_added = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.tree.name


class RecycleArea(models.Model):
    name = models.CharField(max_length=255)
    location = models.PointField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    location = models.PointField(null=True,blank=True)

    def __str__(self) -> str:
        return self.user.username


class Campaign(models.Model):
    name = models.CharField(max_length=255)
    date_started = models.DateTimeField(auto_now_add=True)
    location = models.PointField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class CampaignInvolvement(models.Model):
    user = models.ForeignKey(User, on_delete=models.ForeignKey)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    date_involved = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'campaign')
