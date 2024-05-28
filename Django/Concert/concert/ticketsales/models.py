from django.db import models

class Concert(models.Model):
    class Meta:
        verbose_name = "Concert"
        verbose_name_plural = "Concerts"

    name = models.CharField(max_length=100, verbose_name="Concert Name")
    singer_name = models.CharField(max_length=100, verbose_name="Singer Name")
    length = models.IntegerField(verbose_name="Concert Duration")
    poster = models.ImageField(upload_to="concertImages/", null=True, verbose_name="Poster")

    def __str__(self):
        return self.singer_name

class Location(models.Model):
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    name = models.CharField(max_length=100, verbose_name="Location Name")
    address = models.CharField(max_length=500, default="Tehran-Milad Tower", verbose_name="Location Address")
    phone = models.CharField(max_length=11, null=True, verbose_name="Phone Number")
    capacity = models.IntegerField(verbose_name="Capacity")

    def __str__(self):
        return self.name

class Time(models.Model):
    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"

    concert = models.ForeignKey(Concert, on_delete=models.PROTECT, verbose_name="Concert")
    location = models.ForeignKey(Location, on_delete=models.PROTECT, verbose_name="Location")
    start_date_time = models.DateTimeField(verbose_name="Start Date and Time")
    seats = models.IntegerField(verbose_name="Number of Seats")

    STATUS_CHOICES = [
        ("Start", "Ticket Sales Started"),
        ("End", "Ticket Sales Ended"),
        ("Cancel", "Canceled"),
        ("Sales", "Selling")
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Concert Status")

    def __str__(self):
        return "Time: {} ConcertName: {} Location: {}".format(self.start_date_time, self.concert.name, self.location.name)

class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    name = models.CharField(max_length=100, verbose_name="First Name")
    family = models.CharField(max_length=100, verbose_name="Last Name")

    GENDER_CHOICES = [
        ("man", "Male"),
        ("woman", "Female")
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Gender")
    profile_image = models.ImageField(upload_to="ProfileImages/", verbose_name="Profile Image")

    def __str__(self):
        return "FullName: {} {}".format(self.name, self.family)

class Ticket(models.Model):
    class Meta:
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"

    profile = models.ForeignKey(Profile, on_delete=models.PROTECT, verbose_name="Profile")
    time = models.ForeignKey(Time, on_delete=models.PROTECT, verbose_name="Time")

    name = models.CharField(max_length=100, verbose_name="Title")
    price = models.IntegerField(verbose_name="Price")
    ticket_image = models.ImageField(upload_to="TicketImages/", verbose_name="Ticket Image")

    def __str__(self):
        return "TicketInfo: Profile: {} ConcertInfo: {}".format(self.profile, self.time)

