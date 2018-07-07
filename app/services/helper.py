
def to_dict(object):
    object_list = []
    if object is not None:
        for _ in object:
                object_list.append(_.as_dict())
        return object_list