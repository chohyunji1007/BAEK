function solution(answers) {
    var answer = [];
    var f = [1, 2, 3, 4, 5];
    var s = [2, 1, 2, 3, 2, 4, 2, 5];
    var t = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];

    var arr={};
    for(var i=0; i<answers.length; i++){
        if(answers[i] == f[i%5])
            arr[1] = (arr[1] || 0)+1;
        if(answers[i] == s[i%8])
            arr[2] = (arr[2] || 0)+1;
        if(answers[i] == t[i%10])
            arr[3] = (arr[3] || 0)+1;
    }
    
    
    var maxScore = Math.max(...Object.values(arr));

    for (var key in arr) {
        if (arr[key] === maxScore) {
            answer.push(parseInt(key));
        }
    }
        
    
    return answer;
}