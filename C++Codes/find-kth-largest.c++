#include "ArrayList.h"
#include "BST.h"

int arr[1000];
int i = 0;
void inOrderTraversal(Node* rootNode) {
    if(rootNode == NULL){
        return;
    }
    inOrderTraversal(rootNode -> leftChild);
    arr[i] = rootNode -> value;
    i += 1;
    //cout<<rootNode -> value<<" ";
    inOrderTraversal(rootNode -> rightChild);
}

int findKthMax(Node* rootNode, int k,int nodes) {
    inOrderTraversal(rootNode);
    return(arr[nodes-k]);
}

int main(){
  ArrayList 
  BinarySearchTree bsT(6);
        bsT.insertBST(4);
        bsT.insertBST(9);
        bsT.insertBST(5);
        bsT.insertBST(2);
        bsT.insertBST(8);
  
  cout << findKthMax(bsT.getRoot(),3,6) << endl;
}
