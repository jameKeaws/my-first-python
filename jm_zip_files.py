import zipfile
# TODO Create a new ZIP archive
# zfile = zipfile.ZipFile("myzipfile.zip", "w")
# zfile.write("file1.txt")
# zfile.write("file2.txt")
# zfile.write("file3.txt")
# zfile.close()

# TODO Check validity of the file
# print(zipfile.is_zipfile("myzipfile.zip"))

# TODO Read the properties of the ZIP archive
# zzfile = zipfile.ZipFile("myzipfile.zip")
# print(zzfile.namelist())
# print(zzfile.infolist())
# zzfile.close()

# TODO Read the properties of the ZIP contents
# anyZipFile = zipfile.ZipFile("myzipfile.zip")
# zip_file1_info = anyZipFile.getinfo("file1.txt")
# print(zip_file1_info.file_size)
# # Returns binary
# print(anyZipFile.read("file3.txt"))


# TODO Extract zip file contents
the_zip_file = zipfile.ZipFile("myzipfile.zip")
the_zip_file1_info = the_zip_file.getinfo("file1.txt")
# the_zip_file.extract("file2.txt")
the_zip_file.extractall()
