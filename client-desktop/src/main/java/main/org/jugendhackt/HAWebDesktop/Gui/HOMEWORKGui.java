// This is an special build get the newest at https://github.com/antonk123/haweb
package main.org.jugendhackt.HAWebDesktop.Gui;

import main.org.jugendhackt.HAWebDesktop.Util;

import javax.swing.*;
import java.awt.*;

public class HOMEWORKGui {
    private JPanel topbar;
    private JButton homeworkButton;
    private JButton knowHowButton;
    private JButton chatButton;
    private JButton homeButton;
    private JPanel content;
    private JPanel homeworkMainPane;

    public JPanel getHomeworkPanel() {
        homeButton = Util.makeTopBarClick(homeButton, Gui.HOME);
        knowHowButton = Util.makeTopBarClick(knowHowButton, Gui.KNOWHOW);
        homeworkButton = Util.makeTopBarClick(homeworkButton, Gui.HOMEWORK);
        chatButton = Util.makeTopBarClick(chatButton, Gui.CHAT);

        homeButton = makebtn(homeButton, true);
        knowHowButton = makebtn(knowHowButton, true);
        homeworkButton = makebtn(homeworkButton, false);
        chatButton = makebtn(chatButton, true);

        return homeworkMainPane;
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
