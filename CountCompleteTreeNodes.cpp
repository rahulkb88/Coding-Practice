/* https://leetcode.com/problems/count-complete-tree-nodes/ */

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    int leftHeight(TreeNode* root)
    {
        if(!root) return 0;
        return 1+leftHeight(root->left);
    }
public:
    int countNodes(TreeNode* root) {

        if(!root) return 0;
        int h = leftHeight(root);
        int res = (1<<h) - 1;
        TreeNode *cur = root;
        while(cur->left != NULL){
            int l = leftHeight(cur->left);
            int r = leftHeight(cur->right);
            if(r<l)
            {
                res = res - (1<<r);
                cur = cur->left;
            }
            else
                cur = cur->right;
        }
        return res;
    }
};
