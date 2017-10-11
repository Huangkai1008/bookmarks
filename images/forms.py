from django import forms

from .models import Image


class ImageCreateForm(forms.ModelForm):
    """
    创建一个表单使得用户可以自主上传自己喜欢的图片用作分享
    """
    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {
            'url': forms.HiddenInput,
        }

    def clean_url(self):
        """
        >清洁表单字段
        使得用户上传的图片会被筛选，判断用户输入的url是否合法
        :return:
        """
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('提供的链接不符合image的扩展格式')

