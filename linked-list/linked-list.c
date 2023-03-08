#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* Define a linked list node that can hold a character pointer */
// TODO Define the structure for the linked list node
// NOTE: Name the structure: node
// NOTE: Name the member variable for the character pointer: value
struct node{
    char* value;
    struct node *next;
};


/* Function declarations */
struct node *addnode(struct node *the_node, char *value);
struct node *deletelastnode(struct node *the_node);
struct node *getlastnode(struct node *the_node);
void printlistiterative(struct node *the_node);
void printlistrecursive(struct node *the_node);

/* Use the functions to create and manipulate
   a linked list of character array values. */
int main() {
	struct node *root = NULL;

	root = addnode(root, "Alpha");
	root = addnode(root, "Beta");
	root = addnode(root, "Gamma");
	root = addnode(root, "Delta");

	printf("Print the list using recursion:\n");
	printlistrecursive(root);
	printf("\nPrint the list using iteration:\n");
	printlistiterative(root);

	printf("\nPrint the last node's value: %s\n", getlastnode(root)->value);

	printf("\nRepeatedly delete the last node and");
	printf("\nreprint the list until all nodes have been removed\n");
	while (root) {
		root = deletelastnode(root);
		printlistiterative(root);
        printf("\n");
	}

	return 0;
}


// addnode - add a node to the end of the linked list
// TODO Place the code for the function here
// NOTE: The return value must be the ROOT node
struct node *addnode(struct node *theNode, char *value){
	if(theNode == NULL){
        theNode = (struct node *)malloc(sizeof(struct node));
        theNode->value = value;
        theNode->next = NULL;
    }else { 
        struct node *current = theNode;
        while(current->next != NULL){
            current = current->next;
        }
        struct node *new = (struct node *)malloc(sizeof(struct node));
        new->value = value;
        current->next = new;
        new->next = NULL;     
        //pointer to a structer->member of the structure
    }
	return theNode;
}

// deletelastnode - delete the last node from the linked list
// TODO Place the code for the function here
// NOTE: The return value must be the ROOT node
struct node *deletelastnode(struct node *theNode) {
	if (theNode == NULL) {
		return NULL;
	}
	if (theNode->next == NULL) {
		free(theNode);
		return NULL;
	}
	struct node *current = theNode;
	while(current->next->next != NULL) {
		current = current->next;
	}
	free(current->next);
	current->next = NULL;
	return theNode;
	
}

// getlastnode - get the last node from the linked list
// TODO Place the code for the function here
// NOTE: THe return value must be the LAST node
struct node *getlastnode(struct node *theNode) {
	if (theNode == NULL) {
		return NULL;
	}
	struct node* current = theNode;
	while(current->next != NULL) {
		current = current->next;
	}
	return current;
}

// printlistrecursive - print out the list values using recursion
// TODO Place the code for the function here
void printlistrecursive(struct node *theNode) {
	if(theNode != NULL) {
		printf("%s ", theNode->value);
		printlistrecursive(theNode->next);
	}

}

// printlistiterative - print out the list values using iteration
// TODO Place the code for the function here
void printlistiterative(struct node *theNode) {
	for (struct node *n = theNode; n; n = n->next){
		printf("%s", n->value);
	}
}
