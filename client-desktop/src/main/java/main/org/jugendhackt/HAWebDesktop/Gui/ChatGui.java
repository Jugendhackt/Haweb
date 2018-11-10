package main.org.jugendhackt.HAWebDesktop.Gui;

import main.org.jugendhackt.HAWebDesktop.Util;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ChatGui {
    private JPanel Chatpane;
    private JButton knowHowButton;
    private JButton homeworkButton;
    private JButton chatButton;
    private JButton homeButton;
    private JPanel topbar;
    private JList Chatcontent;
    private JTextField messfield;
    private JButton submitMessage;
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
        DefaultListModel model = new DefaultListModel();

        Chatcontent.setModel(model);

        submitMessage.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println(Chatcontent.getModel().getSize());
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

    public void addMessage(String mess) {
        ListModel model = Chatcontent.getModel();
        DefaultListModel defaultListModel = new DefaultListModel();

        for(int i = 0; i < model.getSize(); i++) {
            defaultListModel.addElement(model.getElementAt(i));
        }
        Chatcontent.setModel(defaultListModel);
        System.out.println("Eingesetzt!");
    }


}
