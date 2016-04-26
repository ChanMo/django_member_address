from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.core.urlresolvers import reverse_lazy
from wechat_member.views import WxMemberView
from .models import *

class AddressListView(WxMemberView, ListView):
    model = Address
    template_name = 'address/index.html'
    def get_queryset(self):
        return Address.objects.filter(member=self.wx_member)

class AddressDetailView(WxMemberView, DetailView):
    model = Address
    template_name = 'address/detail.html'

class AddressCreateView(WxMemberView, CreateView):
    model = Address
    fields = ['name', 'mobile', 'location', 'address', 'longitude', 'latitude']
    def form_valid(self, form):
        form.instance.member = self.wx_member
        return super(AddressCreateView, self).form_valid(form)
    def get_success_url(self):
        return reverse_lazy('address:list')

class AddressUpdateView(WxMemberView, UpdateView):
    model = Address
    fields = ['name', 'mobile', 'location', 'address', 'longitude', 'latitude']
    success_url = reverse_lazy('address:list')
