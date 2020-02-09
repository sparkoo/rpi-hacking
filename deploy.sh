#!/usr/bin/env bash

set -x
set -e

TARGET_IP=192.168.1.101
TARGET_OUT=/home/pi

scp -r buzzer pi@${TARGET_IP}:${TARGET_OUT}
scp -r display pi@${TARGET_IP}:${TARGET_OUT}
scp -r keyboard pi@${TARGET_IP}:${TARGET_OUT}
scp -r nfc pi@${TARGET_IP}:${TARGET_OUT}
