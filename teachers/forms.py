from django import forms
from django.db.models.functions import Trunc

from users.models import Teacher_profile
from teachers.models import Complaints, TeachersComplaints


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = TeachersComplaints
        fields = ('teacher_name', 'complaint')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        complaints = Complaints.objects.all()

        self.dict_comp = {complaint.name_complaint: complaint.id for complaint in complaints}

        choices = [(complaint.name_complaint, complaint.name_complaint) for complaint in complaints]

        self.fields['complaint'] = forms.ChoiceField(choices=choices, label="Complaint")

        self.fields['teacher_name'] = forms.CharField(label="Teacher Name")

    def clean_complaint(self):
        complaint_key = self.cleaned_data.get('complaint')
        complaint_id = self.dict_comp.get(complaint_key)
        if complaint_id:
            try:
                return Complaints.objects.get(pk=complaint_id)
            except Complaints.DoesNotExist:
                raise forms.ValidationError("Invalid complaint selected.")
        raise forms.ValidationError("Invalid complaint selected.")

    def clean_teacher_name(self):
        teacher_name_key = self.cleaned_data.get('teacher_name')
        teacher_obj = Teacher_profile.objects.get(username=teacher_name_key)
        if teacher_obj:
            try:
                return Teacher_profile.objects.get(pk=teacher_obj.id)
            except Teacher_profile.DoesNotExist:
                raise forms.ValidationError("Invalid teacher name selected.")
        raise forms.ValidationError("Invalid teacher name selected.")

