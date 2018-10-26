/*
 * 	dfs routine, finds node v is in subtree rooted at node u
 */

int intime[MAX], outtime[MAX];

int counter = 0;
void dfs(int u, int dad) {
    intime[u] = counter++;
    for (int v : T[u]) {
        if (v != dad) {
            preprocess(v, u);
        }
    }
    outtime[u] = counter++;
}

bool isInSubtree(int u, int v) {
    return ((intime[u] <= outtime[v]) && (outtime[u] >= intime[v]));
}
