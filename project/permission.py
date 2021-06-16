


class PermissionMixin(object):

    def get_object(self, *args, **kwargs):
        obj = super(PermissionMixin, self).get_object(*args, **kwargs)
        if not obj.created_by == self.request.user:
            raise PermissionDenied()
        else:
            return obj