package main.org.jugendhackt.HAWebDesktop.Gui;

import main.org.jugendhackt.HAWebDesktop.Main;
import main.org.jugendhackt.HAWebDesktop.Message;

import javax.swing.*;
import java.awt.*;

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
        JPanel chatpane = new JPanel();
        //Main.messages.add("Test");
        //Main.messages.add("Test2");
        chatpane.setLayout(new BoxLayout(chatpane, BoxLayout.Y_AXIS));
        Font text = new Font("Arial", Font.BOLD, 30);
        Font timestamp = new Font("Arial", Font.LAYOUT_RIGHT_TO_LEFT, 28);
        Font sender = new Font("Arial", Font.ITALIC, 30);

        Main.messages.add(new Message("Hey", "0.0.0.0", "00:00:00"));
        Main.messages.add(new Message("Wake", "0.1.0.1", "00:20:00"));
        Main.messages.add(new Message("Up", "0.1.0.1", "00:20:00"));

        for (Message s:
             Main.messages) {
            JLabel author = new JLabel(s.getSender());
            JLabel mess = new JLabel(s.getMessage());
            JLabel time = new JLabel(s.getTimestamp());
            mess.setFont(text);
            author.setFont(sender);
            time.setFont(timestamp);
            chatpane.add(author);
            chatpane.add(mess);
            chatpane.add(time);
        }


        frame.getContentPane().add(chatpane);
        frame.setSize(1920, 1080);
        frame.setExtendedState(java.awt.Frame.MAXIMIZED_BOTH);
        //frame.pack();
        frame.setVisible(true);
        //chatpane.add(new JLabel("Hallo wwelt"));

    }


}
