function solution(triangle) {
    var answer = 0;
    var len = triangle.length;
    
//     function dp(sum, depth, i){
        
//         if(depth == len){
//             if(sum > answer){
//                 answer = sum;
//             }
//             return;
//         }else{
//             dp(sum + Number(triangle[depth][i]), depth+1, i);
//             dp(sum + Number(triangle[depth][i+1]), depth+1, i+1);
//         }
//     }
//     dp(Number(triangle[0][0]), 1, 0);
    
    for(var i=len-1; i>0; i--){
        for(var j=0; j<triangle[i].length; j++){
            triangle[i-1][j] += Math.max(triangle[i][j],triangle[i][j+1]);
        }
    }
    return triangle[0][0];
}
