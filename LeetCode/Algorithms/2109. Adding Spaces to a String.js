/**
 * @param {string} s
 * @param {number[]} spaces
 * @return {string}
 */
var addSpaces = function(s, spaces) {
        let i = 0;
        let j = 0;
        let ans = '';
        while (i < s.length) {
            if (i === spaces[j]) {
                ans += ' ';
                j += 1;
            }
            ans += s[i];
            i += 1;
        }
        return ans;
};
