using DSharpPlus;
using DSharpPlus.Entities;
using DSharpPlus.Net;
using DSharpPlus.SlashCommands;
using mainBot;

namespace Ribbit.Ribbit.SlashCommands
{
    public class BaseCommands : ApplicationCommandModule
    {
        [SlashCommand("Ping", "Simple ping pong command")]
        public async Task Ping(InteractionContext ctx)
        {
            await ctx.CreateResponseAsync(InteractionResponseType.DeferredChannelMessageWithSource);
            await ctx.EditResponseAsync(new DiscordWebhookBuilder().WithContent($"Pong!"));
        }
        
    }
}