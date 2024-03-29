# gr-fengyun2
OOT GnuRadio blocks for decode S-VISSR2.0 Images from FengYun-2x satellites

### Source
Forked from [gr-soniks](https://github.com/Foxiks/gr-soniks)

### Install Dependencies
1. GNURadio 3.10
2. gr-Satellites: https://github.com/daniestevez/gr-satellites
3. ```sudo apt-get install libjpeg-dev zlib1g-dev gcc build-essential libffi-dev python3-dev python3-cffi python3-opencv python3-pip git cmake libusb-1.0-0-dev libboost-all-dev gnuradio-dev liblog4cpp5-dev swig```
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

![1](/readme/1.png)

### Visible channel (Original width: 9168px)

![2](/readme/3.png)

### Several crops

![3](/readme/1_2.png)

![4](/readme/2.png)

### Low res IR channels

![5](/readme/IR-CH_1.png)

![6](/readme/IR-CH_2.png)

![7](/readme/IR-CH_3.png)

![8](/readme/IR-CH_4.png)

### Documentation of the S-VISSR 2.0 data transfer protocol
[[FY2VISSR2.0](/readme/FY2VISSR2_0_en.pdf)]
