
class MQTTException(Exception):

    def __init__(self, value, *args, **kwargs):
        super(MQTTException, self).__init__(*args, **kwargs)
        self._value = value

    def __str__(self):
        return(repr(self._value))

class CirrusException(Exception):

    def __init__(self, value, *args, **kwargs):
        super(InfluxException, self).__init__(*args, **kwargs)
        self._value = value

    def __str__(self):
        return(repr(self._value))
