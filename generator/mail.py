from .info_fields import Sender, Date, Adress, Recipient
from .text_fields import Head, Body, Peroration


class Constructor:
    # Fields

    head = None
    body = None
    peroration = None
    sender = None
    date = None
    adress = None
    recipient = None

    # Classes

    class Head(Head):
        def __init__(self):
            Head.__init__(self)

    class Body(Body):
        def __init__(self):
            Body.__init__(self)

    class Peroration(Peroration):
        def __init__(self):
            Peroration.__init__(self)

    class Sender(Sender):
        def __init__(self):
            Sender.__init__(self)

    class Date(Date):
        def __init__(self):
            Date.__init__(self)

    class Adress(Adress):
        def __init__(self):
            Adress.__init__(self)

    class Recipient(Recipient):
        def __init__(self):
            Recipient.__init__(self)


