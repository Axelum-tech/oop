class Image:

    def __init__(self,filename,width,height,title):
        self.filename=filename
        self.width=width
        self.height=height
        self.title=title

    def show(avatar):
        print("Image(",avatar.filename, avatar.width, avatar.height, avatar.title,")")


avatar=Image("my-avatar.png",100,100,"me")


Image.show(avatar)