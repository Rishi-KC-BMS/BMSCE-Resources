#include <stdio.h>

int adj[20][20], visited[20];
int n, queue[20], front = 0, rear = -1;

void bfs(int start) {
    int i;
    queue[++rear] = start;
    visited[start] = 1;

    while (front <= rear) {
        start = queue[front++];
        printf("%d ", start);

        for (i = 1; i <= n; i++) {
            if (adj[start][i] == 1 && visited[i] == 0) {
                queue[++rear] = i;
                visited[i] = 1;
            }
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

    printf("BFS Traversal: ");
    bfs(start);

    return 0;
}
