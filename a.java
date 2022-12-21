class Program1 {
    public static void main(String[] args) {

        String cos = "asdasdasdaaaaa";
        char c = 'a';
        countChr(cos,c);
    }
    public static int countChr(String cos, char c){
        int licznik = 0;
        for(int i = 0; i<cos.length();i++){
            char akt = cos.charAt(i);
            if (akt == c) {
                licznik = licznik + 1;
            }

    }
        System.out.println("literek "+c+ " w zdaniu "+cos+" jest "+ licznik);
        return 0;

}
    public static String middle(String cos){
        int dlg = cos.length();
        if(dlg%2==0){
            return cos.charAt(dlg/2)+cos.charAt((dlg+1)/2);
        }else{
            return cos.charAt(dlg/2);
        }

    }}
