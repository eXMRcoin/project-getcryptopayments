from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from apps.coins.models import (RateAPI, Coin, CoinSetting, CoinConvertRequest, Wallet, WalletAddress, Transaction,ClaimRefund, NewCoin, CoinVote, CoPromotion, CoPromotionURL, EthereumToken, EthereumTokenWallet, Phases, ConvertTransaction, PaypalTransaction,PaybyName, PayByNamePackage,MoneroPaymentid, PayByNamePurchase,TradeCommision)


admin.site.site_header = 'GetCryptoPayments Admin'
                              
class CoinResource(resources.ModelResource):

    class Meta:
        model = Coin
        import_id_field = 'code'
        export_id_field = 'code'
        skip_unchanged = True
        report_skipped = True
        fields = ('id', 'coin_name', 'code', 'confirms', 'to_btc', 'fee_percentage')


class CoinModelAdmin(ImportExportModelAdmin):

    resource_class = CoinResource
    search_fields = ('code', 'coin_name', )
    list_display = ('coin_name', 'code', 'confirms', 'active', 'display')
    list_editable = ('active','display', )

    class Meta:
        model = Coin

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['rate_api']
    def has_delete_permission(self, request, obj=None):
        return False
    def has_add_permission(self, request):
        return False  


admin.site.register(Coin, CoinModelAdmin)
admin.site.register(RateAPI)
admin.site.register(Phases)
admin.site.register(CoinSetting)
admin.site.register(CoinConvertRequest)
admin.site.register(Wallet)
admin.site.register(WalletAddress)
admin.site.register(Transaction)
admin.site.register(ClaimRefund)
admin.site.register(NewCoin)
admin.site.register(CoinVote)
admin.site.register(CoPromotion)
admin.site.register(CoPromotionURL)
admin.site.register(EthereumToken)
admin.site.register(EthereumTokenWallet)
admin.site.register(MoneroPaymentid)
admin.site.register(ConvertTransaction)
admin.site.register(PaypalTransaction)
admin.site.register(PaybyName)
admin.site.register(PayByNamePackage)
admin.site.register(PayByNamePurchase)
admin.site.register(TradeCommision)
