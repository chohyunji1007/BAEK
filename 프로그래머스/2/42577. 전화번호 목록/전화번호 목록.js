function solution(phone_book) {
    var answer = true;
    phone_book = phone_book.sort();
    for(var i=0; i<phone_book.length-1; i++){
        if (phone_book[i + 1].startsWith(phone_book[i])) {
            return false; // 접두사가 존재하는 경우
        }
    }
    
    return true;
}