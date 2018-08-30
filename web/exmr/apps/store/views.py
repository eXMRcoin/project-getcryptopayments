import time
import operator

from functools import reduce

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, TemplateView, View

from apps.accounts.decorators import check_2fa
from apps.accounts.models import Profile
from apps.store.forms import AddStoreForm
from apps.store.models import StoreCategory, Store, StorePaymentRec
from apps.coins.models import Coin
from apps.coins.utils import create_wallet


class StoreCategoryListView(ListView):

    template_name = 'store/store_categories.html'
    model = StoreCategory
    queryset = StoreCategory.objects.filter(publish=True)
    context_object_name = 'categories'


class StoreListView(ListView):
    template_name = 'store/store_listing.html'
    model = Store
    context_object_name = 'stores'

    def get_context_data(self,*args,**kwargs):
        q = self.request.GET.get('q')
        slug = self.kwargs.get('slug')
        context = super(StoreListView, self).get_context_data(**kwargs)
        if slug:
            self.category = get_object_or_404(StoreCategory, slug=slug)
            context['category'] = self.category
        elif q:
            context['stores'] = Store.objects.filter(Q(store_name__icontains=q) | Q(category__name__icontains=q))
        context['categories'] = StoreCategory.objects.filter(publish=True)
        return context

@method_decorator(check_2fa, name='dispatch')
class AddToStoreView(LoginRequiredMixin, CreateView):
    template_name = 'store/add-or-update.html'
    form_class = AddStoreForm
    success_url = reverse_lazy('store:addtostore_complete')

    def get_context_data(self, **kwargs):
        context = super(AddToStoreView, self).get_context_data(**kwargs)
        context['categories'] = StoreCategory.objects.filter(publish=True)
        return context

    def form_valid(self, form, commit=True):
        self.object = form.save(commit=False)
        username_or_merchant_id = form.cleaned_data['username_or_merch_id']
        if Profile.objects.filter(merchant_id=username_or_merchant_id).exists():
            profile = Profile.objects.get(merchant_id=username_or_merchant_id)
        elif Profile.objects.filter(user__username=username_or_merchant_id).exists():
            profile = Profile.objects.get(user__username=username_or_merchant_id)

        self.object.user = profile.user
        if commit:
            self.object.save()
            messages.add_message(self.request, messages.INFO,
                                 'Your store details has been added successfully, '
                                 'We will review the details and get back to you soon')
            return super(AddToStoreView, self).form_valid(form)


class AddtoStoreComplete(TemplateView):
    template_name = 'common/message.html'

class StoreCheckout(TemplateView):
    template_name = 'store/payincrypto.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        mydate = timezone.now()
        context['unique_id'] = get_random_string(
            length=32) + str(int(time.mktime(mydate.timetuple())*1000))
        context['merchant_id'] = self.kwargs.get('pk')
        context['item_name'] = "Bump Me to the Top"
        context['item_amount'] = 10
        context['item_number'] = "BUMP"
        # context['item_qty'] = self.request.POST['item_qty']
        context['buyer_qty_edit'] = 1
        # context['invoice_number'] = self.request.POST['invoice_number']
        # context['tax_amount'] = self.request.POST['tax_amount']
        # context['allow_shipping_cost'] = str(
        #     self.request.POST['allow_shipping_cost']).lower()
        # context['shipping_cost'] = self.request.POST['shipping_cost']
        # context['shipping_cost_add'] = self.request.POST['shipping_cost_add']
        # context['success_url_link'] = self.request.POST['success_url_link']
        # context['cancel_url_link'] = self.request.POST['cancel_url_link']
        # context['ipn_url_link'] = self.request.POST['ipn_url_link']
        # context['btn_image'] = self.request.POST['btn_image']
        # context['allow_buyer_note'] = self.request.POST['allow_buyer_note']
        # temp_id = context['merchant_id']
        # context['merchant_name'] = Profile.objects.get(merchant_id=temp_id)
        context['available_coins'] = Coin.objects.filter(active=True)
        return context


class PaymentFormSubmitView(View):
    def post(self, request, *args, **kwargs):
        try:
            sel_coin = Coin.objects.get(code=self.request.POST['selected_coin'])
        except:
            sel_coin = Coin.objects.get(code='ETH')
        superuser = User.objects.get(is_superuser=True)
        crypto_address = create_wallet(superuser, sel_coin.code)
        # crypto_address = '123'
        print(crypto_address)
        temp_obj = StorePaymentRec.objects.create(
            store_id=self.request.POST['merchant_id'],
            item_amount=self.request.POST['item_amount'],
            unique_id=self.request.POST['unique_id'],
            
            first_name=self.request.POST['first_name'],
            last_name=self.request.POST['last_name'],
            email_addr=self.request.POST['email_addr'],
            selected_coin=sel_coin,
            wallet_address=crypto_address,
        )
        temp_obj.save()
        context = {}
        store_id = self.request.POST['merchant_id']
        context['available_coins'] = Coin.objects.filter(active=True)
        context['merchant_name'] = Store.objects.get(id=store_id)
        context['crypto_address'] = crypto_address
        context['unique_id'] = self.request.POST['unique_id']
        context['selected_coin'] = sel_coin
        item_amount = float(self.request.POST['item_amount'])
        item_qty = float(1)
        context['amt_payable_usd'] = (item_amount * item_qty)
        return render(request, 'merchant_tools/postpayment.html', context)



