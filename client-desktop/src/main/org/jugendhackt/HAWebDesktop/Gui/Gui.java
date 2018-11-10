package main.org.jugendhackt.HAWebDesktop.Gui;

import javax.swing.*;

public class Gui {
    public static JFrame frame;
    public static int Site = 0;
    public static final int HOME = 0;
    public static final int KNOWHOW = 1;
    public static final int HOMEWORK = 2;
    public static final int CHAT = 3;
    public Gui() {
        frame = new JFrame("HausaufgabenWeb Desktop");
        //frame.getContentPane().add(new MainGui().MainGui());
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(new KNOWHOWGui().getKnowhowPanel());
        frame.setSize(1920, 1080);
        frame.setExtendedState(java.awt.Frame.MAXIMIZED_BOTH);
        //frame.pack();
        frame.setVisible(true);
    }


}
