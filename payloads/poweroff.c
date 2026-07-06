#include "common_power.h"

int main(void)
{
  send_notification("Turning Off PS5...");
  sleep(2);
  ps5_reboot_syscall(RB_HALT | RB_POWEROFF);
  return 0;
}
