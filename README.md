# ESP8266-TWO-TEMPERATURES

## Background

My dad gave me a project. He asked me to build him something that would:

- Measure temperatures
- At two different locations 
- Every hour, and 
- Log those temperatures 
- In the cloud

This gave me an excellent opportunity to use a [NodeMCU D1 mini ESP8266](https://www.amazon.com/gp/product/B081PX9YFV/) that I had lying around. They cost me about $3 each, they have can handle multiple sensors, they have WiFi built in, and I can write in Python (well, technically, [Micropython](https://docs.micropython.org/en/latest/)).

## Components

- One (1) NodeMCU D1 mini ESP8266
- Two (2) [DHT11 Sensors](https://www.amazon.com/dp/B01DKC2GQ0)
- Some [Dupont](https://www.mattmillman.com/why-do-we-call-these-dupont-connectors/) crimp supplies

## Approach

TODO

## Setting up Firebase

## Usage

Once I got this thing wired up, I needed to figure out how to actually run the script. Turns out that the tool I needed for that was `ampy`.

```sh
mv config.py.example config.py
ampy -p /dev/tty.usbserial-110 put config.py
ampy -p /dev/tty.usbserial-110 put wifi.py
ampy -p /dev/tty.usbserial-110 put main.py
```

To watch what was happening: `screen /dev/tty.usbserial-110 115200`.

## Miscellaneous notes

- **Secret management**. I had to deal with the fact that I have a few secrets I didn't want to commit in source code. More broadly, this is an issue of [storing config in the environment](https://12factor.net/config) and separating config from code. To handle this, I created `config.py`, defined my variables there, and then passed them in the code. I haven't really seen the use of this pattern for microcomputers documented anywhere, but I like it quite a bit.

- **Choosing sensors**. I found myself confused about what temperature sensor to buy. I ended up buying some sensors from Adafruit (DHT22), but realized after the fact that it has a hardcoded "I2C address," which meant I could only have one sensor running at a time. So, I ended up buying a different set of sensors from Amazon (LM75A) that allowed for a configurable I2C address. At some point, though, I realized that I was wildly overthinking it and that I could avoid the whole I2C address thing by just making it simpler. So, I bought some DHT11s, which does not use I2C at all and can just connect to a GPIO pin. This simplified things quite a bit.

- **Making the connectors work**. I don't know why, but I spent way too much time and energy thinking about how to connect multiple sensors to the same pins (5V and ground). I started getting wild ideas about breadboards and PCB with solder jumps. Then I slowed down and just decided to have two wires in a single dupont connector. This seemed to work just fine. Good, meet your enemy: perfection.