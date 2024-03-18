function rotate(s){
    var f = s.shift();
    s.push(f);
    return s;
}
function mirror(s, a){
    // console.log('s =', s, 'a =', a);
    if(s==']' && a=='[')
        return true;
    else if(s==')' && a=='(')
        return true;
    else if(s=='}' && a=='{')
        return true;
    else
        return false;
}
function check(s){
    var arr = [];
    
    arr.push(s[0]);
    
    for(let i=1; i<s.length; i++){
        // console.log('inner arr=', arr);
        if(arr.length > 0 && mirror(s[i], arr[arr.length-1])){
            arr.pop();
        }
        else{ //다른 괄호
            arr.push(s[i]);
        }
    
    }
    // console.log('arr=',arr);
    if(arr.length == 0){
        return true;
    }else{
        return false;
    }
}
function solution(s) {
    var answer = 0;
    var count =0;
    s = s.split("");
    for(let i=0; i<s.length; i++){
        if(check(s)){
            // console.log('s=',s);
            count++;
        }
            
        s = rotate(s);
    }
    
    
    return count;
}