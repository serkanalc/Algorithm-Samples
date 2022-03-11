fun solution(s: String): Int {
        
        var p = -1
        var i: Int
        var j: Int
        i = 0
        while (i < s.length) {
            j = i + 1
            while (j < s.length) {
                if (s[i] == s[j]) {
                    p = i
                    break
                }
                j++
            }
            if (p != -1) break
            i++
        }
        return p
    }
