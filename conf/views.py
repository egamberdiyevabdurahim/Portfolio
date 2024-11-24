from django.views import generic
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse_lazy

from common.models import StartsWithIAMModel, SkillModel, PortfolioModel, SocialModel, MainModel, ContactModel
from conf.forms import ContactModelForm


class HomePageView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        starts_with_iam = StartsWithIAMModel.objects.filter(is_deleted=False)
        skills = SkillModel.objects.filter(is_deleted=False)
        portfolio = PortfolioModel.objects.filter(is_deleted=False)
        socials = SocialModel.objects.filter(is_deleted=False)
        main = MainModel.objects.first()

        context['starts_with_iam'] = ', '.join(item.name for item in starts_with_iam)

        skill = len(skills) // 2
        skill2 = len(skills) % 2

        context['skills'] = [
            skills[:skill + skill2],
            skills[skill + skill2:]
        ]

        context['portfolios'] = portfolio
        context['socials'] = socials
        context['main'] = main

        if main and main.born_date:
            birth_date = main.born_date
            today = timezone.now().date()
            context['age'] = today.year - birth_date.year - (
                        (today.month, today.day) < (birth_date.month, birth_date.day))
        else:
            context['age'] = None

        return context


class PortfolioPageView(generic.DetailView):
    model = PortfolioModel
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch related images
        context['images'] = self.object.images.all()
        main = MainModel.objects.first()
        context['main'] = main
        return context


class ContactView(generic.CreateView):
    model = ContactModel
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = reverse_lazy('home')
    success_message = 'Your message has been sent.'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(self.request, 'There was an error with your submission.')
        return response
