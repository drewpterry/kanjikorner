export default {

  arrayToCommaSeperatedString (array) {
    var formattedString = ''
    var arrayLen = array.length
    array.forEach(function (string, i) {
      formattedString += i < arrayLen - 1 ? string + ', ' : string
    })
    return formattedString
  },

  getLevenshtein: function (a, b) {
    function levenshteinenator (a, b) {
      var cost
      var m = a.length
      var n = b.length

      // make sure a.length >= b.length to use O(min(n,m)) space
      if (m < n) {
        var c = a; a = b; b = c
        var o = m; m = n; n = o
      }

      var r = []; r[0] = []
      for (c = 0; c < n + 1; ++c) {
        r[0][c] = c
      }

      for (var i = 1; i < m + 1; ++i) {
        r[i] = []; r[i][0] = i
        for (var j = 1; j < n + 1; ++j) {
          cost = a.charAt(i - 1) === b.charAt(j - 1) ? 0 : 1
          r[i][j] = minimator(r[i - 1][j] + 1, r[i][j - 1] + 1, r[i - 1][j - 1] + cost)
        }
      }

      return r[r.length - 1][r[r.length - 1].length - 1]
    }

    /**
     * Return the smallest of the three numbers passed in
     * @param Number x
     * @param Number y
     * @param Number z
     * @return Number
     */
    function minimator (x, y, z) {
      if (x < y && x < z) return x
      if (y < x && y < z) return y
      return z
    }

    return levenshteinenator(a, b)
  }
}
