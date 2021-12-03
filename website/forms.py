from django import forms
from website.models import Contact, Newsletter
from captcha.fields import CaptchaField


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["subject"].required = False

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"
