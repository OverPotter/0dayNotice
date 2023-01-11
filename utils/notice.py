import win10toast
from utils.finder import Finder


class Notification(Finder):
    def __init__(self):
        super().__init__()

    def launch_notice(self):
        self.receive_exploit()
        for exploit_info in self.selection_exploits:
            text = f"Release date: {exploit_info[1]}\nDescription: {exploit_info[2]}\nPrice: {exploit_info[6]}"
            self.call_notification(text)

    @staticmethod
    def call_notification(text: str):
        notification = win10toast.ToastNotifier()
        notification.show_toast(title="Exploit Notice App", msg=text, duration=7)
