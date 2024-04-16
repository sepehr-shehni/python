from django.db import models


# Create your models here.

class concertModel(models.Model):
    class Meta:
        verbose_name = "کنسرت"
        verbose_name_plural = "کنسرت"

    Name = models.CharField(max_length=100, verbose_name="نام کنسرت")
    Singer_Name = models.CharField(max_length=100, verbose_name="نام خواننده")
    length = models.IntegerField(verbose_name="مدت زمان کنسرت")
    Poster = models.ImageField(upload_to="concertImages/", null=True, verbose_name="پوستر")

    def __str__(self):
        return self.Singer_Name


class locationModel(models.Model):
    class Meta:
        verbose_name = "محل برگزاری"
        verbose_name_plural = "محل برگزاری"

    Name = models.CharField(max_length=100, verbose_name="نام محل")
    Address = models.CharField(max_length=500, default="تهران-برج میلاد", verbose_name="محل برگزاری")
    Phone = models.CharField(max_length=11, null=True, verbose_name="شماره تماس")
    capacity = models.IntegerField(verbose_name="ظرفیت")

    def __str__(self):
        return self.Name


class timeModel(models.Model):
    class Meta:
        verbose_name = "سانس برگزاری"
        verbose_name_plural = "سانس برگزاری"


    concertModel = models.ForeignKey(to=concertModel, on_delete=models.PROTECT,verbose_name="کنسرت")
    locationModel = models.ForeignKey(to=locationModel, on_delete=models.PROTECT,verbose_name="محل برگزاری")
    StartDateTime = models.DateTimeField(verbose_name="تاریخ برگزاری")
    Seats = models.IntegerField(verbose_name="تعداد صندلی")

    Start = 1
    End = 2
    Cancel = 3
    Sales = 4

    Status_Choices = ((Start, "فروش بلیط شروع شده است"),
                      (End, "فروش بلیط تمام شده است"),
                      (Cancel, "این سانس کنسل شده است"),
                      (Sales, "در حال فروش بلیط"))

    Status = models.IntegerField(choices=Status_Choices, verbose_name="وضعیت کنسرت")


    def __str__(self):
        return "Time: {} ConcertName: {} Location: {}".format(self.StartDateTime, self.concertModel.Name,self.locationModel.Name)


class ProfileModel(models.Model):
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر"

    Name = models.CharField(max_length=100, verbose_name="نام")
    Family = models.CharField(max_length=100, verbose_name="نام خانوادگی")

    man = 1
    women = 2

    Status_choices = (("man", "مرد"), ("woman", "زن"))
    Gender = models.IntegerField(choices=Status_choices, verbose_name="جنسیت")
    ProfileImage = models.ImageField(upload_to="ProfileImages/", verbose_name="عکس")

    def __str__(self):
        return "FullName: {} {}".format(Name, Family)


class ticketModel(models.Model):
    class Meta:
        verbose_name = "بلیط"
        verbose_name_plural = "بلیط"

    ProfileModel = models.ForeignKey("ProfileModel", on_delete=models.PROTECT, verbose_name="کاربر")
    timeModel = models.ForeignKey("timeModel", on_delete=models.PROTECT, verbose_name="سانس")

    Name = models.CharField(max_length=100, verbose_name="عنوان")
    Price = models.IntegerField(verbose_name="مبلغ")
    TicketImage = models.ImageField(upload_to="TicketImages/", verbose_name="عکس")

    @property
    def __str__(self):
        return "TicketInfo: Profile: {} ConcertInfo: {}".format(timeModel.__str__())
