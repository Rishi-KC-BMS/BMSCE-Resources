#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node* prev;
    struct node* next;
};

struct node* create(struct node* head, int data) {
    struct node* newnode = malloc(sizeof(struct node));
    newnode->data = data;
    newnode->prev = NULL;
    newnode->next = NULL;

    if (head == NULL)
        return newnode;

    struct node* temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newnode;
    newnode->prev = temp;

    return head;
}

struct node* insert_left(struct node* head, int value) {
    struct node* newnode = malloc(sizeof(struct node));
    newnode->data = value;
    newnode->prev = NULL;
    newnode->next = head;


    if (head != NULL)
        head->prev = newnode;

    return newnode;
}
struct node* insert_right(struct node* head, int value) {
    struct node* newnode = malloc(sizeof(struct node));
    newnode->data = value;
    newnode->prev = NULL;
    newnode->next = NULL;

    if (head == NULL)
        return newnode;

    struct node* temp = head;
    while (temp->next != NULL)
        temp = temp->next;

    temp->next = newnode;
    newnode->prev = temp;

    return head;
}


struct node* delete_value(struct node* head, int value) {
    struct node* temp = head;

    while (temp != NULL && temp->data != value)
        temp = temp->next;

    if (temp == NULL)
    {
        return head;
        printf("Value not found \n");
    }

    if (temp->prev == NULL)
        head = temp->next;
    else
        temp->prev->next = temp->next;

    if (temp->next != NULL)
        temp->next->prev = temp->prev;

    free(temp);
    return head;
}

void display(struct node* head) {
    struct node* temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}


int main() {
    struct node* head = NULL;
    int choice, val;

    printf("\n1. Create Node \n2. Insert at Left \n3. Insert at Right \n4. Delete Value\n5. Display\n6. Exit\n");

    while (1) {
        printf("\nEnter choice : ");
        scanf("%d", &choice);

        if (choice == 1) {
            printf("Enter value : ");
            scanf("%d", &val);
            head = create(head, val);
        }
        else if (choice == 2) {
            printf("Enter value to insert : ");
            scanf("%d", &val);
            head = insert_left(head, val);
        }
          else if (choice == 3) {
            printf("Enter value to insert : ");
            scanf("%d", &val);
            head = insert_right(head, val);
        }
        else if (choice == 4) {
            printf("Enter value to delete: ");
            scanf("%d", &val);
            head = delete_value(head, val);
        }
        else if (choice == 5) {
            printf("List: ");
            display(head);

        }
         else if (choice == 6) {
            break;

        }
        else {
            printf("Invalid choice\n");
        }
    }
    return 0;
}
