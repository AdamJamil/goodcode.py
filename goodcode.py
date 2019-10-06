//segtree
class Node
{
    int L, R;
    int min = -1, max = -1; //any field you want to be able to query
    Node left = null, right = null;

    Node(int l, int r) //can also pass in additional information
    {
        L = l;
        R = r;
        if (L != R)
        {
            left = new Node(L, (L + R) / 2);
            right = new Node(1 + (L + R) / 2, R);
        }
    }

    int min(int l, int r) //generalized query function
    {
        if (min == -1)
        {
            if (L == R)
                return min = //degenerate case
            //this line below is unique to the type of query
            min = Math.min(left.min(left.L, left.R), right.min(right.L, right.R));
        }
        if (L == l && R == r) //segment matches node
            return min;
        if (l > left.R)
            return right.min(l, r); //subsegment of right only
        if (r < right.L)
            return left.min(l, r); //subsegment of left only
        return Math.min(left.min(l, left.R), right.min(right.L, r)); //subsegment of left and right
    }
}
