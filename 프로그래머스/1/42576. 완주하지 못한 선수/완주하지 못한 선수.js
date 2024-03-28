function solution(participant, completion) {
    // var answer = '';

    const arr = {};
    participant.forEach(element => {
        arr[element] = (arr[element] || 0) + 1;
    });
    for(var i=0; i<completion.length; i++){
        arr[completion[i]] -=1;
    }
    const result = Object.keys(arr).find(key => arr[key] === 1);
    return result;
}