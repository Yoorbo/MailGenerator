"""
    Contains Constructor Class
"""
from generator.info_fields import Sender, Date, Adress, Recipient
from generator.text_fields import Head, Body, Peroration


class Constructor:
    """
        Abstract Constructor Class
        Combines essential elements for mails
        :param None
        :returns None
    """
    # Fields

    head, body, peroration = None, None, None
    sender, recipient = None, None
    date, adress = None, None

    # Classes

    class Head(Head):
        """
            Inheritance of generator.text_fields.Head
        """
        def __init__(self):
            Head.__init__(self)

    class Body(Body):
        """
            Inheritance of generator.text_fields.Body
        """
        def __init__(self):
            Body.__init__(self)

    class Peroration(Peroration):
        """
            Inheritance of generator.text_fields.Peroration
        """
        def __init__(self):
            Peroration.__init__(self)

    class Sender(Sender):
        """
            Inheritance of generator.text_fields.Sender
        """
        def __init__(self):
            Sender.__init__(self)

    class Date(Date):
        """
            Inheritance of generator.text_fields.Date
        """
        def __init__(self):
            Date.__init__(self)

    class Adress(Adress):
        """
            Inheritance of generator.text_fields.Adress
        """
        def __init__(self):
            Adress.__init__(self)

    class Recipient(Recipient):
        """
            Inheritance of generator.text_fields.Recipient
        """
        def __init__(self):
            Recipient.__init__(self)

    # Methods

    def __init__(self):
        self.head, self.body, self.peroration = self.Head(), self.Body(), self.Peroration()
        self.sender, self.recipient = self.Sender(), self.Recipient()
        self.date, self.adress = self.Date(), self.Adress()

    def generate_seed(self):
        """
            Generates a random mail seed as integer
        """

    def generate_string(self):
        """
            Generates a string fitting the generator component
        """
