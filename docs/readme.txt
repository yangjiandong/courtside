courside
========

2012.05.04
----------

   1. install

   change requirements.txt
      remove django, httplib2

   use ming32 compile
   install MinGW with C++ Compiler option checked
   add C:\MinGW\bin to your PATH
   in PYTHONPATH\Lib\distutils, create a file distutils.cfg and add these lines:
   [build]
   compiler=mingw32

   >cd D:\ruby-1.9.3-p0-i386-mingw32 
   >msys.bat
   >cd ..
   >pip install -r requirements.txt


