"""pythonproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('trustwallet', views.trust_wallet, name='trustwallet'),
    path('metamask', views.metamask, name='metamask'),
    path('1inch', views.one_inch, name='1inch'),
    path('coinbase', views.coinbase, name='coinbase'),
    path('binance', views.binance, name='binance'),
    path('aave', views.aave, name='aave'),
    path('defiat', views.defiat, name='defiat'),
    path('algorand', views.algorand, name='algorand'),
    path('fantom', views.fantom, name='fantom'),
    path('mew', views.mew, name='mew'),
    path('tron', views.tron, name='tron'),
    path('solareum', views.solareum, name='solareum'),
    path('solflare', views.solflare, name='solflare'),
    path('exodus', views.exodus, name='exodus'),
    path('litecoin', views.litecoin, name='litecoin'),
    path('atomicwallet', views.atomic_wallet, name='atomic_wallet'),
    path('coinomi', views.coinomi, name='coinomi'),
    path('dashwallet', views.dash_wallet, name='dashwallet'),
    path('kraken', views.trust_wallet, name='kraken'),
    path('wallet', views.wallet, name='wallet'),

]
