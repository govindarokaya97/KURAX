from django import forms
from news_app.models import Contact, Comment, Newsletter


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "comment"]

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"