
#use /dev/serial/by-id/
ps_id = {
    'ARA1' : 'usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_361A15108-if00-port0',
    'ARA5' : 'usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_361F16111-if00-port0',
    'ARA3' : 'usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_361C16125-if00-port0',
    }

#nominal, as of 11/24//2018
#
# 'ARA1' power supply serves ARA1 + ARA4
# 'ARA3' power supply serves ARA2 + ARA3
# 'ARA5' power supply serves ARA5 (+ PA)
ps_volts = {
    'ARA1' : 320.0,
    'ARA5' : 350.0,
    'ARA3' : 400.0,
    }
