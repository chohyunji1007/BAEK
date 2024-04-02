function solution(array, commands) {
    var answer = [];
    let num = array.slice();

    for(let i =0; i < commands.length ; i++){
        answer.push(num.slice(commands[i][0]-1,commands[i][1]).sort((a,b)=>a-b)[commands[i][2]-1]);
    }
    return answer;
}
