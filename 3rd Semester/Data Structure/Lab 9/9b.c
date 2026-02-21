#include <stdio.h>

int adj[20][20], visited[20];
int n;

void dfs(int start) {
    int i;
    visited[start] = 1;
    printf("%d ", start);

    for (i = 1; i <= n; i++) {
        if (adj[start][i] == 1 && visited[i] == 0) {
            dfs(i);
        }
    }
}

int main() {
    int i, j, start;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter adjacency matrix:\n");
    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            scanf("%d", &adj[i][j]);
        }
        visited[i] = 0;
    }

    printf("Enter starting vertex: ");
    scanf("%d", &start);

    printf("DFS Traversal: ");
    dfs(start);

    return 0;
}
