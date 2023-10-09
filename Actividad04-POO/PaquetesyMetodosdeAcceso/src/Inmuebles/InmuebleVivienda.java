package Inmuebles;
public class InmuebleVivienda extends Inmueble {
    protected int numeroHabitaciones;
    protected int numeroBanos;
    public InmuebleVivienda(int identificadorInmobiliario, int area, String direccion, int numeroHabitaciones, int numeroBanos) {
        super(identificadorInmobiliario, area, direccion);
        this.numeroHabitaciones = numeroHabitaciones;
        this.numeroBanos = numeroBanos;
    }

    void imprimir() {
        super.imprimir();
        System.out.println("Numero de habitaciones = " + numeroHabitaciones);
        System.out.println("Numero de baños = " + numeroBanos);
    }
}
