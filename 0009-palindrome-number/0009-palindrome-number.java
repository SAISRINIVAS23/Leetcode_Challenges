class Solution {
    public boolean isPalindrome(int x) {
        if (x<0 || x%10==0 && x!=0){
            return false;
        }

        int re=0;
        int or=x;

        while(x>re){
            re=re*10+x%10;
            x/=10;
        }

        return re==x || x==re/10;
    }
}