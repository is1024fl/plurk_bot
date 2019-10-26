''' A real-time hello world plurk_bot for replurk'''

from plurk_oauth import PlurkAPI
import time
import random
import yaml
import codecs


def time_stamp():
    localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return localtime


# fixed_plurk
fixed_plurk = {
    "plurk_id": "",
    "content": "",
    "qualifier": "says", "lang": "tr_ch"
}

if __name__ == '__main__':

    # get api token
    plurk = PlurkAPI.fromfile("api.key")

    # user info
    with codecs.open("users.yaml", encoding="utf-8") as f:
        users = yaml.load(f)

    try:
        # get every plurks
        timeline_plurks = plurk.callAPI('/APP/Polling/getPlurks', options={"offset": "2019-10-26T11:48:00"})['plurks']

        # choose new plurks(plurk_type == 0) from all plurks
        unread_plurks = [unread_plurk for unread_plurk in timeline_plurks
                         if unread_plurk['plurk_type'] == 0 and unread_plurk['owner_id'] in users['ids']]

        for unread_plurk in unread_plurks:
            # replurk format
            fixed_plurk['plurk_id'] = unread_plurk['plurk_id']
            name_id = users['ids'].index(unread_plurk['owner_id'])
            num = str(random.randint(1, 520))
            fixed_plurk['content'] = "Hello, world, " + users['names'][name_id] + ".[emo" + num + "]"

            # replurk with api
            plurk.callAPI('/APP/Responses/responseAdd', options=fixed_plurk)
            plurk.callAPI('/APP/Timeline/markAsRead',
                          options={"ids": [str(unread_plurk['plurk_id'])]})

            # print to log
            print(f"{time_stamp()} read {users['names'][name_id]}: {unread_plurk['content'][:10]}\n")

    except:
        pass
