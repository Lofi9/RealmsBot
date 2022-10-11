using DSharpPlus;

namespace mainBot
{
    public class RealmsBot
    {
        public static void Main(string[] args)
        {
            var bot = new DiscordShardedClient(new DiscordConfiguration());

            
            bot.StartAsync();
        }
    }
}
