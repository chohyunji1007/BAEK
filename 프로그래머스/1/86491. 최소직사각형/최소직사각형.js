function solution(sizes) {
    var answer = 0;
    var w = 0;
    var h = 0;
    for(var i=0; i<sizes.length; i++){
        sizes[i].sort((a, b)=>{return b-a;});
        w<sizes[i][0] ? w=sizes[i][0] : null ;
        h<sizes[i][1] ? h=sizes[i][1] : null ;
    }
    
    answer = w*h;
    return answer;
}