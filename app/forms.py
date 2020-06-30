from django.forms import  ModelForm
from app.models import  Moment
class MomentForm(ModelForm):
	class Meta:
		model=Moment
		fields='__all__'#导入所有字段
	def clean(self):
		cleaned_data=super(MomentForm, self).clean()
		content=cleaned_data.get("content")
		if content is None:
			raise  ValueError("请输入Content内容")
		elif content.find("ABCD")>0:
			raise ValidationError("不能输入敏感字ABCD！")
		return  cleaned_data