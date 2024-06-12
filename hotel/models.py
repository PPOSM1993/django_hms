from django.db import models
from user_auth.models import User
from shortuuid.django_fields import ShortUUIDField
from django.utils.text import slugify
import shortuuid
from django.utils.html import mark_safe
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.


HOTEL_STATUS = (
    ("Draft", "Draft"),
    ("Disabled", "Disabled"),
    ("Rejected", "Rejected"),
    ("In Review", "In Review"),
    ("Live", "Live"),
)

ICON_TYPE = (
    ("Bootstrap Icons", "Bootstrap Icons"),
    ("Font awesome Icons", "Font awesome Icons"),
    ("Box Icons", "Box Icons"),
    ("Remi Icons", "Remi Icons"),
    ("Flat Icons", "Flat Icons"),
)

PAYMENT_STATUS = (
    ("Paid", "Paid"),
    ("Pending", "Pending"),
    ("Processing", "Processing"),
    ("Cancelled", "Cancelled"),
    ("Initiated", "Initiated"),
    ("Failed", "Failed"),
    ("Refunding", "Refunding"),
    ("Refunded", "Refunded"),
    ("Unpaid", "Unpaid"),
    ("Expired", "Expired"),
)


RATING = (
    (1, "One Star"),
    (2, "Two Star"),
    (3, "Three Star"),
    (4, "Four Star"),
    (5, "Five Star"),
)



class Hotel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100)
    description = CKEditor5Field(null=True, blank=True)
    image = models.FileField()
    address = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    status =models.CharField(max_length=20, choices=HOTEL_STATUS, default="Live")

    tags = models.CharField(max_length=200, help_text="Separate tags with comma")
    views = models.IntegerField(default=0)
    featured = models.BooleanField(default = False)
    hid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghijlmnopqrstvwxyz123")
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:4]
            self.slug = slugify(self.name) + '-' + str(uniqueid.lower())

            #a-b-c-d
        super(Hotel, self).save(*args, **kwargs)

    def thumbnail(self):
        return mark_safe("<img src='%s' width='50' height='50' style='object-fit: cover; border-radius: 6px; />" % (self.image.url))




class HotelGallery(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.FileField(upload_to="hotel_galley")
    hgid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghijlmnopqrstvwxyz123")


    def __str__(self):
        return str(self.hotel.name)
    
    class Meta:
        verbose_name_plural = "Hotel Gallery"

class HotelFeatures(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    icon_type = models.CharField(max_length=100, null=True, choices=ICON_TYPE)
    icon = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.hotel.name)
    
    class Meta:
        verbose_name_plural = "Hotel Features"

class HotelFaqs(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return str(self.question)
    
    class Meta:
        verbose_name_plural = "Hotel FAQs"

class RoomType(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    number_of_beds = models.PositiveIntegerField(default=0)
    room_capacity = models.PositiveIntegerField(default=0)
    rtid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghijlmnopqrstvwxyz123")
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.hotel.name} - {self.price}"
    
    class Meta:
        verbose_name_plural = "Room Type"

    
    def rooms_count(self):
        Room.objects.filter(room_type=self).count()
    

    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:4]
            self.slug = slugify(self.name) + '-' + str(uniqueid.lower())


        super(RoomType, self).save(*args, **kwargs)

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=1000)
    is_available = models.BooleanField(default=True)
    rid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghijlmnopqrstvwxyz123")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} - {self.hotel.name} - {self.price}"
    
    class Meta:
        verbose_name_plural = "Rooms"

    def price(self):
        return self.room_type.price
    
    def number_of_beds(self):
        return self.room_type.number_of_beds



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS)

    full_name = models.CharField(max_length=1000)
    email = models.EmailField(max_length=1000)
    phone = models.CharField(max_length=1000)

    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, null=True, blank=True)
    room = models.ManyToManyField(Room)
    before_discount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    saved = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    check_in_date = models.DateField()
    check_out_date = models.DateField()

    total_days = models.PositiveIntegerField(default=0)
    num_adults = models.PositiveIntegerField(default=1)
    num_children = models.PositiveIntegerField(default=1)


    check_in = models.BooleanField(default=False)
    check_out = models.BooleanField(default=False)

    is_activate = models.BooleanField(default=False)

    check_in_tracker = models.BooleanField(default=False)
    check_out_tracker = models.BooleanField(default=False)


    date = models.DateTimeField(auto_now_add=True)
    stripe_payment_intent = models.CharField(max_length=1000, null=True, blank=True)
    success_id = models.CharField(max_length=1000, null=True, blank=True)
    booking_id = ShortUUIDField(unique=True, length=10, max_length=20, alphabet="abcdefghijlmnopqrstvwxyz123")

    def __str__(self):
        return f"{self.booking_id}"
    
    def rooms(self):
        return self.room.all().count()
    

class Activity(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    guess_out = models.DateTimeField()
    guess_in = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking}"

class StaffOnDuty(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff_id}"
    