
function solution(brown, yellow) {
    var answer = [];
//     if(yellow*2 + 1*2 + 4 === brown){ //yellow가 한줄로
//         answer = [ yellow+2, 3];
//     }else if(yellow + 2*2 + 4 === brown){ //y 두줄
        
//     }else if((yellow/3)*2 + 3*2 + 4 === brown{ //세줄
        
//     }
    //공식 (yellow/줄수)*2 + 줄수*2 + 4(모서리) === brown
    var i=1;
    while(true){
        if((yellow/i)*2 + i*2 + 4 === brown){ //yellow가 한줄로
            return answer = [ yellow/i+2, i+2];
        }
        i+=1;
    }
    // return answer;
}