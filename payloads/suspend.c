#include "common_power.h"

/*
 * Rest Mode / Standby
 * Symbol found in:
 * /opt/ps5-payload-sdk/target/lib/libSceSystemService.so
 */
int sceSystemStateMgrEnterStandby(void);

int main(void)
{
    send_notification("Entering Rest Mode...");
    sleep(2);

    int ret = sceSystemStateMgrEnterStandby();

    if (ret != 0) {
        char msg[128];
        snprintf(msg, sizeof(msg), "EnterStandby failed: 0x%08X", ret);
        send_notification(msg);
    }

    return ret;
}
