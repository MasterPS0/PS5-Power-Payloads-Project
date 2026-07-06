PS5_PAYLOAD_SDK ?= /opt/ps5-payload-sdk

CC := $(PS5_PAYLOAD_SDK)/bin/prospero-clang
CFLAGS := -Wall -Wextra -O2 -I.
LDFLAGS := -L$(PS5_PAYLOAD_SDK)/target/lib -lkernel -lSceSystemService

TARGETS := notify_test.elf reboot.elf poweroff.elf suspend.elf

all: $(TARGETS)

notify_test.elf: notify_test.c
	$(CC) $(CFLAGS) notify_test.c -o $@ $(LDFLAGS)

reboot.elf: reboot.c common_power.h
	$(CC) $(CFLAGS) reboot.c -o $@ $(LDFLAGS)

poweroff.elf: poweroff.c common_power.h
	$(CC) $(CFLAGS) poweroff.c -o $@ $(LDFLAGS)

suspend.elf: suspend.c common_power.h
	$(CC) $(CFLAGS) suspend.c -o $@ $(LDFLAGS)

clean:
	rm -f *.elf *.o
