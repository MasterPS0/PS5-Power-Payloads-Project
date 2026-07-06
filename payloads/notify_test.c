#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stddef.h>

typedef struct notify_request {
  char useless1[45];
  char message[3075];
} notify_request_t;

int sceKernelSendNotificationRequest(int, notify_request_t*, size_t, int);

int main(void) {
  notify_request_t req;

  bzero(&req, sizeof req);
  strncpy(req.message, "Hello, world!", sizeof(req.message) - 1);
  req.message[sizeof(req.message) - 1] = '\0';

  return sceKernelSendNotificationRequest(0, &req, sizeof req, 0);
}
