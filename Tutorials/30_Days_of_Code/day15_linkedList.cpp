

      Node* insert(Node *head,int data)
      {
          //Complete this method
          Node **prev = &head;
           while(*prev)
          {
            prev = &((*prev)->next);
          }
          *prev = new Node(data);
          return head;
      };

