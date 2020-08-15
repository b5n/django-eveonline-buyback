import requests


def main():
    with open('items.txt', 'r') as submission:
        contents = submission.readlines()
    sorted_items = item_sorter(contents)
    general, blue = sorted_items
    general_total = get_evepraisal(general, 10)
    blue_total = get_bluepraisal(blue, 50)
    print(f'general: {general_total}\nblue: {blue_total}')
    total = general_total + blue_total
    print(f'{round(total):.2f}')


def item_sorter(submission):
    blue_buyback = []
    general_buyback = ''
    for line in submission:
        item_name = line.split('\t')[0]
        if item_name in str(blue_loot().keys()):
            blue_buyback.append(line)
        else:
            general_buyback = general_buyback + line
    sorted_items = (general_buyback, blue_buyback)
    return sorted_items


def get_evepraisal(submission, rate):
    url = url = 'https://evepraisal.com/appraisal'
    market = 'jita'
    payload = {
        'User-Agent': 'django-eveonline-buyback/0.0.1 b@bnunez.com',
        'raw_textarea': f'{submission}',
        'market': f'{market}',
    }
    id_request = requests.post(url, params=payload)
    appraisal_id = id_request.headers['X-Appraisal-Id']
    appraisal_url = "https://evepraisal.com/a/{}.json".format(appraisal_id)
    result = requests.get(appraisal_url).json()
    total = (result['totals']['buy'])
    return total * (rate / 100)


def get_bluepraisal(submission, rate):
    total = 0
    blue_loot_base = blue_loot()
    for line in submission:
        item_name = line.split('\t')[0]
        item_quantity = int(line.split('\t\t')[1])
        item_price = blue_loot_base.get(item_name)
        total += item_price * item_quantity
    return total * (rate / 100)


def blue_loot():
    blue_loot = {
        'Neural Network Analyzer': 200000.00,
        'Sleeper Data Library': 500000.00,
        'Ancient Coordinates Database': 1500000.00,
        'Sleeper Drone AI Nexus': 5000000.00
    }
    return blue_loot


if __name__ == '__main__':
    main()
