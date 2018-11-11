package org.jugendhackt.HAWebMC.Command;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.craftbukkit.libs.jline.internal.Nullable;
import org.bukkit.entity.Player;
import org.jugendhackt.HAWebMC.Main;
import org.jugendhackt.HAWebMC.communication.Websocket;

public class Send implements CommandExecutor {
    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
        Player p = (Player) sender;
        if(args.length >= 1) {

            String mess = "";
            for (String s:
                 args) {
                mess = mess + " " + s;
            }

            Websocket websocket = getSocketByPlayer(p);
            if(websocket != null) {
                websocket.sendmessage("chat","[MC] " + sender.getName() + ": " + mess);
            } else {
                sender.sendMessage(Main.PREFIX + "§cAktuell sind keine verbindungen offen!");
            }
        }





        return true;
    }
    @Nullable
    private Websocket getSocketByPlayer(Player p) {
        for (Websocket socket:
                Main.websockets) {
            if(socket.getTarget().equals(p)) {
               return socket;
            }

        }
        return null;
    }
}
