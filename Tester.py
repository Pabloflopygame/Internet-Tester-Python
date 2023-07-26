import time
import speedtest


def actual_time():
    return time.strftime("%H:%M:%S", time.localtime())


wifi = speedtest.Speedtest(secure=True)
print("[Time]: [Download Kbs]-[Upload Kbs]")

while True:
    print(f"{actual_time()}: {int(wifi.download()*10**(-3))}-{int(wifi.upload()*10**(-3))}")
    time.sleep(60*5)
