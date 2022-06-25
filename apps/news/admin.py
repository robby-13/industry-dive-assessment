from django import forms
from django.contrib import admin
from news.models import NewsPost

options = [(False, 'False'), (True, 'True')]
class NewsPostForm(forms.ModelForm):
    model = NewsPost
    is_cover_story = forms.ChoiceField(choices=options, widget=forms.RadioSelect)
    fields = ['title', 'source_divesite', 'is_cover_story', 'active']



class NewsPostAdmin(admin.ModelAdmin):
    form = NewsPostForm
    list_display = ['title', 'source_divesite', 'is_cover_story', 'active']
    list_editable = ['is_cover_story', 'active']


admin.site.register(NewsPost, NewsPostAdmin)
