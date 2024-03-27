function solution(wallpaper) {
    var answer = [50, 50, 0, 0];
    // var small = [50,50];
    // var big = [0,0];
    for(var i=0; i<wallpaper.length; i++){
        for(var j=0; j<wallpaper[i].length; j++)
        
        if(wallpaper[i][j]=='#'){
            if(i<answer[0]){
                answer[0] = i;
            }
            if(j<answer[1]){
                answer[1] = j;
            }
            if(i+1 > answer[2]){
                answer[2] = i+1;
            }
            if(j +1> answer[3]){
                answer[3] = j+1;
            }
            
        }
    }
    
    return answer;
}