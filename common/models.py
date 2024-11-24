from django.db import models


class StartsWithIAMModel(models.Model):
    name = models.CharField(max_length=100)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Starts with IAM Models"
        verbose_name = "Starts with IAM Model"


class SkillModel(models.Model):
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PortfolioImagesModel(models.Model):
    image = models.ImageField(upload_to='portfolio/images/')

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name_plural = "Portfolio Images"
        verbose_name = "Portfolio Image"


class PortfolioModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    images = models.ManyToManyField(PortfolioImagesModel)
    image = models.ImageField(upload_to="test", null=True)
    url = models.URLField(null=True)
    client = models.CharField(max_length=255)
    date = models.DateField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Portfolio Models"
        verbose_name = "Portfolio Model"


class SocialModel(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    icon = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Social Models"
        verbose_name = "Social Model"


class MainModel(models.Model):
    name = models.CharField(max_length=100)
    name_for_full = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='logo/default/')
    big_logo = models.ImageField(upload_to='logo/big/')
    mid_logo = models.ImageField(upload_to='logo/mid/')
    about_description = models.TextField()
    about_2_description = models.TextField()
    about_3_description = models.TextField()
    title_for_about = models.CharField(max_length=255)
    website = models.URLField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=255)
    degree = models.CharField(max_length=64)
    email = models.EmailField()
    freelancer = models.CharField(max_length=255)
    happy_clients_count = models.PositiveBigIntegerField()
    projects_count = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    born_date = models.DateField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Main Models"
        verbose_name = "Main Model"


class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Contact Models"
        verbose_name = "Contact Model"
