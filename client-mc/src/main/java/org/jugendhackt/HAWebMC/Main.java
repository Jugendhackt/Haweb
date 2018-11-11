package org.jugendhackt.HAWebMC;

import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;
import org.jugendhackt.HAWebMC.Command.Connect;
import org.jugendhackt.HAWebMC.Command.Disconnect;
import org.jugendhackt.HAWebMC.Command.Send;
import org.jugendhackt.HAWebMC.communication.Websocket;

import java.util.ArrayList;
import java.util.List;

public class Main extends JavaPlugin {

    public static final String PREFIX = "§7[§2Hausaufgaben§8-§2Chat§7] ";
    public static List<Websocket> websockets;

    @Override
    public void onEnable() {
        websockets = new ArrayList<>();
        System.out.println("HA-WEB MC-Client enabled!");

        Bukkit.getPluginCommand("connect").setExecutor(new Connect());
        Bukkit.getPluginCommand("sendmessage").setExecutor(new Send());
        Bukkit.getPluginCommand("disconnect").setExecutor(new Disconnect());
    }

    @Override
    public void onDisable() {
        for (Websocket socket:
             websockets) {
            socket.close();
        }
    }

}
