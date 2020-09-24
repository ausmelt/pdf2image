import fitz
import os

def get_files():
    files = []
    for file in os.listdir():
        if os.path.splitext(file)[1] in ('.pdf', '.PDF'):
            files.append(file)
    return files

def cov_pdf(filename):
    path = filename.split('.')[0]
    if not os.path.exists(path):
        os.makedirs(path)
    doc = fitz.open(filename)
    print("开始将 {} 转换为图片".format(filename))
    for pg in range(doc.pageCount):
        page = doc[pg]
        rotate = int(0)
        zoom_x = 2.0
        zoom_y = 2.0
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
        pm = page.getPixmap(matrix=trans, alpha=False)
        pm.writePNG(path+'/'+'{}.png'.format(pg+1))
        print("共{}页 第{}页转换完成".format(doc.pageCount, (pg+1)), end="\r")
    print(" {} 已完成转换\n".format(filename))


if __name__ == "__main__":
    files = get_files()
    for file in files:
        cov_pdf(file)
    os.system('pause')
