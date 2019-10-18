from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=10, min_length=3, initial='I love you sites',help_text='提示信息',label='项目')
    email = forms.EmailField(required=False,label='邮件地址')
    message = forms.CharField(widget=forms.Textarea, min_length=3)

    # def clean_message(self):
    #     message = self.cleaned_data['message']
    #     num_words = len(message.split())
    #     if num_words < 4:
    #         raise forms.ValidationError("Not enough words!")
    #     return message

    def clean_message(self):
        massage = self.cleaned_data['message']
        if massage:
            a = '我'
        return a
