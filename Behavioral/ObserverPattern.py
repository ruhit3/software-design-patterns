from abc import ABC, abstractmethod


class YouTubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)


class YouTubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, event):
        pass


class YouTubeUser(YouTubeSubscriber):
    def __init__(self, name):
        self.name = name

    def sendNotification(self, channel, event):
        print(f"User {self.name} received notification from {channel}: {event}")


channel = YouTubeChannel("neetcode")

channel.subscribe(YouTubeUser("sub1"))
channel.subscribe(YouTubeUser("sub2"))
channel.subscribe(YouTubeUser("sub3"))

channel.notify("A new video released")

for i in range(len(channel.subscribers)):
    print("Subscribers list: " + channel.subscribers[i].name)
