# gr-fengyun2
OOT GnuRadio blocks for decode S-VISSR2.0 Images from FengYun-2x satellites

### Source
Forked from [gr-soniks](https://github.com/Foxiks/gr-soniks)

### Install Dependencies
1. gr-Satellites: https://github.com/daniestevez/gr-satellites
2. OpenCV2 ```sudo apt-get install python3-opencv```
3. ``` python3 -m pip install hexhamming construct Pillow```

### Installation
```
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig
```
