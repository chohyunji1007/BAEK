function solution(clothes) {
    var answer = 1; 
    var arr = {};
    
    for(var i=0; i<clothes.length; i++){
        arr[clothes[i][1]] = (arr[clothes[i][1]] || 0) + 1;
    }
    var arr2 = Object.values(arr);
    console.log(arr2);
    for (var j=0; j<arr2.length; j++) {
        answer *= (arr2[j]+1);
    }
    return answer-1;
}