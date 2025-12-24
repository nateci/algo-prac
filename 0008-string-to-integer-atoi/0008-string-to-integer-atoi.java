class Solution {
    public int myAtoi(String s) {
        // Define 32-bit integer bounds
        int INT_MAX = Integer.MAX_VALUE;  // 2147483647
        int INT_MIN = Integer.MIN_VALUE;  // -2147483648
        
        // Step 1: Remove leading whitespace
        int i = 0;
        while (i < s.length() && s.charAt(i) == ' ') {
            i++;
        }
        
        // Check if we've reached the end
        if (i == s.length()) {
            return 0;
        }
        
        // Step 2: Determine sign
        int sign = 1;
        if (s.charAt(i) == '-') {
            sign = -1;
            i++;
        } else if (s.charAt(i) == '+') {
            i++;
        }
        
        // Step 3: Convert digits to integer
        int result = 0;
        while (i < s.length() && Character.isDigit(s.charAt(i))) {
            int digit = s.charAt(i) - '0';
            
            // Check for overflow before adding the digit
            // If result > INT_MAX / 10, then result * 10 will overflow
            // If result == INT_MAX / 10, then result * 10 + digit might overflow
            if (result > INT_MAX / 10 || (result == INT_MAX / 10 && digit > 7)) {
                return sign == 1 ? INT_MAX : INT_MIN;
            }
            
            result = result * 10 + digit;
            i++;
        }
        
        // Step 4: Apply sign and return
        return sign * result;

    }
}