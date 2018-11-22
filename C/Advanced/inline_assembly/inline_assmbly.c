#include <stdio.h>

int main() {

  int main()
{

    printf("Running the application");
    int x = 1;

    asm ("movl %1, %%eax;"
         "movl %%eax, %0;"
         :"=r"(x) /* x is output operand and it's related to %0 */
         :"r"(11)  /* 11 is input operand and it's related to %1 */
         :"%eax"); /* %eax is clobbered register */

   printf("Hello x = %d\n", x);
}
}