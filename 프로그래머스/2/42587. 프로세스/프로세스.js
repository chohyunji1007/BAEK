function solution(priorities, location) {
    var answer = 0;
    let len = priorities.length;
    // let check = priorities[location-1];
    const arr = Array.from({ length: priorities.length }, (_, index) => index);
    while(priorities.length != 0){
        // console.log('p=', priorities);
        // console.log('a=', arr);
        if(Math.max(...priorities.slice(0,len), priorities[0]) != priorities[0])        {
            var a = priorities.shift();
            priorities.push(a);
            // console.log('p1=', priorities);
            var b = arr.shift();
            arr.push(b);
            // console.log('a1=', arr);
            
        }else{
            var c = priorities.shift();
            answer+=1;
            // console.log('answer=', answer);
            if(arr.shift() == location){
                return answer;
            }
           
        }
        
        
    }
    return answer;
}