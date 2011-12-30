from math import *
import urllib, urllib2, re, hashlib, random, time

class evalFunctions(object):

    def __init__(self, bot):
        self.bot = bot

    def seval(self, command, cinfo):
        user = cinfo["user"]
        host = cinfo["hostmask"]
        origin = cinfo["origin"]
        message = cinfo["message"]
        target = cinfo["target"]

        md5 = self.md5
        wget = self.wget
        randint = self.randint
        msg = self.msg
        notice = self.notice

        del self
        try:
            value = str(eval(command))
        except Exception as e:
            value = str(e)
        except SystemExit as e:
            value = "ERROR: Tried to call a SystemExit!"
        return value

    def randint(self, lo, hi):
        return random.randint(lo, hi)

    def md5(self, data):
        return hashlib.md5(data).hexdigest()

    def wget(self, url):
        obj = urllib2.urlopen(url)
        if obj.geturl().startswith("file://"):
            return "Local file access is not allowed."
        elif not str(obj.info()).split("Content-Type: ")[1].lower().strip("\n").strip() == "text/html":
            return "Content-Type " + str(obj.info()).split("Content-Type: ")[1].strip("\n").strip() + "not allowed."
        elif not int(str(obj.info()).split("Content-Length: ")[1].split("\n")[0]) < 51200:
            return "Content is greater than 50KB in size."
        else:
            return self.rht(obj.read())

    def msg(self, target, message, flag=False):
        try:
            self.bot.sendmsg(target, message)
        except:
            if flag:
                return "Couldn't send message!"
            else:
                return ""
        else:
            if flag:
                return "Message sent!"
            else:
                return ""

    def notice(self, target, message, flag=False):
        try:
            self.bot.sendnotice(target, message)
        except:
            if flag:
                return "Couldn't send notice!"
            else:
                return ""
        else:
            if flag:
                return "Message sent!"
            else:
                return ""

    def join(self, channel, flag=False):
        return "Not implemented!"

    def part(self, channel, message="Leaving", flag=False):
        return "Not implemented!"

    def kick(self, channel, target, message, flag=False):
        return "Not implemented!"

    def mode(self, channel, modes, flag=False):
        return "Not implemented!"

    def rht(self, data):
    # Utility, removes HTML from the input
        p = re.compile(r'<.*?>')
        try:
            return p.sub('', data.encode('ascii','ignore'))
        except:
            return "Unable to parse HTML."