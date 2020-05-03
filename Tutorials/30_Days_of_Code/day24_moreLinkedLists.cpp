

          Node* removeDuplicates(Node *head)
          {
              Node* n =head;
              while (n != NULL)
              {
                  while ( (n->next != NULL) && ((n->data) == (n->next->data)) )
                  {
                    Node *temp = n->next;
                    n->next=n->next->next;
                    delete temp;
                  }
                n=n->next;
              }
              return head;
          }

