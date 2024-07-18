from django import forms
from users.models import Teacher_profile
from teachers.models import Complaints, TeachersComplaints


class ComplaintForm(forms.ModelForm):
    teacher_name = forms.ModelChoiceField(queryset=Teacher_profile.objects.all(), label="Teacher")

    class Meta:
        model = TeachersComplaints
        fields = ('teacher_name', 'complaint')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Загружаем все жалобы из базы данных
        complaints = Complaints.objects.all()

        # Создаем словарь для сопоставления ключей с идентификаторами
        self.dict_comp = {complaint.name_complaint: complaint.id for complaint in complaints}

        # Создаем список кортежей для поля ChoiceField
        choices = [(complaint.name_complaint, complaint.name_complaint) for complaint in complaints]

        # Устанавливаем поле complaint как ChoiceField с новыми значениями
        self.fields['complaint'] = forms.ChoiceField(choices=choices, label="Complaint")

    def clean_complaint(self):
        complaint_key = self.cleaned_data.get('complaint')
        complaint_id = self.dict_comp.get(complaint_key)
        if complaint_id:
            try:
                return Complaints.objects.get(pk=complaint_id)
            except Complaints.DoesNotExist:
                raise forms.ValidationError("Invalid complaint selected.")
        raise forms.ValidationError("Invalid complaint selected.")
