function solution(babbling) {
    var answer = 0;
    // aya , ye , woo , ma 4가지만 가능
    
    
    var a = ["aya", "ye", "woo", "ma", ""];
    var ar = make(a);
    for(const entry of babbling){
        if(ar.includes(entry)){ 
            // console.log(entry);
            answer++;
        }
    }
    
    return answer;
}
function make(a){
    var arr = a.filter((data)=>data!=='');
    var len = a.length;
    for(var i=0; i<len; i++){
        var fir = a[i];
        for(var j=0; j<len; j++){
            if(i!=j){
                var second = fir + a[j];
                arr.push(second);
            }
            
            for(var k=0; k<len; k++){
                if(j!=k){
                    var th = second + a[k];
                    arr.push(th);
                }
                
                for(var q=0; q<len; q++){
                    if(k!=q){
                        var fo = th+a[q];
                        arr.push(fo);
                    }
                    
                }
            }
        }
    }
    arr = [... new Set(arr)];
    console.log(arr);
    return arr;
    
}