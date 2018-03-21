import pytz

from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site

from apps.accounts.models import Profile

CHOICES = [(pytz.timezone(tz), tz) for tz in pytz.common_timezones]


MALE = 0
FEMALE = 1
OTHER = 2

GENDER_CHOICES = [(MALE, _('Male')),
    (FEMALE, _('Female')),
    (OTHER, _('Other/Prefer Not to say')),]


class SignUpForm(UserCreationForm):

    email = forms.EmailField()
    confirm_email = forms.EmailField()
    timezone = forms.ChoiceField(choices=CHOICES)
    need_newsletter = forms.BooleanField(required=False)
    accept_terms_and_conditions = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2', 'confirm_email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if self and User.objects.filter(email=email).exists():
            raise forms.ValidationError(u'Please use a different email address.')
        return email

    def clean_confirm_email(self):
        if self.cleaned_data.get('email') != self.cleaned_data.get('confirm_email'):
            return forms.ValidationError(_("Emails doesn't match"))
        return self.cleaned_data.get('confirm_email')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        return username

    def clean_accept_terms_and_conditions(self):
        if not self.cleaned_data.get('accept_terms_and_conditions'):
            raise forms.ValidationError(_('Please accept the terms and conditions'))
        return self.cleaned_data.get('accept_terms_and_conditions')



class UpdateBasicProfileForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    confirm_email = forms.EmailField(required=False)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    timezone = forms.ChoiceField(choices=CHOICES)
    date_format = forms.CharField(required=False)
    date_format_second = forms.CharField(required=False)
    time_format = forms.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['gender', 'timezone', 'date_format', 'time_format', 'email', 'confirm_email']

    def __init__(self, *args, **kwargs):
        super(UpdateBasicProfileForm, self).__init__(*args, **kwargs)
        self.fields['timezone'].widget.attrs['class'] = 'form-control select-view'
        self.fields['email'].widget.attrs['class'] = 'form-control text-view'
        self.fields['confirm_email'].widget.attrs['class'] = 'form-control text-view'
        self.fields['gender'].widget.attrs['class'] = 'form-control select-view'
        self.fields['date_format'].widget.attrs['class'] = 'datepicker form-control select-view date-box'
        self.fields['date_format'].widget.attrs['placeholder'] = '03/10/2018'
        self.fields['date_format_second'].widget.attrs['class'] = 'datepicker form-control select-view date-box second-date'
        self.fields['date_format_second'].widget.attrs['placeholder'] = '03/10/2018'
        self.fields['time_format'].widget.attrs['data-format'] = "hh:mm:ss"
        self.fields['time_format'].widget.attrs['class'] = 'timepicker form-control select-view'
        self.fields['time_format'].widget.attrs['placeholder'] = '05:30'

    def clean_confirm_email(self):
        cleaned_data = super(UpdateBasicProfileForm, self).clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")
        if email and confirm_email:
            if email != confirm_email:
                raise forms.ValidationError("Emails do not match.")
        return cleaned_data

class CustomPasswordResetForm(PasswordResetForm):

    username = forms.CharField(required=False)
    email = forms.EmailField(required=False)

    fields = ('username', 'email', )

    def clean(self):
        if not self.cleaned_data.get('username') and not self.cleaned_data.get('email'):
            raise forms.ValidationError(_('Either username or email needs to be provided'))

    def get_users(self, email):
        """Given an email, return matching user(s) who should receive a reset.

        This allows subclasses to more easily customize the default policies
        that prevent inactive users and users with unusable passwords from
        resetting their password.
        """
        active_users = User._default_manager.filter(**{
            '%s__iexact' % User.get_email_field_name(): email,
            'is_active': True,
        })
        return (u for u in active_users if u.has_usable_password())


    def save(self, domain_override=None,
             subject_template_name='registration/password_reset_subject.txt',
             email_template_name='registration/password_reset_email.html',
             use_https=False, token_generator=default_token_generator,
             from_email=None, request=None, html_email_template_name=None,
             extra_email_context=None):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        email = self.cleaned_data.get("email")
        username = self.cleaned_data.get('username')
        if email:
            users = self.get_users(email)
        else:
            users = User.objects.filter(username=username, is_active=True)
            email = users[0].email
        for user in self.get_users(email):
            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override
            context = {
                'email': email,
                'domain': domain,
                'site_name': site_name,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': 'https' if use_https else 'http',
            }
            if extra_email_context is not None:
                context.update(extra_email_context)
            self.send_mail(
                subject_template_name, email_template_name, context, from_email,
                email, html_email_template_name=html_email_template_name,
            )

