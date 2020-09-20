import serial
from time import sleep

def main():
    aqi = serial.Serial('/dev/serial0', 9600)

    while aqi.is_open:
        while (aqi.in_waiting > 31):
            if (aqi.read() != b'B'):
                continue
            if (aqi.read() != b'M'):
                continue
            print(AQIData(aqi.read(30)), '\n')

        print('serial buffer empty, sleeping')
        sleep(2);

class AQIData:
    def __init__(self, data):
        self.pm1 = int.from_bytes(data[2:4], 'big')
        self.pm25 = int.from_bytes(data[4:6], 'big')
        self.pm10 = int.from_bytes(data[6:8], 'big')
        self.environment_pm1 = int.from_bytes(data[8:10], 'big')
        self.environment_pm25 = int.from_bytes(data[10:12], 'big')
        self.environment_pm10 = int.from_bytes(data[12:14], 'big')
        self.particles_03um = int.from_bytes(data[14:16], 'big')
        self.particles_05um = int.from_bytes(data[16:18], 'big')
        self.particles_1um = int.from_bytes(data[18:20], 'big')
        self.particles_25um = int.from_bytes(data[20:22], 'big')
        self.particles_5um = int.from_bytes(data[22:24], 'big')
        self.particles_10um = int.from_bytes(data[24:26], 'big')

    def __str__(self):
        return '\n'.join([f'standard PM1:\t\t\t{self.pm1}', f'standard PM2.5:\t\t\t{self.pm25}',
            f'standard PM10:\t\t\t{self.pm10}', f'atmospheric PM1:\t\t{self.environment_pm1}',
            f'atmospheric PM2.5:\t\t{self.environment_pm25}',
            f'atmostpheric PM10:\t\t{self.environment_pm10}', f'0.3um particles:\t\t{self.particles_03um}',
            f'0.5um particles:\t\t{self.particles_05um}', f'1um particles:\t\t\t{self.particles_1um}',
            f'2.5um particles:\t\t{self.particles_25um}', f'5um particles:\t\t\t{self.particles_5um}',
            f'10um particles:\t\t\t{self.particles_10um}'])


if __name__ == '__main__':
    main()
