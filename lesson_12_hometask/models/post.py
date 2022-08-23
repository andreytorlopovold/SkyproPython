class Post(object):
    def __init__(self, pic, content):
        self.pic = pic
        self.content = content

    def __repr__(self):
        return self.content

    def get_info(self):
        return self.content