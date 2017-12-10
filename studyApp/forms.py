from django import forms


def min_length_3_validator(value):
    if len(value)<3:
        raise forms.ValidationError('3글자 이상으로 입력해주세요')


class StudyForm(forms.Form):
    title = forms.CharField(validators=[min_length_3_validator])
    content = forms.CharField(widget=forms.Textarea)
    book = forms.CharField()
    status = forms.CheckboxInput()