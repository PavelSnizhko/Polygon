# from regd import DecoratorRegistry as dreg


def check_values(f):
    """ side - side of polygone
        n - count a polygone top
    """

    def decorated(self, a):
        if a > 0:
            return f(self, a)
        else:
            msg = "{} is out of positive range"
            raise ValueError(msg.format(a))

    return decorated


# check_values = dreg.decorator(check_values)
