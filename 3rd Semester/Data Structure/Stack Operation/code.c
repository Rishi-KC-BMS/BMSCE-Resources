#include <stdio.h>

#define N 5
int stack[N];
int top = -1;


void push();
void pop();
void peek();
void display();

int main() {
    int choice;

    do {
        printf("\n--- Stack Menu ---\n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Peek (Top Element)\n");
        printf("4. Display Stack\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                peek();
                break;
            case 4:
                display();
                break;
            case 5:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }

    } while (choice != 5);

    return 0;
}
void push()
{
    int x;
    printf("Enter Data ");
    scanf("%d",&x);
    if(top == (N-1))
    {
        printf("Overflow");
    }
    else
    {
     top++;
     stack[top]=x;
    }
}

void pop()
{
    int item;
    if (top==-1)
    {
        printf("Underflow");
    }
    else
    {
        item = stack[top];
        top--;
        printf("%d",item);
    }
}

void peek()
{
    int item;
    if (top==-1)
    {
        printf("Underflow");
    }
    else
    {
        printf("%d",stack[top]);
    }
}

void display()
{
    int i;
    for(i=0;i<5;i++)
    {
    printf("%d\n",stack[i]);
    }

}
