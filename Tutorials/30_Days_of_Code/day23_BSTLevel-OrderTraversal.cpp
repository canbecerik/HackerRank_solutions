

	void levelOrder(Node * root){
      //Write your code here
      queue<Node *> q;    

      while (root)
      {
          
          std::cout << root->data << " ";
          if (root->left)
          {
              q.push(root->left);
          }
          if (root->right)
          {
              q.push(root->right);
          }

          if (!q.empty())
          {
              root = q.front();
              q.pop();
          }
          else {
            root=NULL;
          }

      }
  	
  
	}

