class Node(object):
    def __init__(self, ip=None, mac=None):
        self.ip = ip
        self.mac = mac
        # TODO
        # description?
        # OS?

    def __repr__(self):
        # FIXME should actually be a python expression able to generate
        # this same object i.e. Node(ip, mac)
        _ret = "Node IP: {}".format(self.ip)
        if self.mac:
            _ret += " [mac: {}]".format(self.mac)
        return _ret

    def __eq__(self, other):
        # if a mac address is defined,
        if self.mac and self.other.mac:
            return self.ip == self.other.ip and self.mac == self.other.mac

        # no mac address specified or one is undefined - we compare by IP
        return self.ip == self.other.ip
