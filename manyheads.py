# 欢迎杨大大为计算机视觉做出的贡献

# 来点有用的 https://github.com/tzutalin/labelImg

# 上面这个太麻烦了

# https://github.com/rachelcao277/LabelImage 这个好
# https://labelhub.cn/home
# https://app.labelbox.com/signin
# http://www.jinglingbiaozhu.com/


# importing cv2
import cv2
from skimage import io
# path
image = io.imread('https://cdn.britannica.com/25/172925-050-DC7E2298/black-cat-back.jpg')  # 1920 * 800 的 3 维数组

# Reading an image in default mode
#image = cv2.imread(path)

face = image[413:749,214:579]

#image[0:336,0:365] = face

for i in range(2):
    for j in range(2):
        image[336*(i):336*(i+1), 580+365*(j):580+365*(j+1)] = face

cv2.imwrite("blackcat-face.jpg", image)

from matplotlib import pyplot as plt
#%matplotlib inline
plt.imshow(cv2.imread('./blackcat-face.jpg',cv2.IMREAD_UNCHANGED))
plt.title('picture-rgb')
plt.show()