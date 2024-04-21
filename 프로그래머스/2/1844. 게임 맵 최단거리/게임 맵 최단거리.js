function solution(maps) {
    const N = maps.length;
    const M = maps[0].length;
    const dx = [1, -1, 0, 0]; 
    const dy = [0, 0, -1, 1];
    
    const queue = [{x: 0, y: 0, dist: 1}]; 
    const visited = new Array(N).fill().map(() => new Array(M).fill(false));

    while (queue.length > 0) {
        const {x, y, dist} = queue.shift(); 

        if (x === N - 1 && y === M - 1) { 
            return dist;
        }

        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (nx >= 0 && nx < N && ny >= 0 && ny < M && maps[nx][ny] === 1 && !visited[nx][ny]) {
                visited[nx][ny] = true; 
                queue.push({x: nx, y: ny, dist: dist + 1}); 
            }
        }
    }

    return -1; 
}