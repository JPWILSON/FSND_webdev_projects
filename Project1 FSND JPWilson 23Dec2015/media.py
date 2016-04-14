#Below are the 3 classes used to create the content for the 'Fresh Tomatoes' website

class Videos():
        """Videos is the parent class"""
        def __init__(self, title, poster, description, trailer):
                self.title = title
                self.poster = poster
                self.description = description
                self.trailer = trailer


class Movies(Videos):
        """Movies inherits from Videos, and includes the constructor for movie objects"""
        def __init__(self, title, poster, description, trailer, specific_info):
                Videos.__init__(self,title, poster, description, trailer)
                self.specific_info = specific_info
                self.video_type = 'Movies hi mom'


class TVSeries(Videos):
        """TVSeries includes the constructor for tv shows objects, 
        as with the Movies class, it inherits from Videos"""
        def __init__(self, title, poster, description, trailer, specific_info):
                Videos.__init__(self,title, poster, description, trailer)
                self.specific_info = specific_info
                self.video_type = 'TV Series wont say hi mom'
            
        
