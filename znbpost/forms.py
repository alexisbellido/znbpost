# from django import forms
# from django.core.mail import send_mail
# from django.contrib import messages
# from django.conf import settings
#
#
# class ContactForm(forms.Form):
#     name = forms.CharField(label='Your name', max_length=100)
#     sender = forms.EmailField(label='Your email')
#     message = forms.CharField(widget=forms.Textarea)
#     # The Honeypot
#     die_robot = forms.CharField(widget=forms.HiddenInput, required=False)
#
#     def clean_die_robot(self):
#         data = self.cleaned_data['die_robot']
#         if data:
#             raise forms.ValidationError("Shut up, Donny.")
#         return data
#
#     def send_email(self):
#         name = self.cleaned_data['name']
#         sender = self.cleaned_data['sender']
#         message = self.cleaned_data['message']
#         recipient_list = getattr(settings, 'ZNBPOST_ADMIN_EMAILS', [])
#         send_mail(
#             'Human contact!',
#             '%s said:\n%s\n' % ( name, message),
#             sender,
#             recipient_list,
#             fail_silently=False,
#         )
