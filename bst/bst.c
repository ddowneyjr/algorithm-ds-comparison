#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct node {
    int value;
    struct node* left;
    struct node* right;
};

struct node* insert(struct node*, int val);
void print(struct node*);

int main() {
    struct node* head;
    head = insert(head, 7);
    insert(head, 3);
    insert(head, 10);
    insert(head, -5);
    insert(head, 100);
    print(head);
}


struct node* insert(struct node* root, int val){
    
    if(root == NULL){
        // printf("here");
        struct node* new = (struct node *) malloc(sizeof(struct node));
        new->value = val;
        new->left = NULL;
        new->right = NULL;
        return new;
    }
    
    if(val >= root->value){
        if(root->right == NULL){
            struct node* new = (struct node *) malloc(sizeof(struct node));
            new->value = val;
            new->left = NULL;
            new->right = NULL;
            root->right = new;
            return new;
        }
        else{
            insert(root->right, val);
        }
    }
    else{
        if(root->left == NULL){
            struct node* new = (struct node *) malloc(sizeof(struct node));
            new->value = val;
            new->left = NULL;
            new->right = NULL;
            root->left = new;
            return new;
        }
        else{
            insert(root->left, val);
        }
    }

}


void print(struct node* root){
    if(root != NULL){
        print(root->left);
        printf("%d \n", root->value);
        print(root->right);
    }

}