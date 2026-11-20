
import webbrowser


class WebsiteLauncher:

    def __init__(self):
        self.websites = {
            "Google": "https://www.google.com",
            "YouTube": "https://www.youtube.com",
            "GitHub": "https://github.com",
            "Gmail": "https://mail.google.com",
            "LinkedIn": "https://www.linkedin.com"
        }

    def open_website(self, url):

        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        webbrowser.open(url)

        return True

    def add_website(self, name, url):

        if not name.strip() or not url.strip():
            raise ValueError("Website name and URL are required.")

        self.websites[name.strip()] = url.strip()

    def delete_website(self, name):

        if name in self.websites:
            del self.websites[name]

    def get_websites(self):

        return self.websites
