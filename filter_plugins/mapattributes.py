# This is a custom filter that allows map with multiple attributes, cf https://github.com/pallets/jinja/issues/554
# Some of the code is stolen from https://github.com/pallets/jinja/blob/main/src/jinja2/filters.py
import typing as t

def _prepare_attribute_parts(
        attr: t.Optional[t.Union[str, int]]
    ) -> t.List[t.Union[str, int]]:
    if attr is None:
        return []

    if isinstance(attr, str):
        return [int(x) if x.isdigit() else x for x in attr.split(".")]

    return [attr]

def _make_attrgetter(
    attribute: t.Optional[t.Union[str, int]],
    default: t.Optional[t.Any] = None,
) -> t.Callable[[t.Any], t.Any]:
    """Returns a callable that looks up the given attribute from a
    passed object with the rules of the environment. Dots are allowed
    to access attributes of attributes. Integer parts in paths are
    looked up as integers.
    """
    parts = _prepare_attribute_parts(attribute)

    def attrgetter(item: t.Any) -> t.Any:
        for part in parts:
            item = item[part]

            if default is not None:
                item = default

        return item

    return attrgetter

class FilterModule(object):
    def filters(self):
        return { 'mapattributes': self.mapattributes }

    def mapattributes(self, dicts, keys, key_names=None, default=None):
        if key_names is None:
            key_names = keys

        l = []
        for di in dicts:
            newdi = { }
            for key, name in zip(keys, key_names):
                func = _make_attrgetter(key, default)
                newdi[name] = func(di)
            l.append(newdi)
        return l
