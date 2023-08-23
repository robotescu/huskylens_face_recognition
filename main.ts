basic.showIcon(IconNames.SmallHeart)
huskylens.initI2c()
huskylens.initMode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)
basic.showIcon(IconNames.Yes)
basic.forever(function () {
    huskylens.request()
    if (huskylens.isLearned(1)) {
        if (huskylens.isAppear_s(HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
            if (huskylens.isAppear(1, HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
                basic.showIcon(IconNames.Happy)
                music.ringTone(659)
                pins.digitalWritePin(DigitalPin.P1, 1)
                basic.pause(2000)
                pins.digitalWritePin(DigitalPin.P1, 0)
                music.stopAllSounds()
            } else {
                basic.showIcon(IconNames.Sad)
                music.ringTone(165)
                pins.digitalWritePin(DigitalPin.P2, 1)
                basic.pause(2000)
                pins.digitalWritePin(DigitalPin.P2, 0)
                music.stopAllSounds()
            }
        }
    }
    basic.pause(1000)
})
