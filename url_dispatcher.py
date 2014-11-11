def baseurl(request):
    """
    Return a BASE_URL template context for the current request.
    """
    return {'EINVOICE_URL': '/einvoice/',}