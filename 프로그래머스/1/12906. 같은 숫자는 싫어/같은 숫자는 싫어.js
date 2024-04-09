function solution(arr)
{
    var answer = [];
    var stack =[];
    stack.push(arr[0]);
    answer.push(arr[0]);
    for(var i=1; i<arr.length; i++){
        if(stack.pop()!==arr[i]){
            answer.push(arr[i]);
            stack.push(arr[i]);
        }else{
            stack.push(arr[i]);
        }
        
    }
    
    return answer;
}