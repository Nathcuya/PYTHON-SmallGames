#include <easyx.h>
#include <stdio.h>
int main()
{
    initgraph(500, 500);

    circle(0, 0, 300);
    getchar();

    closegraph();
    return 0;
}
