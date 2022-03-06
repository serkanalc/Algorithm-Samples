fun main(){
    var toplam = 0
    for (i in 1 until 1000){ // Until sonuncu değeri dahil etmez.
        if ( i % 3 == 0 || i % 5 == 0 ){
            toplam += i
        }
        else {
            continue
        }
    }
    println(toplam)
}
