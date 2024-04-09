function solution(k, dungeons) {
    let answer = 0;
    let visited = new Array(dungeons.length).fill(false);

    function dfs(k, count) {

        for(let i=0; i<dungeons.length; i++) {
            if(k >= dungeons[i][0] && !visited[i]) {
                // 방문 체크
                visited[i] = true;
                dfs(k-dungeons[i][1], count + 1);
                visited[i] = false; 
            }
        }

        answer = Math.max(answer, count);
    }

    dfs(k, 0);

    return answer;
}
