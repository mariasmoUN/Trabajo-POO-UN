package friends;

import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.lang.NumberFormatException;
import javax.swing.JOptionPane;

class DisplayFriends {

    public static void main(String data[]) {

        try {

            String nameNumberString;
            String name;
            long number;

            // Using file pointer creating the file.
            File file = new File("friendsContact.txt");

            if (!file.exists()) {

                // Create a new file if not exists.
                file.createNewFile();
            }

            // Opening file in reading mode.
            RandomAccessFile raf = new RandomAccessFile(file, "r");
            boolean found = false;

            // Traversing the file
            // getFilePointer() gives the current offset
            // value from the start of the file.
            while (raf.getFilePointer() < raf.length()) {

                // Reading a line from the file.
                nameNumberString = raf.readLine();

                // Splitting the string to get name and number
                String[] lineSplit = nameNumberString.split("!");


                if (lineSplit.length >= 2) {
                    // Separating name and number.
                    name = lineSplit[0];
                    number = Long.parseLong(lineSplit[1]);

                    // Print the contact data

                    JOptionPane.showMessageDialog(null,
                            "Friend Name: " + name + "\n"
                                    + "Contact Number: " + number + "\n");
                }
            }
        } catch (IOException ioe) {
            System.out.println(ioe);
        } catch (NumberFormatException nef) {
            System.out.println(nef);
        }
    }
}
