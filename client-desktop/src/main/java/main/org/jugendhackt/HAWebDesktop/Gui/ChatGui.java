// This is an special build get the newest at https://github.com/antonk123/haweb
package main.org.jugendhackt.HAWebDesktop.Gui;

import main.org.jugendhackt.HAWebDesktop.Main;
import main.org.jugendhackt.HAWebDesktop.Message;
import main.org.jugendhackt.HAWebDesktop.Util;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class ChatGui {

    DefaultListModel model = new DefaultListModel();

    private JPanel Chatpane;
    private JButton knowHowButton;
    private JButton homeworkButton;
    private JButton chatButton;
    private JButton homeButton;
    private JPanel topbar;
    private JList Chatcontent;
    private JTextField messfield;
    private JButton submitMessage;
    private JPanel liste;
    private JTextArea output;
    private JLabel messagesField;
    private JButton knowhowButton;



    public JPanel getChatpane() {
        homeButton = Util.makeTopBarClick(homeButton, Gui.HOME);
        knowHowButton = Util.makeTopBarClick(knowHowButton, Gui.KNOWHOW);
        homeworkButton = Util.makeTopBarClick(homeworkButton, Gui.HOMEWORK);
        chatButton = Util.makeTopBarClick(chatButton, Gui.CHAT);

        homeButton = makebtn(homeButton, true);
        knowHowButton = makebtn(knowHowButton, true);
        homeworkButton = makebtn(homeworkButton, true);
        chatButton = makebtn(chatButton, false);

        //liste.add(new JLabel("Hallo Welt"));

        Font liste = new Font("Arial1", Font.PLAIN, 15);
        output.setFont(liste);


        submitMessage.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                //Main.init();
                Main.websocket.sendmessage("chat", messfield.getText());
                messfield.setText("");
                //messagesField.setText("Hey wake up!");
            }
        });

        messfield.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {

            }

            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == KeyEvent.VK_ENTER) {
                    Main.websocket.sendmessage("chat", messfield.getText());
                    messfield.setText("");
                }

            }

            @Override
            public void keyReleased(KeyEvent e) {

            }
        });




        return Chatpane;
    }

    public JButton makebtn(JButton button, boolean back) {

        button.setForeground(Color.WHITE);
        if(back) {
            button.setOpaque(false);
            button.setContentAreaFilled(false);
            button.setBorderPainted(false);
        }


        return button;
    }

    public void addMessage(Message mess) {
        Main.messages.add(mess);
        output.append("\n(" + mess.getTimestamp() + ") " + mess.getSender() + ": " + mess.getMessage());
        //System.out.println("Appended: " + "(" + mess.getTimestamp() + ") " + mess.getSender() + ": " + mess.getMessage());
        //System.out.println(output.getText());
    }


}
