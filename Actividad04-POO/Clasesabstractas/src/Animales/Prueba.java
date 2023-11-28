/*package Animales;
public class Prueba {
    public static void main(String[] args) {
        Animal[] animales = new Animal[4];
        animales[0] = new Gato();
        animales[1] = new Perro();
        animales[2] = new Lobo();
        animales[3] = new Leon();
        for (int i = 0; i < animales.length; i++) {
            System.out.println(animales[i].getNombreCientifico());
            System.out.println("Sonido: " + animales[i].getSonido());
            System.out.println("Alimentos: " + animales[i].getAlimentos());
            System.out.println("Habitat: " + animales[i].getHabitat());
            System.out.println();
        }
    }
}*/

package CarreraCiclistica;
import java.util.Scanner;
import java.util.Vector;
public class Equipo {
    private String nombre;
    private static double totalTiempo;
    private String país;
    Vector listaCiclistas;


    public Equipo(String nombre, String país) {
        this.nombre = nombre;
        this.país = país;
        totalTiempo = 0;
        listaCiclistas = new Vector();
    }


    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


    private String getPaís() {
        return país;
    }
    private void setPaís(String país) {
        this.país = país;
    }
    void añadirCiclista(Ciclista ciclista) {
        listaCiclistas.add(ciclista);
    }
    void listarEquipo() {
        for (int i = 0; i < listaCiclistas.size(); i++) {
            Ciclista c = (Ciclista) listaCiclistas.elementAt((i));
            System.out.println(c.getNombre());
        }
    }
    void buscarCiclista() {
        Scanner sc = new Scanner(System.in);
        String nombreCiclista = sc.next();
        for (int i = 0; i < listaCiclistas.size(); i++) {
            Ciclista c = (Ciclista) listaCiclistas.elementAt(i);
            if (c.getNombre().equals(nombreCiclista)) {
                System.out.println(c.getNombre());
            }
        }
    }
    void calcularTotalTiempo() {
        for (int i = 0; i < listaCiclistas.size(); i++) {
            Ciclista c = (Ciclista) listaCiclistas.elementAt(i);
            totalTiempo = totalTiempo + c.getTiempoAcumulado();
        }
    }


    void imprimir() {
        System.out.println("Nombre del equipo = " + nombre);
        System.out.println("Pais = " + país);
        System.out.println("Total tiempo del equipo = " + totalTiempo);
    }
}
