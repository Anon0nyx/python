#!/usr/local/bin/python3

import os
LOGO = """

                      ..:::::::::..
                  ..:::aad8888888baa:::..
              .::::d:?88888888888?::8b::::.
            .:::d8888:?88888888??a888888b:::.
          .:::d8888888a8888888aa8888888888b:::.
         ::::dP::::::::88888888888::::::::Yb::::
        ::::dP:::::::::Y888888888P:::::::::Yb::::
       ::::d8:::::::::::Y8888888P:::::::::::8b::::
      .::::88::::::::::::Y88888P::::::::::::88::::.
      :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
      :::::::Y88888888888P::|::Y88888888888P:::::::
      ::::::::::::::::888:::|:::888::::::::::::::::
      `:::::::::::::::8888888888888b::::::::::::::'
       :::::::::::::::88888888888888::::::::::::::
        :::::::::::::d88888888888888:::::::::::::
         ::::::::::::88::88::88:::88::::::::::::
          `::::::::::88::88::88:::88::::::::::'
            `::::::::88::88::P::::88::::::::'
              `::::::88::88:::::::88::::::'
                 ``:::::::::::::::::::''
                      ``:::::::::''

"""

def change_mac_addr(interface, new_mac_addr):
	os.system('ip link set '+interface+' address '+new_mac_addr)
def main():
	interface = input('[*]Enter Interface to change: ')
	new_mac_addr = input('[*]Enter New Mac Addr: ')

	change_mac_addr(interface, new_mac_addr)

	print(LOGO)
	print('Mac Address changed successfully')
	os.system('ip addr show '+interface)

if __name__ == '__main__':
	main()
