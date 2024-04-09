function solution(n, wires) {
    let answer = Infinity;

    function dfs(start, newArr) {
        let stack = [start];
        let count = 0;
        const visited = new Array(n).fill(false);

        while (stack.length > 0) {
            const cur = stack.pop();
            if (!visited[cur]) {
                visited[cur] = true;
                count++;
                for (let i = 0; i < newArr.length; i++) {
                    if (newArr[i][0] === cur + 1 && !visited[newArr[i][1] - 1]) {
                        stack.push(newArr[i][1] - 1);
                    } else if (newArr[i][1] === cur + 1 && !visited[newArr[i][0] - 1]) {
                        stack.push(newArr[i][0] - 1);
                    }
                }
            }
        }
        return count;
    }

    for (let i = 0; i < wires.length; i++) {
        const newArr = wires.filter((_, index) => index !== i);
        const first = dfs(newArr[0][0] - 1, newArr);
        const second = n - first;
        answer = Math.min(answer, Math.abs(first - second));
    }

    return answer;
}
