
function solution(s) {
    var answer = [];
    // num.toString(2) 2진수
    answer=s;
    var ori_len = answer.length;
    var count = 0;
    var z_count = 0;
    while(answer!="1"){
        answer= answer.split('');
        
        answer = answer.filter((data) => data !== "0");
        
        var len = answer.length;
        z_count += ori_len - len;
        console.log('z_count =', z_count, 'ori_len=', ori_len, 'len =', len);
        answer = len.toString(2);
        count++;
        ori_len = answer.length;
    }
    answer = [count, z_count];
    return answer;
}