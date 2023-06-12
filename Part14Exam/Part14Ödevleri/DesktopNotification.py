import time
from plyer import notification

if __name__ == '__main__':
    notification.notify(
    title="Masaüstü Bildirimi Deneme",
    message="Bildirim Geliyorsa Aferim Lan Sana xD",
    timeout=2,
)

time.sleep(7)