using System.Text;
using DSharpPlus;
using DSharpPlus.EventArgs;
using Microsoft.Extensions.Logging;
using Newtonsoft.Json;

namespace mainBot
{
    public class RealmsBot
    {
        public readonly EventId BotEventId = new EventId(42, "RealmsBot");
        public DiscordClient Client { get; set; }

        public static void Main(string[] args)
        {
            var prog = new RealmsBot();
            prog.RunBotAsync().GetAwaiter().GetResult();
        }

        public async Task RunBotAsync()
            {
                var json = "";
                using (var fs = File.OpenRead("config.json"))
                using (var sr = new StreamReader(fs, new UTF8Encoding(false)))
                    json = await sr.ReadToEndAsync();

                var cfgjson = JsonConvert.DeserializeObject<ConfigJson>(json);
                var cfg = new DiscordConfiguration
                {
                    Token = cfgjson.Token,
                    TokenType = TokenType.Bot,

                    AutoReconnect = true,
                    MinimumLogLevel = LogLevel.Debug
                };
                this.Client = new DiscordClient(cfg);

                this.Client.Ready += this.Client_Ready;
                this.Client.GuildAvailable += this.Client_GuildAvailable;
                this.Client.ClientErrored += this.Client_ClientErrored;

                await this.Client.ConnectAsync();

                await Task.Delay(-1);
            }

        private Task Client_Ready(DiscordClient sender, ReadyEventArgs e)
        {
            sender.Logger.LogInformation(BotEventId, "Client is ready to process events.");
            return Task.CompletedTask;
        }

        private Task Client_GuildAvailable(DiscordClient sender, GuildCreateEventArgs e)
        {
            sender.Logger.LogInformation(BotEventId, $"Guild available: {e.Guild.Name}");
            
            return Task.CompletedTask;
        }

        private Task Client_ClientErrored(DiscordClient sender, ClientErrorEventArgs e)
        {
            sender.Logger.LogError(BotEventId, e.Exception, "exception occured");

            return Task.CompletedTask;
        }
    }

    public struct ConfigJson
    {
        [JsonProperty("token")]
        public string Token { get; private set; }
        
        [JsonProperty("prefix")]
        public string CommandPrefix { get; private set; }
    }
}
