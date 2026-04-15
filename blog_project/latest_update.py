# models.py mein yeh property add karo
@property
def reading_time(self):
    import math
    word_count = len(self.content.split())
    minutes = math.ceil(word_count / 200)  # average 200 words/min
    return minutes

