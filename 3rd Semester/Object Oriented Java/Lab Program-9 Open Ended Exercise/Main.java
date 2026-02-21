import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class DivisionUI {
    public static void main(String[] args) {

        JFrame frame = new JFrame("Integer Division");
        frame.setSize(350, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(4, 2));

        JLabel l1 = new JLabel("Num1:");
        JTextField t1 = new JTextField();

        JLabel l2 = new JLabel("Num2:");
        JTextField t2 = new JTextField();

        JLabel l3 = new JLabel("Result:");
        JTextField result = new JTextField();
        result.setEditable(false);

        JButton divideBtn = new JButton("Divide");

        divideBtn.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                try {
                    int num1 = Integer.parseInt(t1.getText());
                    int num2 = Integer.parseInt(t2.getText());

                    int res = num1 / num2;
                    result.setText(Integer.toString(res));
                }
                catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(frame,
                            "Please enter valid integers!",
                            "Number Format Error",
                            JOptionPane.ERROR_MESSAGE);
                }
                catch (ArithmeticException ex) {
                    JOptionPane.showMessageDialog(frame,
                            "Division by zero is not allowed!",
                            "Arithmetic Error",
                            JOptionPane.ERROR_MESSAGE);
                }
            }
        });

        frame.add(l1); frame.add(t1);
        frame.add(l2); frame.add(t2);
        frame.add(l3); frame.add(result);
        frame.add(divideBtn);

        frame.setVisible(true);
    }
}
