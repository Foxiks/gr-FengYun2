# gr-fengyun2
OOT GnuRadio blocks for decode S-VISSR2.0 Images from FengYun-2x satellites

### Source
Forked from [gr-soniks](https://github.com/Foxiks/gr-soniks)

### Install Dependencies
1. GNURadio 3.10
2. gr-Satellites: https://github.com/daniestevez/gr-satellites
3. OpenCV2 ```sudo apt-get install python3-opencv```
4. ``` python3 -m pip install hexhamming construct Pillow```

### Installation
```
git clone https://github.com/Foxiks/gr-FengYun2.git
cd gr-FengYun2
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig
```

### Result
Here is your flowgraph for demodulating and decoding FengYun2 signal:

![1](/img/1.png)
