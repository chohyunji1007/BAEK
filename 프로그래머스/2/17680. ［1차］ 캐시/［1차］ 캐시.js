function rotate(arr, name){
    // console.log(arr.indexOf(name));
    let index = arr.indexOf(name);
    let out = arr.splice(index,1);
    arr.push(out[0]);
    return arr;
}
// function upper(arr){
//     for(var i=0; i<arr.length; i++){
//         arr[i]= arr[i].toUpperCase();
//     }
//     return arr;
// }
function solution(cacheSize, cities) {
    let answer = 0;
    let cache = [];
    // cities = upper(cities);
    cities = cities.map(e => e.toLowerCase());
    
    for(let i=0; i<cities.length; i++){
        // console.log(cache);
        if(cache.length !=0 && cache.includes(cities[i]) && cacheSize!=0){
            answer+=1; //hit
            // console.log('1=',cache);
            if(i!= cache.length-1){
                rotate(cache, cities[i]);
            }
            
            // console.log('2=',cache);
        }else{
            answer+=5; //miss
            if(cache.length == cacheSize){
                cache.shift();
            }
            cache.push(cities[i]);
        }
    }
    return answer;
}