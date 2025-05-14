from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from apps.base.models import BaseModel
from django.utils.text import slugify

User = get_user_model()


class Category(BaseModel):
    name = models.CharField(_("Category name"), max_length=100)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(_("Tag name"), max_length=50)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), unique=True)
    description = models.CharField(_("Short description"), max_length=255)
    content = models.TextField(_("Content"))
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name=_("Category"),
        related_name="posts",
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_("Author"), related_name="posts"
    )
    tags = models.ManyToManyField(
        Tag, through="PostTag", verbose_name=_("Tags"), related_name="posts"
    )

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.title


class PostTag(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=_("Post"))
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name=_("Tag"))

    class Meta:
        unique_together = ("post", "tag")
        verbose_name = _("Post Tag")
        verbose_name_plural = _("Post Tags")
