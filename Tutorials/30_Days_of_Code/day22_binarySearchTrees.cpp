

    int getHeight(Node* root) 
    {
        return (nullptr == root) ? -1 : 1 + std::max(getHeight(root->left), getHeight(root->right));
    }
