// Import Swing library components
import javax.swing.*;
import java.awt.event.*;

// Main class
public class Main {

    // Main method
    public static void main(String[] args) {
        // Create a frame
        JFrame frame = new JFrame("GUI Application");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        // Create a button
        JButton button = new JButton("Click me");
        frame.getContentPane().add(button);

        // Add action listener to button
        button.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                // Show message dialog
                JOptionPane.showMessageDialog(null, "CLICK");
                // Show 'tyy' in a text box
                JTextField textField = new JTextField("tyy", 10);
                JOptionPane.showMessageDialog(null, textField);
            }
        });

        // Set frame visibility
        frame.setVisible(true);
    }
}