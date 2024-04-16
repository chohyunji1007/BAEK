function solution(prices) {
    const len = prices.length;
    const answer = new Array(len).fill(0);
    const stack = [];

    for (let i = 0; i < len; i++) {
        while (stack.length > 0 && prices[stack[stack.length - 1]] > prices[i]) {
            const top = stack.pop();
            answer[top] = i - top;
        }
        stack.push(i);
    }

    // 스택에 남은 요소 처리
    while (stack.length > 0) {
        const top = stack.pop();
        answer[top] = len - 1 - top;
    }

    return answer;
}
