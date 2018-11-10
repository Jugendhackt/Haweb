package org.jugendhackt.HAWebDesktop.Gui;

import org.jugendhackt.HAWebDesktop.Util;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.net.URL;

public class MainGui {
    public static JFrame frame;
    private JButton homeButton;
    private JButton knowHowButton;
    private JButton homeworkButton;
    private JButton chatButton;
    private JPanel Mainpanel;
    private JPanel topbar;
    private JPanel HomePane;
    private JLabel linkHomePane;


    public JPanel MainGui() {
        linkHomePane.addMouseListener(new MouseListener() {
            public void mouseClicked(MouseEvent e) {

            }

            public void mousePressed(MouseEvent e) {

            }

            public void mouseReleased(MouseEvent e) {
                try {
                    Util.openWebpage(new URL("https://github.com/AntonK123/Haweb"));
                } catch (Exception lk) {

                }
            }

            public void mouseEntered(MouseEvent e) {

            }

            public void mouseExited(MouseEvent e) {

            }
        });
        linkHomePane.setCursor(Cursor.getPredefinedCursor(Cursor.HAND_CURSOR));


        homeButton = Util.makeTopBarClick(homeButton, Gui.HOME);
        knowHowButton = Util.makeTopBarClick(knowHowButton, Gui.KNOWHOW);
        homeworkButton = Util.makeTopBarClick(homeworkButton, Gui.HOMEWORK);
        chatButton = Util.makeTopBarClick(chatButton, Gui.CHAT);

        homeButton = makebtn(homeButton, false);
        knowHowButton = makebtn(knowHowButton, true);
        homeworkButton = makebtn(homeworkButton, true);
        chatButton = makebtn(chatButton, true);
        return Mainpanel;

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
}
