import requests
from decimal import Decimal
from django.shortcuts import render
from django_eveonline_buyback.forms import EveBuyback
from django_eveonline_buyback.models import BuybackSettings
from django.contrib.auth.decorators import login_required


@login_required
def buyback(request, total=0):
    if request.method == 'POST':
        form = EveBuyback(request.POST)
        if form.is_valid():
            general_buyback_rate = form.cleaned_data['general_buyback_rate']
            blue_loot_buyback_rate = form.cleaned_data['blue_loot_buyback_rate']
            item_list = form.cleaned_data['item_list']
            sorted_items = item_sorter(item_list)
            general, blue = sorted_items
            general_total = get_evepraisal(general, general_buyback_rate)
            blue_total = get_bluepraisal(blue, blue_loot_buyback_rate)
            total = general_total + blue_total
    else:
        form = EveBuyback()

    context = {
        'buyback_settings': get_buyback_settings(),
        'total': round(total, 2),
        'form': form
    }
    return render(request, 'adminlte/buyback.html', context)


def item_sorter(submission):
    blue_buyback = []
    general_buyback = ''
    for line in submission.splitlines():
        item_name = line.split('\t')[0]
        if item_name.lower() in str(get_blue_loot_types()):
            blue_buyback.append(line)
        else:
            general_buyback = general_buyback + f'{line}\n'
    sorted_items = (general_buyback, blue_buyback)
    return sorted_items


def get_evepraisal(submission, rate):
    if submission is not '':
        url = url = 'https://evepraisal.com/appraisal'
        market = 'jita'
        payload = {
            'User-Agent': 'django-eveonline-buyback/0.0.1 b@bnunez.com',
            'raw_textarea': f'{submission}',
            'market': f'{market}',
        }
        id_request = requests.post(url, params=payload)
        appraisal_id = id_request.headers['X-Appraisal-Id']
        appraisal_url = f'https://evepraisal.com/a/{appraisal_id}.json'
        result = requests.get(appraisal_url).json()
        total = (result['totals']['buy'])
        return Decimal(total) * rate
    else:
        return 0


def get_bluepraisal(submission, rate):
    total = 0
    if submission is not '':
        print(submission)
        buyback_settings = get_buyback_settings()
        for line in submission:
            print(line)
            item_name = line.split('\t')[0].replace(
                ' ', '_').strip().lower() + '_price'
            print(item_name)
            item_quantity = int(line.split('\t')[1])
            print(item_quantity)
            item_price = getattr(buyback_settings, item_name)
            print(item_price)
            total += item_price * item_quantity
            print(total)
            print(total * rate)
    return total * rate


def get_blue_loot_types():
    buyback_settings = get_buyback_settings()
    blue_loot_types_raw = [field.name for field in buyback_settings._meta.get_fields()[
        1:5]]
    blue_loot_types = [x.replace('_', ' ').replace(
        'price', '').strip() for x in blue_loot_types_raw]
    return blue_loot_types


def get_buyback_settings():
    buyback_settings = BuybackSettings()
    return buyback_settings
