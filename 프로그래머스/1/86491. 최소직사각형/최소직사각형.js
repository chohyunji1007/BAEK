function solution(sizes) {
    var answer = 0;
    var w = 0;
    var h = 0;
    
    // console.log(sizes);
    
    sizes.forEach((element, index, array)=>{
         // console.log(element, array);
        if(element[0]>element[1]){
            var c = element[0];
            element[0] = element[1];
            element[1] = c;
        }
        if(w < element[0]){
            w = element[0];
        }
        if(h < element[1]){
            h = element[1];
        }
    });
    // console.log(w, h);
    
    return w*h;
}