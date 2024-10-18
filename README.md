#计算机视觉分配1
##使用OpenCV和Tesseract OCR提取图像文本
这个存储库包含Python脚本，这些脚本利用OpenCV进行图像预处理，利用Tesseract OCR从图像中提取文本。这些脚本处理各种预处理技术，如灰度转换、噪声消除、阈值处理、膨胀、腐蚀和去歪斜，以增强OCR结果。
##要求
-Python 3.x
-OpenCV
-宇宙魔方
-NumPy
﻿
##装置
﻿
1.安装所需的软件包:
   
```嘘
pip安装opencv-python pytesseract numpy
```
﻿
2.安装宇宙魔方OCR:
- **Windows操作系统**:从以下网站下载安装程序[UB曼海姆的宇宙魔方](https://github.com/UB-Mannheim/tesseract/wiki).

﻿
##使用
﻿
###预处理和OCR
﻿
该代码包括各种图像预处理功能，以提高OCR准确性:
﻿
-灰度转换
-噪声消除
-阈值处理
-扩张
-侵蚀
-去歪斜
-Canny边缘检测
