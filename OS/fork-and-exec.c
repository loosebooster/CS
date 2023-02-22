#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <err.h>

static void child()
{
    char *args[] = { "/bin/echo", "hello" , NULL};
    prinf("child-pid: %d.\n", getpid());
    fflush(stdout);
    execve("/bin/echo", args, NULL);
    err(EXIT_FAILURE, "exec() failed");
}

static void parent(pid_t pid_c)
{
    printf(parent-pid: %d, child-pid: %d.\n", getpid(), pid_c);
    exit(EXIT_SUCCESS);
}

int main(void)
{
    pid_t ret;
    ret = fork();
    if (ret == -1)
        err(EXIT_FAILURE, "fork() failed");
    if (ret == 0) {
        // child process came here because fork() returns 0 for child process child();
    } else {
        // parenr process came here because fork() returns the pid of newly created child process (> 1)
        parent(ret);
    }
    // shouldn't reach here
    err(EXIT_FAILURE, "shouldn't reach here");
}