/*
This implementation, implements the linkedlist 
directly in this class, instead of referring to 
SequentialSearchST 
*/

public class SeparateChainingHashST2<Key, Value>
{

    private class Node
    {
        Key key;
        Value val;
        Node next;

        public Node(Key key, Value val, Node next)
        {
            this.key = key;
            this.val = val;
            this.next = next;
        }
    }

    public SeparateChainingHashST2(int M)

    public hash(Key key)
    {
        return key.hashcode() & 07ffffff
    }

    public void put(Key key, Value val) 
    {
        // If key already present update the value
        // If key is not there insert 
    }

    public void get(Key key)
    {

    }
}