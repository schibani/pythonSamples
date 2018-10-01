import gc
import collections

#print("\n".join(sorted({attrname for item in gc.get_objects() for attrname in dir(item) if attrname.startswith("__")})))

person = collections.namedtuple("Person", ["name", "age"])

persons = [person("smail", 40), person("wassim", 6)]

print("\n".join(person.name for person in persons if person.age > 6))

print({person.name for person in persons})

