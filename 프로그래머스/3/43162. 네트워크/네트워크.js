function solution(n, computers) {
    var answer = 0;
    var visited = new Array(n).fill(false);
    
    function bfs(index){
        if(visited[index]){
            return;
        }
        visited[index] = true; // 현재 노드를 방문했다고 표시

        for(var i = 0; i < n; i++){
            if(index !== i && computers[index][i] === 1){
                bfs(i);
            }
        }
    }

    for(var j = 0; j < n; j++){ 
        if(!visited[j]){ // 아직 방문하지 않은 노드에 대해서만 BFS를 수행
            bfs(j);
            answer++;
        }
    }

    return answer;
}