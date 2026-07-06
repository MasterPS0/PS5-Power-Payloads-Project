#include "common_power.h"

int main(void)
{
  send_notification("Restarting PS5...");
  sleep(2);
  ps5_reboot_syscall(RB_AUTOBOOT);
  return 0;
}
