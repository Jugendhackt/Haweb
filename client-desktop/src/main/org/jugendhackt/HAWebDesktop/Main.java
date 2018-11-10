package main.org.jugendhackt.HAWebDesktop;

import main.org.jugendhackt.HAWebDesktop.Gui.Gui;
import main.org.jugendhackt.HAWebDesktop.Gui.MainGui;

import javax.swing.*;

public class Main {


    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (InstantiationException e) {
            e.printStackTrace();
        } catch (IllegalAccessException e) {
            e.printStackTrace();
        } catch (UnsupportedLookAndFeelException e) {
            e.printStackTrace();
        }
        new Gui();

    }

}
