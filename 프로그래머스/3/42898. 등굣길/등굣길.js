function solution(m, n, puddles) {
    var maps = Array.from({ length: n }, () => new Array(m).fill(0));
    
    // 출발점
    maps[0][0] = 1;
    
    // 물 웅덩이 표시
    for (let [x, y] of puddles) {
        maps[y-1][x-1] = -1;
    }
    
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (maps[i][j] === -1) { // 웅덩이인 경우 건너뜀
                maps[i][j] = 0;
                continue;
            }
            if (i > 0) maps[i][j] += maps[i-1][j];
            if (j > 0) maps[i][j] += maps[i][j-1];
            maps[i][j] %= 1000000007;
        }
    }

    return maps[n-1][m-1];
}
