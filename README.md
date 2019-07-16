Forked from kendryte-standalone-demo repo

Added UART data transmission to KPU 20 class detection. Transmits the detected object class number over UART(Baud 115200, TX 5 RX 4).

Added sample code for Arduino mega(which prints object name on Serial) and Raspberry PI(speaks the objects out loud with flite TTS).

Included pre-built binary, which you can upload to K210 with the following command on Linux

sudo python3 kflash.py -t kpu.bin
