function check(arr, char){
    var a = false;
    if(arr.length ==0){
        return a;
    }else{
        if(arr[arr.length-1] ==='(' && char ===')'){
            a = true;
        }
    }
    
    return a;
        
}
function solution(s){
    var answer = false;
    let stack=[];
    s = s.split('');
    // console.log(s);
    for(var i=0; i<s.length; i++){
        
        if(check(stack, s[i])){

            stack.pop();
        }else{
            stack.push(s[i]);
        }
       
    }
    // console.log(stack);
    if(stack.length ==0)
        answer = true;
    return answer;
}