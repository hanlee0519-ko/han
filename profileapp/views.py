from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        temp_profile = form.save(commit=False) # 임시저장
        temp_profile.user = self.request.user # 서버 내에서 구현 / 클라이언트에서 유저를 정해서 구현하게 되면, 잘못하게 만들 수 있기에
        temp_profile.save()
        return super().form_valid(form)