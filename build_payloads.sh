#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/payloads"
make clean
make PS5_PAYLOAD_SDK="${PS5_PAYLOAD_SDK:-/opt/ps5-payload-sdk}"
echo
echo "Done:"
ls -lh *.elf
