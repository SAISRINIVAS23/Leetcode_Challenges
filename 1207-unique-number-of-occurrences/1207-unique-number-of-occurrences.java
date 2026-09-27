class Solution {
    public boolean uniqueOccurrences(int[] arr) {
         HashMap<Integer,Integer> map=new HashMap<>();
         for(int x:arr){
            map.put(x,map.getOrDefault(x,0)+1);
         }

         HashSet<Integer> set=new HashSet<>();
         for(int q: map.values()){
            if(set.contains(q)){
                return false;
            }
            set.add(q);
         }

        return true;
        
    }
}