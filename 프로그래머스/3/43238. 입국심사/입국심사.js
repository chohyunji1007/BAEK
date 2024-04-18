function solution(n, times) {
    let left = 0;
    let right = Math.max(...times) * n;
    let small = right; // 초기화 값을 더 작은 값으로 설정

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        let count = 0;

        times.forEach((d) => {
            count += Math.floor(mid / d);
        });

        if (count < n) {
            left = mid + 1;
        } else {
            // count가 n 이상이거나 정확히 n일 때만 small을 갱신
            small = Math.min(small, mid);
            right = mid - 1;
        }
    }

    return small;
}
