#include <iostream>

using namespace std; 

struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

ListNode* swapPairs(ListNode* head) {
    if (head->next == NULL or head == NULL) {
        return head;
    }
    // swap the head and its next value 
    if( head->next->next != NULL){
        ListNode *temp = head->next->next;
        head->next->next = head;
        head->next = temp;
    }
    else{
        head->next->next = head;
        head->next = NULL;
    }
    
    ListNode* swapped_list = swapPairs(head->next);        
    head->next = swapped_list; 
    return head; 
}

int main(){
    int in[4] = [1,2,3,4];
    ListNode* head = ListNode(1);
    ListNode* two = ListNode(2);
    ListNode* three = ListNode(3);
    ListNode* four = ListNode(4);
    head->next = two;
    two->next = three;
    three->next = four;

    //print the list
    ListNode* pointer = head;
    while(pointer != NULL){
        cout << pointer->val << endl;
        pointer = pointer->next; 
    }

}