using DSharpPlus.Entities;
using DSharpPlus.Menus;

namespace Ribbit.Ribbit.Infrastructure
{
   public class AuditLogs
   {
      public async Task Logging(AuditLogActionCategory actCat, AuditLogActionType actType)
      {
         // audit log types
         var create = actCat == AuditLogActionCategory.Create;
         var delete = actCat == AuditLogActionCategory.Delete;
         var other = actCat == AuditLogActionCategory.Other;
         var update = actCat == AuditLogActionCategory.Update;
         var logTypes = new[] 
            { create, delete, other, update };

         // create related logs
         var roleCreate = actType == AuditLogActionType.RoleCreate;
         var webhookCreate = actType == AuditLogActionType.WebhookCreate;
         var invCreate = actType == AuditLogActionType.InviteCreate;
         var channelCreate = actType == AuditLogActionType.ChannelCreate;
         var permNew = actType == AuditLogActionType.OverwriteCreate;
         var createLogs = new[] 
            { channelCreate, invCreate, webhookCreate, permNew, roleCreate };
         
         // delete related logs
         var roleDelete = actType == AuditLogActionType.RoleDelete;
         var webhookDelete = actType == AuditLogActionType.WebhookDelete;
         var invDelete = actType == AuditLogActionType.InviteDelete;
         var channelDelete = actType == AuditLogActionType.ChannelDelete;
         var permDel = actType == AuditLogActionType.OverwriteDelete;
         var MD = actType == AuditLogActionType.MessageDelete;
         var MBD = actType == AuditLogActionType.MessageBulkDelete;
         
         var deleteLogs = new[]
            { roleDelete, webhookDelete, invDelete, channelDelete, permDel, MD, MBD };
         
         // other logs
         var kick = actType == AuditLogActionType.Kick;
         var prune = actType == AuditLogActionType.Prune;
         var ban = actType == AuditLogActionType.Ban;
         var unban = actType == AuditLogActionType.Unban;
         var messagePin = actType == AuditLogActionType.MessagePin;
         var messageUnpin = actType == AuditLogActionType.MessageUnpin;
         var otherLogs = new[] 
            { ban, unban, prune, kick, messagePin, messageUnpin };
         
         // update related logs
         var guildUpdate = actType == AuditLogActionType.GuildUpdate;
         var roleUpdate = actType == AuditLogActionType.RoleUpdate;
         var webhookUpdate = actType == AuditLogActionType.WebhookUpdate;
         var userUpdate = actType == AuditLogActionType.MemberUpdate;
         var userRoleUpdate = actType == AuditLogActionType.MemberRoleUpdate;
         var channelsEdit = actType == AuditLogActionType.ChannelUpdate;
         var permUpdate = actType == AuditLogActionType.OverwriteUpdate;
         var updateLogs = new[]
            { guildUpdate, roleUpdate, webhookUpdate, userUpdate, userRoleUpdate, channelsEdit, permUpdate };
      }
   }
}