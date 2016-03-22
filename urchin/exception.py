import sys
import six

_ = lambda x: x

class UrchinException(Exception):
    msg_fmt = _("An unknown exception occurred.")
    code = 500
    headers = {}
    safe = False

    def __init__(self, message=None, **kwargs):
        self.kwargs = kwargs

        if 'code' not in self.kwargs:
            try:
                self.kwargs['code'] = self.code
            except AttributeError:
                pass


        self.message = message
        super(UrchinException, self).__init__(message)


class Invalid(UrchinException):
    msg_fmt = _("Unacceptable parameters.")
    code = 400


class InvalidContentType(Invalid):
    msg_fmt = _("Invalid content type %(content_type)s.")

