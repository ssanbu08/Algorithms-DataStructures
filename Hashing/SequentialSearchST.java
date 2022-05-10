public class SequentialSearchST<Key, Value>
{
    private Node first;     // first node in the linked list

    // Inner Class
    private class Node
    {   // linked-list Node
        Key key;
        Value val;
        Node next;
        public Node(Key key, Value val, Node next)
        {
            this.key = key;
            this.val = val;
            this.next =  next;
        }
    }

    public Value get(Key key)
    {
        for (Node x = first; x != null; x = x.next)
            if (key.equals(x.key))
                return x.val;   // search hit
        return null;            // search miss
    }
    
    public void put(Key key, Value val)
    {   // Search for key. Update value if found; grow table if new
        for (Node x = first; x != null; x = x.next)
            if (key.equals(x.key))
            {   x.val = val; return;    }       // Search hit: Update val
        first = new Node(key, val, first);      // Search miss: add new Node.
    }
}