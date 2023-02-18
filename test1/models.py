from django.db import models

# Create your models here.


class Location(models.Model):
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.city


class Network(models.Model):
    gbfs_href = models.URLField()
    href = models.CharField(max_length=255)
    id = models.CharField(primary_key=True, max_length=255)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)  # 1
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company(models.Model):  # 2
    network = models.ForeignKey(Network, on_delete=models.CASCADE)  # 4
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Payment(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Extra(models.Model):
    address = models.CharField(max_length=255)
    altitude = models.FloatField()
    ebikes = models.IntegerField()
    has_ebikes = models.BooleanField()
    last_updated = models.IntegerField()
    normal_bikes = models.IntegerField()
    payments = models.ManyToManyField(Payment)  # 4
    payment_terminal = models.BooleanField()
    post_code = models.CharField(max_length=255, blank=True)
    renting = models.IntegerField()
    returning = models.IntegerField()
    slots = models.IntegerField()
    uid = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.uid


class Station(models.Model):
    network = models.ForeignKey(Network, on_delete=models.CASCADE)
    empty_slots = models.IntegerField()
    extra = models.OneToOneField(Extra, on_delete=models.CASCADE)
    free_bikes = models.IntegerField()
    id = models.CharField(primary_key=True, max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.name

















