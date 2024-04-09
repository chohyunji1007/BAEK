function solution(word) {
    let answer = 0;
    let words = ['A', 'E', 'I', 'O', 'U'];
    let temp = [];

    function dfs(str, depth) {
        if (depth <= 5) {
            temp.push(str);

            for (let i = 0; i < words.length; i++) {
                dfs(str + words[i], depth + 1);
            }
        }
    }

    dfs('', 0);
    temp.sort(); // 모든 경우의 수를 사전순으로 정렬
    answer = temp.indexOf(word); // 0부터 시작하는 인덱스를 1부터 시작하는 인덱스로 변경

    return answer;
}
