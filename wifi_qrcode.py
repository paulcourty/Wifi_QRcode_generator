import subprocess
import wifi_qrcode_generator

from PIL import Image, ImageDraw, ImageFont



def get_wifi_info():
    try:
    # Get wifi details from PC
        # Get wifi profile
        wifi_info = subprocess.check_output(['netsh', 'wlan', 'show', 'interfaces']).decode('utf-8').split('\n')
        wifi_name = str([profile_result.split(":")[1] for profile_result in wifi_info if 'Profile' + 16 * ' ' + ':' in profile_result][0]).strip()  # Wifi SSID

        # Get password
        password_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles', wifi_name, 'key=clear']).decode('utf-8').split('\n')
        password = str(
            [password_result.split(":")[1] for password_result in password_info if "Key Content" in password_result][0]).strip()

    except:
    # Ask wifi details from user
        print('Something went wrong, please enter manually your wifi:\n')
        wifi_name = input('Wifi name: ')
        password = input('Password: ')

    return wifi_name, password



def generate_qr_code(wifi_name, password, show_wifi_info = False):
    wifi = '\n| ' + wifi_name + '\n| ' + password
    print(wifi)

    # Generate QRcode
    qrcode = wifi_qrcode_generator.wifi_qrcode(wifi_name, False, 'WPA', password)

    if not show_wifi_info:
        new_qrcode = qrcode

    else:
        y_padding = 60
        old_size = qrcode.size
        new_size = (old_size[0], old_size[0] + y_padding)

        new_qrcode = Image.new("RGB", new_size, color=(255, 255, 255))
        new_qrcode.paste(qrcode, (0, y_padding))

        draw = ImageDraw.Draw(new_qrcode)
        font = ImageFont.truetype('Fonts\\Futura.ttf', 20)
        draw.text((38, 0), wifi, fill=(0, 0, 0), font=font)

    return new_qrcode



def main():
    qrcode_name = input('\nQR code name: ')
    print('\nWifi name & password:')
    wifi_name, password = get_wifi_info()
    qr_code = generate_qr_code(wifi_name, password, show_wifi_info = True)
    qr_code.save(qrcode_name + '.png')

    # Display QR code
    img = Image.open(qrcode_name + '.png')
    img.show()



if __name__ == '__main__':
    main()




