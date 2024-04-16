function solution(bridge_length, weight, truck_weights) {
    // 최대 bridge_length대, 최대 weight 무게, 트럭별 무게 truck_weights
    var answer = 1; //초
    var stack1 = [truck_weights.shift()];
    var stack2 = [1]; //들어간 시간을 넣고 +1하면서 bridge_length가 지났나 확인
    while(stack1.length != 0){
        // console.log('time = ',answer, 'stack2=',stack2);
        if(stack2[0]>bridge_length){
            var out = stack1.shift();
            stack2.shift();
            // console.log('time = ',answer,', out = ',out);
        }
        var sum=0;
        stack1.forEach(e =>{
            sum+=e;
        });
        if(sum + truck_weights[0] <= weight){
            stack1.push(truck_weights.shift());
            stack2.push(1);
        }
        
        
        answer++; //1초 추가
        stack2 = stack2.map(e => e + 1);

    }
    return answer-1;
}