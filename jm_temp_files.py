import os
import tempfile
# import os.path

# TODO Get information about the temp data environment
# print("gettempdir(): ", tempfile.gettempdir())
# print("gettempprefix(): ", tempfile.gettempprefix())

# TODO Create a temp file using mkstemp() 
# (temp_file_handle, temp_file_path) = tempfile.mkstemp(".tmp", "jd_custom_temp_file", None, True)

# f = os.fdopen(temp_file_handle, "w+t")
# f.write("This is some temporary data we wrote")
# f.seek(0)
# print(f.read())
# # We need to close the file
# f.close()
# os.remove(temp_file_path)

# TODO Create a temp file using the TemporaryFile class
# This is context manager syntax here
with tempfile.TemporaryFile(mode="w+t") as temporary_file_pointer:
    temporary_file_pointer.write("Aloha temporary")
    temporary_file_pointer.seek(0)
    print(temporary_file_pointer.read())

# TODO Create a temp directory using the TemporaryDirectory class
with tempfile.TemporaryDirectory() as tdp:
    path = os.path.join(tdp,"tempfile.txt")
    tfp = open(path,"w+t")
    tfp.write("Hello")
    tfp.seek(0)
    print(tfp.read())
    tfp.close()
    os.remove(path)
