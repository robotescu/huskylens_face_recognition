basic.show_icon(IconNames.SMALL_HEART)
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)
basic.show_icon(IconNames.YES)

def on_forever():
    huskylens.request()
    if huskylens.is_learned(1):
        if huskylens.isAppear_s(HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
            if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
                basic.show_icon(IconNames.HAPPY)
                music.ring_tone(659)
                pins.digital_write_pin(DigitalPin.P1, 1)
                basic.pause(2000)
                pins.digital_write_pin(DigitalPin.P1, 0)
                music.stop_all_sounds()
            else:
                basic.show_icon(IconNames.SAD)
                music.ring_tone(165)
                pins.digital_write_pin(DigitalPin.P2, 1)
                basic.pause(2000)
                pins.digital_write_pin(DigitalPin.P2, 0)
                music.stop_all_sounds()
    basic.pause(1000)
basic.forever(on_forever)
