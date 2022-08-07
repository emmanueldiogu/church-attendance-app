from django.db import models

# Create your models here.


class Ministry(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    leader = models.ForeignKey(
        'Member', on_delete=models.PROTECT, related_name='leader')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'ministries'


class Zone(models.Model):
    title = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Member(models.Model):
    
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'

    GENDER_CHOICES = {
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    }
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_names = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    membership_date = models.DateField(blank=True, null=True)
    tally_no = models.IntegerField()
    # photo = models.ImageField(upload_to='church/members/images/')
    is_elder = models.BooleanField(default=False)
    is_deacon = models.BooleanField(default=False)
    is_preacher = models.BooleanField(default=False)
    zone = models.ForeignKey(Zone, on_delete=models.PROTECT, null=True)
    ministry = models.ManyToManyField(Ministry, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Attendance(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    member_id = models.ForeignKey(
        Member, on_delete=models.PROTECT, related_name='member')

    def __str__(self) -> str:
        return str(self.date)

    class Meta:
        unique_together = [['date', 'member_id']]
        verbose_name_plural = 'attendance'
