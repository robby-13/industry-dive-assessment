from xml.dom import ValidationErr
from django import forms
from django.contrib import admin
from news.models import NewsPost
# from django.core.exceptions import ValidationError

# options = [(False, 'False'), (True, 'True')]
class NewsPostForm(forms.ModelForm):
    model = NewsPost
    fields = '__all__'
    # is_cover_story = forms.ChoiceField(choices=options, widget=forms.RadioSelect)
    # fields = '__all__'
    # print('print')
    # cover_story = NewsPost.objects.filter(is_cover_story=True)
    
    # def clean_active(self):
    #     print('error!')



class NewsPostAdmin(admin.ModelAdmin):
    form = NewsPostForm
    list_display = ['title', 'source_divesite', 'is_cover_story', 'active']
    list_editable = ['is_cover_story', 'active']
    # cover_story = NewsPost.objects.filter(is_cover_story=True)
    # print(cover_story)
    # print(len(cover_story))
    # if len(cover_story) > 1:
    #    results = NewsPost.objects.filter(is_cover_story=True)
    #    for i in results:
    #         i.is_cover_story = False
    #         i.save()


admin.site.register(NewsPost, NewsPostAdmin)
