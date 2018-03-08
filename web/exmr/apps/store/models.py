from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class StoreCategory(models.Model):
    """
    Model for store category
    """
    name = models.CharField(_('name'), max_length=255)
    publish = models.BooleanField(_('publish'), default=True)
    image = models.ImageField(verbose_name=_('image'), upload_to='store/category')

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Store(models.Model):
    """
    Model for store information
    """
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='get_user_stores', on_delete=models.CASCADE)
    store_name = models.CharField(_('store name'), max_length=255)
    store_url = models.URLField(_('store url'))
    category = models.ForeignKey(StoreCategory, verbose_name=_('category'), related_name='get_store_category', on_delete=models.CASCADE)
    crypto_processor = models.CharField(_('crypto processor'), max_length=255)
    store_email = models.EmailField(_('store email'))
    keywords = models.CharField(_('keywords'), max_length=255, null=True, blank=True)
    banner_image_url = models.URLField(_('banner image url'))
    is_approved = models.BooleanField(_('is approved'), default=False)

    class Meta:
        verbose_name = _('Store')
        verbose_name_plural = _('Stores')

    def __str__(self):
        return self.store_name
