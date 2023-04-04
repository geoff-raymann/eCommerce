from django.db import models
from django.urls import reverse
from parler.models import TranslatableModel, TranslatedFields

# Create your models here.

class Category(TranslatableModel):
    translations = TranslatedFields(
        name =  models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, unique=True)
    )
    
    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
    

    
class Product(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=200, db_index=True),
        slug = models.SlugField(max_length=200, db_index=True),
        short_intro = models.CharField(max_length=200, blank=True),
        description = models.TextField(blank=True)
    )
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image5 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image6 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image7 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    video1 = models.FileField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    video2 = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ('name',)
    #     index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
