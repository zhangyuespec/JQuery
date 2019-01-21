import os
import os.path
from PIL import Image
'''
filein: 输入图片
fileout: 输出图片
width: 输出图片宽度
height:输出图片高度
type:输出图片类型（png, gif, jpeg...）
'''
def ResizeImage(filein, fileout, width, height, type):
  img = Image.open(filein)
  out = img.resize((width, height),Image.ANTIALIAS) #resize image with high-quality
  out.save(fileout, type)
if __name__ == "__main__":
  # filein =
  # fileout =
  width = 300
  height = 400
  type = 'png'
  for i in range (5,9):
      ResizeImage(r'../images/%s.jpg'%i,r'../images/%s.png'%i, width, height, type)