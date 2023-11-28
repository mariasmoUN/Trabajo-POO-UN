package friends;

import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import javax.swing.JOptionPane;

public class DeleteFriend {
    public static void eliminarContacto(String nombreAEliminar) {
        try {
            // Using file pointer creating the file.
            File file = new File("friendsContact.txt");

            if (!file.exists()) {

                JOptionPane.showMessageDialog(null, "El archivo no existe.");

                return;
            }

            // Opening file in reading and write mode.
            RandomAccessFile raf = new RandomAccessFile(file, "rw");
            boolean found = false;

            // Creating a temporary file with file pointer as tmpFile.
            File tmpFile = new File("temp.txt");

            // Opening this temporary file in ReadWrite Mode
            RandomAccessFile tmpraf = new RandomAccessFile(tmpFile, "rw");

            // Set file pointer to start
            raf.seek(0);

            // Traversing the friendsContact.txt file
            while (raf.getFilePointer() < raf.length()) {
                // Reading line from the file.
                String nameNumberString = raf.readLine();
                int index = nameNumberString.indexOf('!');
                String name = nameNumberString.substring(0, index);

                // Check if the fetched contact is the one to be deleted
                if (name.equals(nombreAEliminar)) {
                    found = true;
                    continue; // Skip inserting this contact into the temporary file
                }

                // Add this contact in the temporary file
                tmpraf.writeBytes(nameNumberString);
                tmpraf.writeBytes(System.lineSeparator());
            }

            raf.setLength(tmpraf.length());

            // Closing the resources.
            tmpraf.close();
            raf.close();

            // Deleting the temporary file
            tmpFile.delete();

            if (found) {

                JOptionPane.showMessageDialog(null, "Amigo eliminado.");
            } else {

                JOptionPane.showMessageDialog(null, "El nombre no existe.");
            }
        } catch (IOException ioe) {
            System.out.println(ioe);
        }
    }
}
