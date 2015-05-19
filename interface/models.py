from django.db import models

# Create your models here.


class ServiceProvider(models.Model):
    name = models.CharField(max_length=200, null=False)
    website = models.URLField(max_length=100, null=True)
    phone_number = models.CharField(max_length=10, null=True)
    address = models.TextField(null=True)
    hours_of_operation = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class ServiceCategory(models.Model):
    name = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Item(models.Model):
    name = models.CharField(max_length=100, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, default=None)
    providers = models.ManyToManyField("ServiceProvider", related_name="items")
    categories = models.ManyToManyField("ServiceCategory", related_name="items")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Link(models.Model):
    url = models.URLField(null=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.pk == 1:
            return "Recycling Depot Link"
        elif self.pk == 2:
            return "Recycling Bin Link"
        return "Unknown Link"