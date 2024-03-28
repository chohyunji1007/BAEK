function solution(nums) {
    var answer = 0;
    var len = nums.length;
    nums = [... new Set(nums)];

    return Math.min(nums.length, len/2);
}