from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField('Category name', max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):

    name = models.CharField('Subcategory name', max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_cat')

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'


    def __str__(self) -> str:
        return self.name

class SubSubCategory(models.Model):

    name = models.CharField('Subcategory name', max_length=50)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='sub_sub')

    class Meta:
        verbose_name = 'SubSubCategory'
        verbose_name_plural = 'SubSubCategories'


    def __str__(self) -> str:
        return self.name