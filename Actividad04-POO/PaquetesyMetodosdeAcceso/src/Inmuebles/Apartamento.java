package Inmuebles;
public class Apartamento extends InmuebleVivienda {
    public Apartamento(int identificadorInmobiliario, int area, String direccion, int numeroHabitaciones, int numeroBanos) {
        super(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBanos);
    }
    void imprimir() {
        super.imprimir();
    }
}