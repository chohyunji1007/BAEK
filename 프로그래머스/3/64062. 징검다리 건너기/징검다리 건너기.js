function solution(stones, k) {
    let left = 1;
    let right = 200000000;
    
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        console.log('left = ',left, 'right=', right,'mid=', mid);
        let count = 0;
        let flag = false;
        
        for (let i = 0; i < stones.length; i++) {
            if (stones[i] < mid) {
                count++;
                if (count === k) {
                    flag = true;
                    break;
                }
            } else {
                count = 0;
            }
        }
        
        if (flag) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    
    return left-1;
}