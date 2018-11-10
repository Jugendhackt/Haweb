package main.org.jugendhackt.HAWebDesktop.Gui;

import main.org.jugendhackt.HAWebDesktop.Util;

import javax.swing.*;
import java.awt.*;

public class KNOWHOWGui {
    private JPanel KnowhowPanel;
    private JButton knowHowButton;
    private JButton homeworkButton;
    private JButton chatButton;
    private JButton homeButton;
    private JPanel topbar;

    public JPanel getKnowhowPanel() {
        homeButton = Util.makeTopBarClick(homeButton, Gui.HOME);
        knowHowButton = Util.makeTopBarClick(knowHowButton, Gui.KNOWHOW);
        homeworkButton = Util.makeTopBarClick(homeworkButton, Gui.HOMEWORK);
        chatButton = Util.makeTopBarClick(chatButton, Gui.CHAT);

        homeButton = makebtn(homeButton, true);
        knowHowButton = makebtn(knowHowButton, false);
        homeworkButton = makebtn(homeworkButton, true);
        chatButton = makebtn(chatButton, true);

        return KnowhowPanel;
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
