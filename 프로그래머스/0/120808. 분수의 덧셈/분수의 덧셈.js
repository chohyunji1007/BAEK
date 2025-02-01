function solution(numer1, denom1, numer2, denom2) {
    // 최소공배수(LCM)를 찾아야 분모를 통일할 수 있음
    let lcm = (denom1 * denom2) / gcd(denom1, denom2);
    
    // 분모를 최소공배수로 맞춰서 분자 계산
    let newNumer1 = numer1 * (lcm / denom1);
    let newNumer2 = numer2 * (lcm / denom2);
    
    // 두 분수를 더함
    let sumNumer = newNumer1 + newNumer2;
    
    // 기약분수로 만들기 위해 GCD로 약분
    let commonDivisor = gcd(sumNumer, lcm);
    return [sumNumer / commonDivisor, lcm / commonDivisor];
}

// 최대공약수(GCD) 구하는 함수
function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
}