from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):

    class Meta:

        model = ContactMessage

        fields = (
            "name",
            "email",
            "subject",
            "message",
        )

        widgets = {

            "name": forms.TextInput(

                attrs={
                    "class": "w-full rounded-xl bg-slate-900 border border-slate-700 px-5 py-4 text-white focus:outline-none focus:border-cyan-400",
                    "placeholder": "Your Name"
                }

            ),

            "email": forms.EmailInput(

                attrs={
                    "class": "w-full rounded-xl bg-slate-900 border border-slate-700 px-5 py-4 text-white focus:outline-none focus:border-cyan-400",
                    "placeholder": "Email Address"
                }

            ),

            "subject": forms.TextInput(

                attrs={
                    "class": "w-full rounded-xl bg-slate-900 border border-slate-700 px-5 py-4 text-white focus:outline-none focus:border-cyan-400",
                    "placeholder": "Subject"
                }

            ),

            "message": forms.Textarea(

                attrs={
                    "rows": 6,
                    "class": "w-full rounded-xl bg-slate-900 border border-slate-700 px-5 py-4 text-white focus:outline-none focus:border-cyan-400",
                    "placeholder": "Write your message..."
                }

            )

        }