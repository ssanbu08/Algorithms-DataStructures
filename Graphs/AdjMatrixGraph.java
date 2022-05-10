import java.util.zip.ZipException;

public class AdjMatrixGraph
{
    private int V;
    private boolean[][] adj;

    public Graph(int V)
    {
        this.V = V;
        adj = new boolean[V][V];
    }

    public void addEdge(int v, int w)
    {
        adj[v][w] = true;
        adj[w][v] = true;
    }

    public Iterable<Integer> adj(int v)
    {
        return new AdjIterator(v);
    }
}