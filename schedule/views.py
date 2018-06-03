from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm, CandidateForm


class Home(LoginView):
    template_name = 'schedule/Home.html'
    form_class = UserForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        if self.request.user.has_perm('schedule.can_access_hr'):
            return reverse_lazy('hrworkarea')
        else:
            return reverse_lazy('workarea')


class Logout(LogoutView):
    next_page = reverse_lazy('Home')


class WorkArea(LoginRequiredMixin, generic.TemplateView):
    template_name = 'schedule/WorkArea.html'
    login_url = reverse_lazy('Home')


class HRWorkArea(LoginRequiredMixin, generic.TemplateView):
    template_name = 'schedule/HRWorkArea.html'
    login_url = reverse_lazy('Home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CandidateForm
        return context


class CreateCandidate(generic.FormView):
    template_name = 'schedule/HRWorkArea.html'
    form_class = CandidateForm
    success_url = reverse_lazy('hrworkarea')

    def form_valid(self, form):
        form.save(commit=False)
        form.added_by_id = self.request.user.id
        interviewer_name = form.interviewed_by
        if interviewer_name == ' ':
            form.interviewed_by = None
        else:
            interviewer = User.objects.get(username=interviewer_name)
            form.interviewed_by = interviewer.id
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        form = form
        return super().form_valid(form)
