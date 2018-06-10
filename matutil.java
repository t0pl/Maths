import java.util.Scanner;

public class matutil {
	public static void main(String[] args) {
		Scanner reader = new Scanner(System.in);
		System.out.println("Taper un nombre: ");
		double nb = reader.nextDouble();
    	System.out.println("................................................................");
		for (int i=1; i <= nb+1; i++) {
        	if (nb/i == Math.round(nb/i)){
        		System.out.println(nb + " est divisible par " + i);
            	System.out.println(nb + " divise par " + i + " vaut " + nb/i);
                System.out.println(" ");
        	} else {
            	continue; }
        }
    	for (int x = 1; x <= 28; x++) {
        	System.out.println(x + " fois " + nb + "= " + x*nb);
    }
    System.out.println(" ");
    System.out.println("Carre: " + nb*nb);
    System.out.println(" ");
    if (Math.sqrt(nb) == Math.round(Math.sqrt(nb))){
        System.out.println("La racine carree de " + nb + " tombe juste");
        System.out.println(" ");
    } else{
        System.out.println("La racine carree de "  + nb + " ne tombe pas juste");
    	System.out.println("Racine carree: " + Math.sqrt(nb));
        System.out.println(" ");
    }
    for (int v=1; v <= 11; v++) {
        System.out.println("Exposant " + v +": " + Math.pow(nb, v));
        }
	}
}