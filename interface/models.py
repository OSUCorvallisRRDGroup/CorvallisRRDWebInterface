from django.db import models


class Settings(models.Model):
    settings = ['username', 'password']
    key = models.CharField(max_length=20)
    value = models.CharField(max_length=200)


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
    providers = models.ManyToManyField("ServiceProvider", related_name="items", through='ServiceProviderItem')
    categories = models.ManyToManyField("ServiceCategory", related_name="items", through='ServiceCategoryItem')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class ServiceProviderItem(models.Model):
    serviceProvider = models.ForeignKey(ServiceProvider)
    item = models.ForeignKey(Item)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, default=None)


class ServiceCategoryItem(models.Model):
    serviceCategory = models.ForeignKey(ServiceCategory)
    item = models.ForeignKey(Item)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(null=True, default=None)


class Link(models.Model):
    url = models.URLField(null=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.pk == 1:
            return "Recycling Depot Link"
        elif self.pk == 2:
            return "Recycling Bin Link"
        return "Unknown Link"