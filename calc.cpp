#include <stdio.h>

extern "C" int add(int a, int b) {
    return a + b;
}
extern "C" int sub(int a, int b) { return a - b; }
extern "C" int mul(int a, int b) { return a * b; }
extern "C" int div(int a, int b) { return a / b; }


