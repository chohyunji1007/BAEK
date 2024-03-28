function findShortestRange(gems, kinds) {
    const targetCount = kinds.length;
    const countMap = new Map();
    let start = 0;
    let end = 0;
    let minRange = Infinity;
    let result = [0, 0];
    
    while (end < gems.length) {
        const gem = gems[end];
        if (!countMap.has(gem)) countMap.set(gem, 0);
        countMap.set(gem, countMap.get(gem) + 1);

        while (countMap.size === targetCount) {
            const currentRange = end - start;
            if (currentRange < minRange) {
                minRange = currentRange;
                result = [start, end];
            }

            const startGem = gems[start];
            countMap.set(startGem, countMap.get(startGem) - 1);
            if (countMap.get(startGem) === 0) countMap.delete(startGem);
            start++;
        }
        end++;
    }

    return result;
}

function solution(gems) {
    const kinds = [...new Set(gems)];
    return findShortestRange(gems, kinds).map(idx => idx + 1);
}
