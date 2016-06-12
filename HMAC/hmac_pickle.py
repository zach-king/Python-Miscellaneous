import hmac
from fnvhash import fnv1a_32
import pickle
import pprint
from io import StringIO

def make_digest(message):
    "Return a digest for the given message"
    return hmac.new(b'secret-shared-key', message).hexdigest()


class SimpleObject(object):
    "A very simple class to demonstrate digests before unpickling."
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# Simulate a writeable socket or pipe with StringIO
out_s = StringIO()

# Write a valid object to the stream:
#   digest/nlength/npickle
o = SimpleObject('digest matches')
pickled_data = pickle.dumps(o)
digest = make_digest(pickled_data)
header = '%s %s' % (digest, len(pickled_data))
print('\nWRITING:', header)
out_s.write(header + '\n')
out_s.write(str(pickled_data))


# Write an invalid object to the stream
o = SimpleObject('digest does not match')
pickled_data = pickle.dumps(o)
digest = make_digest(b'not the pickled data at all')
header = '%s %s' % (digest, len(pickled_data))
print('\nWRITING:', header)
out_s.write(header + '\n')
out_s.write(str(pickled_data))

out_s.flush()


# Simulate a readable socket or pipe with StringIO
in_s = StringIO(out_s.getvalue())

# Read the data
while True:
    first_line = in_s.readline()
    print('FL:', first_line)
    if not first_line:
        break
    incoming_digest, incoming_length = first_line.split(' ')
    incoming_length = int(incoming_length)
    print('\nREAD:', incoming_digest, str(incoming_length))
    incoming_pickled_data = in_s.read(incoming_length)

    actual_digest = make_digest(incoming_pickled_data.encode())
    print('ACTUAL:', actual_digest)

    if incoming_digest != actual_digest:
        print('UNAUTHORIZED MESSAGE')
    else:
        obj = pickle.loads(incoming_pickled_data)
        print('VERIFIED:', obj)
