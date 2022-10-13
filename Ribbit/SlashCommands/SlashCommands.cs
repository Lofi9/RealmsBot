using DSharpPlus;
using DSharpPlus.Entities;
using DSharpPlus.SlashCommands;

namespace Ribbit.Ribbit.SlashCommands
{
    public class SlashCommands : ApplicationCommandModule
    {
        [SlashCommand("Ping", "Simple ping pong command")]
        public async Task Ping(InteractionContext ctx)
        {
            await ctx.CreateResponseAsync(InteractionResponseType.DeferredChannelMessageWithSource);
            await ctx.EditResponseAsync(new DiscordWebhookBuilder().WithContent($"Pong!"));
        }
        
    }
}