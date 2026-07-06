# PS5 Power Payloads Project

Default sender:
- IP: `192.168.137.250`
- Port: `9021`

Payloads:
- `payloads/reboot.elf`   -> Restart PS5
- `payloads/poweroff.elf` -> Turn Off PS5
- `payloads/suspend.elf`  -> Rest Mode template

## Build on WSL/Linux

```bash
cd PS5_Power_Payloads_Project
chmod +x build_payloads.sh
./build_payloads.sh
```

Or:

```bash
cd payloads
make PS5_PAYLOAD_SDK=/opt/ps5-payload-sdk
```

## Send from Windows

Double click:

```txt
Run_Sender_Windows.bat
```

The sender sends the selected `.elf` file directly to:

```txt
192.168.137.250:9021
```

## Notes

`reboot.elf` and `poweroff.elf` use the FreeBSD/Orbis-style reboot syscall.
They need a payload environment with enough privileges.

`suspend.elf` is a safe template. Your PS5 logs show Rest Mode is triggered by ShellUI:

```txt
PowerManager.RequestStateChange state:Suspend
SystemStateMgr: Enter Standby Mode Request from ShellUI
```

That ShellUI/SystemStateMgr request is not exposed the same way as `reboot()`.
If you find the correct exported call or IPC route, add it inside `payloads/suspend.c`.
