# https://stackoverflow.com/a/45698519
class AttrDict(dict):
    def __init__(self, d):
        super(AttrDict, self).__init__(d)

    def __dir__(self):
        return self.keys()

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key)

    def __setattr__(self, key, value):
        if key in self:
            raise AttributeError("These attributes are read only")
        else:
            super(AttrDict, self).__setattr__(key, value)
