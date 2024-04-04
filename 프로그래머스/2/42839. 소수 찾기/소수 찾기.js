function isPrime(number) {
    if (number < 2) return false;
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) return false;
    }
    return true;
}

function makeCombinations(numbers) {
    const combinations = new Set();
    for (let length = 1; length <= numbers.length; length++) {
        const perms = getPermutations(numbers.split(''), length);
        perms.forEach(perm => combinations.add(parseInt(perm.join(''))));
    }
    return combinations;
}

function getPermutations(arr, length) {
    if (length === 1) return arr.map(el => [el]);
    const result = [];
    arr.forEach((fixed, index, origin) => {
        const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
        const perms = getPermutations(rest, length - 1);
        const attached = perms.map(perm => [fixed, ...perm]);
        result.push(...attached);
    });
    return result;
}

function solution(numbers) {
    const combinations = Array.from(makeCombinations(numbers));
    let count = 0;
    combinations.forEach(num => {
        if (isPrime(num)) count++;
    });
    return count;
}
