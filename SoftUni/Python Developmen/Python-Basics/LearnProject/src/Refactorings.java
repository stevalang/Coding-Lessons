import javax.swing.*;
import java.awt.*;

class Test{
    private static JButton glassButton;
    private static JPanel glass;

    public static void main(String[] args) {

        final Dimension myDimension = new Dimension(100, 100);

        JPanel panel = init(myDimension);

        JFrame frame = new JFrame();
        frame.setGlassPane(glass);
        glass.setVisible(true);
        frame.setContentPane(panel);
        frame.pack();
        frame.setVisible(true);
    }

    private static JPanel init(Dimension myDimension) {
        JButton button = new JButton("Test");
        button.setPreferredSize(myDimension);

        glassButton = new JButton("Block");
        JPanel panel = new JPanel();
        panel.add(button);

        glass = new JPanel();
        glass.setOpaque(false);
        glass.add(glassButton);
        return panel;
    }
}