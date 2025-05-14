from modeltranslation.translator import register, TranslationOptions

from apps.blog.models import Post
@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content')