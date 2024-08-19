# Generating unique identifiers
# uuid is 128 bit string values
import uuid

# TODO Create the uuid4 function to generate a random sequence using
# the underlying os.urandom() function
result = uuid.uuid4()
print("UUID4: ")
print(result)
print(result.hex)
print(result.urn)


# TODO Create a UUID using uuid5 which takes a namespace and namevalue
# Note that this version is not crypto safe
result_uuid5 = uuid.uuid5(uuid.NAMESPACE_DNS, "mojo.com")
print("UUID5: ")
print(result_uuid5)
print(result_uuid5.hex)
print(result_uuid5.urn)

