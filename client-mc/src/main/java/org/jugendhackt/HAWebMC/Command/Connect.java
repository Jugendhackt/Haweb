package org.jugendhackt.HAWebMC.Command;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.entity.Player;
import org.jugendhackt.HAWebMC.Main;
import org.jugendhackt.HAWebMC.communication.Websocket;

import java.net.URISyntaxException;

public class Connect implements CommandExecutor {
    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
        Player p = (Player) sender;

        if(args.length == 1) {
            try {
                Websocket websocket = new Websocket(args[0], p);
                websocket.open();
                Main.websockets.add(websocket);
            } catch (URISyntaxException e) {
                e.printStackTrace();
            }
        }
        return true;
    }
}
