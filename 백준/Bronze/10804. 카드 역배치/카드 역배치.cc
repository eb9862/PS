#include <stdio.h>

void    swap(int *a, int *b)
{
    int tmp;
    
    tmp = *a;
    *a = *b;
    *b = tmp;
}

void    reverse_card(int *card, int start, int end)
{
    while (start < end)
    {
        swap(&(card[start-1]), &(card[end-1]));
        start++;
        end--;
    }
}

int main(void)
{
    int card[20];
    int i;
    int start;
    int end;

    i = 0;
    while (i < 20)
    {
        card[i] = i + 1;
        i++;
    }
    for (int i = 0; i < 10; i++)
    {
        scanf("%d %d", &start, &end);
        reverse_card(card, start, end);
    }
    i = 0;
    while (i < 20)
    {
        printf("%d", card[i]);
        if (i != 19)
            printf(" ");
        i++;
    }
}