/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        ListNode* prev = head;
        ListNode* curr = head->next;
        if(curr->next==nullptr)return {-1,-1};
        ListNode* nxt = curr->next;
        int first = -1;
        int last = -1;
        vector<int> ans(2,-1);
        int point = 2;
        while(nxt!=nullptr){
        if(curr->val>max(prev->val,nxt->val) || curr->val<min(prev->val,nxt->val)){
            if(first==-1 && last== -1){
                first= point;
                last = point;
            }
            else{
                ans[1]=point-first;
                ans[0]=(ans[0]==-1?point-last:min(ans[0],point-last));
                last=point;
            }
        }
        nxt=nxt->next;
        curr=curr->next;
        prev=prev->next;
        point++;
        }
        return ans;
    }
};