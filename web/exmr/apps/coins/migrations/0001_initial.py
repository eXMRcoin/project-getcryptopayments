# Generated by Django 2.0.2 on 2018-06-25 10:58

import apps.coins.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0013_plugindownload'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClaimRefund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refund_sent_address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_name', models.CharField(max_length=255, verbose_name='coin name')),
                ('coin_url', models.URLField(blank=True, null=True, verbose_name='coin site URL')),
                ('code', models.CharField(max_length=25, unique=True, verbose_name='code')),
                ('confirms', models.PositiveSmallIntegerField(verbose_name='confirms')),
                ('image', models.ImageField(help_text='Upload a 35X35 image for better experience', upload_to='', verbose_name='image')),
                ('to_btc', models.DecimalField(decimal_places=8, default=1.0, max_digits=10, verbose_name='to BTC value')),
                ('fee_percentage', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='fee percentage')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Crypto'), (1, 'Ripple'), (2, 'Ether tokens'), (3, 'Fiat')], default=0, verbose_name='type')),
                ('can_convert', models.BooleanField(default=True, verbose_name='can convert coin to another')),
                ('can_explore', models.BooleanField(default=False, verbose_name='can explore coins')),
                ('can_donate', models.BooleanField(default=False, verbose_name='can donate coins')),
                ('active', models.BooleanField(default=True, help_text='Disable this coin anytime')),
                ('min_deposit', models.DecimalField(decimal_places=8, default=0, max_digits=10)),
                ('max_deposit', models.DecimalField(decimal_places=8, default=0, max_digits=10)),
                ('vote_count', models.IntegerField(default=0, verbose_name='vote count')),
            ],
            options={
                'verbose_name': 'Coin',
                'verbose_name_plural': 'Coins',
            },
        ),
        migrations.CreateModel(
            name='CoinConvertRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_from', models.CharField(blank=True, max_length=255, null=True, verbose_name='wallet from address')),
                ('wallet_to', models.CharField(blank=True, max_length=255, null=True, verbose_name='wallet to address')),
                ('convert_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_conversions', to='coins.Coin', verbose_name='convert from coin')),
                ('convert_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_conversions', to='coins.Coin', verbose_name='convert to coin')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_conversion_requests', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Coin Conversion Request',
                'verbose_name_plural': 'Coin Conversion Requests',
            },
        ),
        migrations.CreateModel(
            name='Coin_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_hosting', models.CharField(choices=[('hosted', 'hosted'), ('poloneix', 'poloneix'), ('binance', 'binance'), ('okex', 'okex')], default='HOSTED', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CoinRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=500, verbose_name='name')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('coin_website', models.CharField(blank=True, default='', max_length=500, verbose_name='coin website')),
                ('coin_url', models.URLField(blank=True, null=True, verbose_name='coin url')),
            ],
        ),
        migrations.CreateModel(
            name='CoinSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False, verbose_name='enabled')),
                ('payment_address', models.CharField(max_length=64, verbose_name='payment address')),
                ('payment_mode', models.PositiveSmallIntegerField(choices=[(0, 'To Balance'), (1, 'ASAP'), (2, 'Nightly'), (3, 'To Balance + Convert'), (4, 'ASAP + Convert')], default=0, verbose_name='payment mode')),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='discount field')),
                ('maximum_per_transaction', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='maximum per transaction')),
                ('coin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_coin_settings', to='coins.Coin', verbose_name='coin')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='common.Currency', verbose_name='currency')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_user_coin_settings', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='CoinVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('follow', 'follow'), ('share', 'share'), ('token', 'token')], default='', max_length=20)),
                ('source', models.CharField(choices=[('facebook', 'facebook'), ('twitter', 'twitter'), ('linkedin', 'linkedin'), ('telegram', 'telegram'), ('reddit', 'reddit'), ('youtube', 'youtube'), ('medium', 'medium'), ('steemit', 'steemit'), ('instagram', 'instagram')], default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='NewCoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('company_email', models.EmailField(max_length=254, verbose_name='comapny email')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, verbose_name='last name')),
                ('contact_number', models.CharField(max_length=20, verbose_name='contact number')),
                ('secondary_number', models.CharField(blank=True, max_length=20, null=True)),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='coin name')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='coin code')),
                ('website', models.URLField(blank=True, null=True, verbose_name='website URL')),
                ('logo_url', models.URLField(blank=True, null=True, verbose_name='logo_url')),
                ('hash_tags', models.CharField(max_length=100, verbose_name='hash tags')),
                ('twitter_handle', models.CharField(max_length=20, verbose_name='twitter handle')),
                ('fb_page', models.URLField(blank=True, null=True, verbose_name='facebook page')),
                ('twitter_page', models.URLField(blank=True, null=True, verbose_name='twitter page')),
                ('linkedin_page', models.URLField(blank=True, null=True, verbose_name='linkedin page')),
                ('telegram_page', models.URLField(blank=True, null=True, verbose_name='telegram page')),
                ('reddit_page', models.URLField(blank=True, null=True, verbose_name='reddit page')),
                ('vote_count', models.IntegerField(blank=True, default=0, null=True, verbose_name='vote count')),
                ('approved', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PaybyName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user paybyname')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(max_length=200)),
                ('balance', models.CharField(blank=True, max_length=20)),
                ('currency', models.CharField(blank=True, max_length=20)),
                ('transaction_id', models.CharField(blank=True, max_length=200)),
                ('transaction_to', models.CharField(blank=True, max_length=200)),
                ('message', models.CharField(blank=True, max_length=300)),
                ('system_tx_id', models.CharField(default=apps.coins.models.get_random, max_length=50)),
                ('activation_code', models.CharField(blank=True, max_length=20)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('private', models.CharField(blank=True, default='', max_length=500)),
                ('public', models.CharField(blank=True, default='', max_length=500)),
                ('words', models.CharField(blank=True, default='', max_length=500)),
                ('paymentid', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='WalletAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='wallet',
            name='addresses',
            field=models.ManyToManyField(to='coins.WalletAddress'),
        ),
        migrations.AddField(
            model_name='wallet',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.Coin'),
        ),
        migrations.AddField(
            model_name='wallet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coinvote',
            name='coin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.NewCoin', verbose_name='coin'),
        ),
        migrations.AddField(
            model_name='coinvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='coin',
            name='coin_hosting_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.Coin_Type'),
        ),
        migrations.AddField(
            model_name='claimrefund',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.Transaction'),
        ),
    ]
