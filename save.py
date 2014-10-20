# save 'data' into 'filename' which is located at 'path'
def saveFile(data, filename, path, mode):
    f_obj = open(path + '/' + filename, mode)
    f_obj.write(data)
    f_obj.write(bytes('\n', 'UTF-8'))
    f_obj.close()
