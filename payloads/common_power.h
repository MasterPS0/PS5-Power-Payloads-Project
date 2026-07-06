#pragma once

#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stddef.h>
#include <unistd.h>
#include <sys/syscall.h>

typedef struct notify_request {
  char useless1[45];
  char message[3075];
} notify_request_t;

int sceKernelSendNotificationRequest(int, notify_request_t*, size_t, int);

static int send_notification(const char *text)
{
  notify_request_t req;

  bzero(&req, sizeof req);
  strncpy(req.message, text, sizeof(req.message) - 1);
  req.message[sizeof(req.message) - 1] = '\0';

  return sceKernelSendNotificationRequest(0, &req, sizeof req, 0);
}

static long ps5_reboot_syscall(int flags)
{
  return syscall(55, flags);
}

#define RB_AUTOBOOT 0x0000
#define RB_HALT 0x0008
#define RB_POWEROFF 0x4000
