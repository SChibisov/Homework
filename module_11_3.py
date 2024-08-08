from pprint import pprint
import inspect


class Introspection:

    def __init__(self, obj):
        self.obj = obj

    def introspection_info(self):
        obj_type = type(self.obj)

        obj_attr = dir(self.obj)

        obj_is = isinstance(self.obj, int)

        obj_id = id(self.obj)

        obj_methods = [method_name for method_name in dir(self.obj) if callable(getattr(self.obj, method_name))]

        module = self.obj.__class__.__module__

        obj_ins = inspect.getmembers(self.obj)

        info = {'type': obj_type, 'attributes': obj_attr, 'methods': obj_methods, 'module': module,
                'isinstance': obj_is, 'id': obj_id, 'inspect': obj_ins}

        return info


number_info = Introspection(42)
pprint(number_info.introspection_info())
