package org.jugendhackt.HAWebMC.Command;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;
import org.bukkit.craftbukkit.libs.jline.internal.Nullable;
import org.bukkit.entity.Player;
import org.jugendhackt.HAWebMC.Main;
import org.jugendhackt.HAWebMC.communication.Websocket;

public class Disconnect implements CommandExecutor {
    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
        Player p = (Player)sender;
        Websocket websocket = getSocketByPlayer(p);
        if(websocket != null) {
            websocket.close();
        } else {
            sender.sendMessage(Main.PREFIX + "§cAktuell sind keine verbindungen offen!");
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
