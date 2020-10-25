import os
import win32com.client
from wirecastCOMAPI import PreviewShotID, LiveShotID, getName
import requests
import time


def get_shots():
    preview_shot1 = PreviewShotID(1)
    live_shot1 = LiveShotID(1)
    preview_shot2 = PreviewShotID(2)
    live_shot2 = LiveShotID(2)
    return {"queued2": str(getName(preview_shot2)).lower(), "live2": str(getName(live_shot2)).lower(),
            "queued1": str(getName(preview_shot1)).lower(), "live1": str(getName(live_shot1)).lower()}


def update_shots():
    try:
        url = 'https://cam-ops.cbcfamily.church/api/shot_status'
        response = requests.post(url, json=get_shots())
        print(response.json())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    while True:
        update_shots()
        time.sleep(.8)
